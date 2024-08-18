import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('lineplot.csv', parse_dates=[3])       # NB metto parse_dates[3] perchè voglio che pandas trasformi la colonna 3 in formato datetime
print(df.head())
print(df.shape)

# data preparation: rinomino due colonne, ne creo altre e filtro solo due 'location'
df.rename(columns={'SystemCodeNumber': 'Location', 'LastUpdated': 'Timestamp'}, inplace=True)

df['Day'] = df['Timestamp'].dt.date     # creo la colonna giorno usando la funzione dt (datetime) 
df['Month'] = df['Timestamp'].dt.month     # creo la colonna mese usando la funzione dt (datetime) 
df['Hour'] = df['Timestamp'].dt.hour     # creo la colonna ora usando la funzione dt (datetime) 

park = df[df['Location'].isin(['Broad Street', 'NIA South'])]       # filtro due location

print(park.head())
print(park.shape)

# creo il lineplot (aggiunge di default l'intervallo di confidenza al 95%, si può cambiare all'80% ad es aggiungendo il parametro ci=80 o rimuoverlo del tutto mettendo ci=None)
sns.lineplot(data= park, x = 'Day', y = 'Occupancy')
plt.show()

# anche qui posso aggiungere l'argomento hue per inserire le diverse categorie (oltre che le solite style e size al posto di hue oppure in aggiunta a hue)
sns.lineplot(data= park, x = 'Hour', y = 'Occupancy', hue='Month', ci=None)
plt.show()
