import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

condizioni = pd.read_csv('condizioni stradali 20-21.csv', sep=';')
print(condizioni.head())
print(condizioni.shape)

# faccio due df , uno per il 2020 e uno per il 2021
condizioni_2020 = condizioni[condizioni['Anno'].isin([2020])]
condizioni_2021 = condizioni[condizioni['Anno'].isin([2021])]

# barplot parcheggi 
sns.barplot(data = condizioni, y = 'Regione', x = 'parcheggio', hue='Anno')
plt.show()

# ---parcheggi 2021---
# creo una lista ordinata decrescente della colonna parcheggio da passare nel barplot
plot_order = condizioni_2021.groupby('Regione')['parcheggio'].sum().sort_values(ascending=False) # così creo una raggruppamento della coppia regioni-parcheggio ordinate decrescenti per la somma dei parcheggio
plot_order = condizioni_2021.groupby('Regione')['parcheggio'].sum().sort_values(ascending=False).index.values # così creo la lista delle regioni ordinate decrescenti per la somma dei parcheggio

sns.barplot(data = condizioni_2021, y = 'Regione', x = 'parcheggio', order = plot_order)
plt.show()

# --- mezzi pubblici 2021
plot_order = condizioni_2021.groupby('Regione')['mezzi pubblici'].sum().sort_values(ascending=False).index.values
sns.barplot(data = condizioni_2021, y = 'Regione', x = 'mezzi pubblici', order = plot_order)
plt.show()

# scatterplot
sns.scatterplot(data = condizioni_2021, y = 'parcheggio', x = 'mezzi pubblici', hue = 'Regione')
plt.show()