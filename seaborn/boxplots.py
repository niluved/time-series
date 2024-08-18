import seaborn as sns
import matplotlib.pyplot as plt

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

# vedo le statistiche di base della colonna 'mpg'
print(cars['cylinders'].describe())

# faccio un boxplot della colonna mpg
# sns.boxplot(cars['mpg'])
# plt.show()

# faccio un boxplot delle colonne origin e mpg
sns.boxplot(data = cars, x = 'origin', y = 'mpg')
plt.show()

# faccio un boxplot delle colonne origin e mpg , dividendole per la categoria (hue) della colonna 'cylinders'
sns.boxplot(data = cars, x = 'origin', y = 'mpg', hue = 'cylinders')
plt.show()

# creo una nuova colonna (boolean) che ha true per i modelli nuovi e false per quelli vecchi
cars['newer_model'] = cars['model_year'] > 76
sns.boxplot(data = cars, x = 'origin', y = 'mpg', hue = 'newer_model')  # faccio il boxplot con la nuova colonna come hue
plt.show()

# posso impostare un colore (unico) diverso dagli standard
sns.boxplot(data = cars, x = 'origin', y = 'mpg', hue = 'newer_model', color='green')  
plt.show()