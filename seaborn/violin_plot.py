import seaborn as sns
import matplotlib.pyplot as plt

# il Violin Plot è la somma di un boxplot e di un doppio KDE plot (kernel density estimation) (ossia come se fosse allo specchio)

# ---per iniziare uso lo stesso df usato per i boxplot e faccio le stesse pulizie dei dati...----

cars = sns.load_dataset('mpg')

# pulisco il df dai valori null
print(cars.head())
print(cars.shape)
cars.dropna(inplace = True)
print(cars.shape)

# seleziono solo le auto che hanno 4,6,8 cilindri (escludendo gli altri valori perchè ci sono auto che ne hanno 3 o 5 e non li voglio)
print(cars['cylinders'].value_counts())        # vedo le occorrenze nella colonna 'cylinders'
cars = cars[cars['cylinders'].isin([4,6,8])]   # modifico il df scegliendo solo le parti in cui i cilindri sono 4,6,8
print(cars.shape)

# faccio il violinplot con due colonne
sns.violinplot(data = cars, x = 'cylinders', y = 'displacement')
plt.show()

# faccio il violinplot per due colonne e una categoria (hue)
sns.violinplot(data = cars, x = 'cylinders', y = 'displacement', hue = 'origin')
plt.show()

# posso anche rinunciare alla simmetria dei violini, mettendo insieme la stessa categoria sui due lati (chiaramente la hue deve avere solo due valori)
# utilizzo il parametro SPLIT = True
# (per farlo modifico il df mettendo solo europe e japan come origin)
sns.violinplot(data = cars[cars['origin'].isin(['europe','japan'])], x = 'cylinders', y = 'displacement', hue = 'origin', split=True)
plt.show()

# posso mostrare i quartili su entrambe le facce del violino, introducendo l'argomento 'inner'
sns.violinplot(data = cars[cars['origin'].isin(['europe','japan'])], x = 'cylinders', y = 'displacement', hue = 'origin', split=True, inner='quartiles')
plt.show()

# posso mostrare la reale grandezza delle facce del violino, introducendo l'argomento scale='count' e scale_hue=False (altrimenti di default le due facce hanno la stessa area)
sns.violinplot(data = cars[cars['origin'].isin(['europe','japan'])], x = 'cylinders', y = 'displacement', hue = 'origin', split=True, inner='quartiles', scale='count', scale_hue=False)
plt.show()

# per verificare che i violini corrispondono a realtà faccio un group by dei cilindri per ogni origine e conto i valori
print(cars[cars.origin.isin(['japan', 'europe'])].groupby('cylinders')['origin'].value_counts())