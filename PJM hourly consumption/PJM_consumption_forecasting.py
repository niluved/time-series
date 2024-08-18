from tkinter.ttk import Style
from turtle import color, title
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import xgboost as xgb


# imposto la paletta dei colori di seaborn, per usarla dopo come argomento opzionale nei plot ecc
color_pal = sns.color_palette()

# imposto uno stile di matpltlib 
plt.style.use('fivethirtyeight')

# --DATA PREPARATION--

# importo il dataset
df = pd.read_csv('PJME_hourly.csv')

# print(df.tail())

# imposto come indice la colonna delle date e lo imposto come tipo 'datetime' 
df = df.set_index('Datetime')
df.index = pd.to_datetime(df.index)

# creo un plot della serie e lo mostro con il comando show
df.plot(style='.', figsize=(15,5), color=color_pal[0], title='PJME hourly consumption in MWh') 
plt.show()

# --TRAIN AND TEST SPLIT--

# le date prima del 2015 vengono prese come training del modello, mentre dopo il 2015 è preso come test del modello
train = df.loc[df.index < '01-01-2015'] 
test = df.loc[df.index >= '01-01-2015'] 

# li metto tutti e due dentro lo stesso grafico creando un subplot (il comando subplots ritona una tupla che contiene gli oggetti figure e axes, quindi faccio un semplice unpacking, poi la variabile fig in realtà non la userò)
fig, ax = plt.subplots(figsize=(15,5))
train.plot(ax=ax, label='Training Set', title='Train and Test split')
test.plot(ax=ax, label='Test set')
# aggiungo una linea verticale che divide le due serie
ax.axvline('01-01-2015', color='black')
# aggiungo una legenda 
ax.legend(['Training set', 'Test set'])
plt.show()

# guardo i dati di una settimana e li plotto per vedere in effetti i comportamenti stagionali che mi serviranno per le feature che aggiungerò fra poco
df.loc[(df.index > '01-01-2010') & (df.index < '01-08-2010')].plot(figsize=(15, 5), title='Week Of Data')
plt.show()

# --FEATURE CREATION--

# scrivo una funzione per creare nuove colonne nel nostro dataframe per ognuna delle componenti stagionali
def create_features(df):
    df = df.copy()
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    return df

df = create_features(df)

# -- VISUALIZZARE LE FEATURES PER MODELLARE LE RELAZIONI--

# utilizzo la funzione boxplot di seaborn per mostrare i dati orari in un'unico grafico 

fig , ax = plt.subplots(figsize=(10,8))             # faccio la stessa cosa di prima usando subplots
sns.boxplot(data=df, x='hour', y='PJME_MW')         # utilizzo le colonne 'hour' e 'PJME_MW' del dataframe come x e y
ax.set_title('MW by hour')
plt.show()

# posso fare la stessa cosa con i dati mensili (solo cambio la paleatta dei colori)
fig , ax = plt.subplots(figsize=(10,8))             
sns.boxplot(data=df, x='month', y='PJME_MW', palette='Blues')         
ax.set_title('MWh by month')
plt.show()

# --CREAZIONE DEL MODELLO di REGRESSIONE SUI DATI DI TRAINING--

# adesso lancio la funzione che crea le features sia sui dati di training che su quelli di test (ho inserito la riga df=df.copy() nella funzione per evitare di sovrascrivere il df adesso)
train = create_features(train)
test = create_features(test)

# riporto per comodità i nomi delle colonne del df separandole tra features e target, cioè rispettivamente tra regressori (x) e variabile dipendente (Y)
FEATURES = ['dayofyear', 'hour', 'dayofweek', 'quarter', 'month', 'year']
TARGET = 'PJME_MW'

# creo le variabili x e y di train e di test che contengono i relativi nomi delle colonne del df
X_train = train[FEATURES]
y_train = train[TARGET]

X_test = test[FEATURES]
y_test = test[TARGET]

# creo un modello di regressione e lo fitto sui dati di training 
reg = xgb.XGBRegressor(n_estimators=1000, early_stopping_rounds=50, learning_rate=0.01)

reg.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        verbose=100)

# evidenziamo l'importanza di ogni singola feature (mi sa che sono i coefficienti dei regressori) e li metto dentro un dataframe per comodità (con i nomi delle colonne parlanti)
fi = pd.DataFrame(data=reg.feature_importances_,
             index=reg.feature_names_in_,
             columns=['importance'])
# li metto in ordine plottandoli con un grafico a barre orizzontali
fi.sort_values('importance').plot(kind='barh', title='Feature Importance')
plt.show()

# --FORECAST DEL MODELLO SUI DATI DI TEST--

# creo una serie di previsioni a partire dalle x della serie test e creo una nuova colonna nel df
test['prediction'] = reg.predict(X_test)

# faccio un merge tra il nostro df delle previsioni (che ha però tutte le feature dentro più la colonna appena creata, quindi seleziono solo quest'ultima per fare il merge) e il nostro df originario (faccio il join sulle colonne 'index' dei due df)
df = df.merge(test[['prediction']], how='left', left_index=True, right_index=True)

# faccio il plot di queste serie
ax = df[['PJME_MW']].plot(figsize=(15, 5))
df['prediction'].plot(ax=ax, style='.')

# aggiungo la legenda e il titolo
plt.legend(['Truth Data', 'Predictions'])
ax.set_title('Raw Dat and Prediction')
plt.show()

# faccio un focus su una week per vedere meglio quanto (male!) fitta il modello
ax = df.loc[(df.index > '04-01-2018') & (df.index < '04-08-2018')]['PJME_MW'] \
    .plot(figsize=(15, 5), title='Week Of Data')
df.loc[(df.index > '04-01-2018') & (df.index < '04-08-2018')]['prediction'] \
    .plot(style='.')
plt.legend(['Truth Data','Prediction'])
plt.show()




