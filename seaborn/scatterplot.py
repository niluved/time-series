import seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset('diamonds')

print(diamonds.head())
print(diamonds.shape)

# preparo il df . metto solo alcuni cut e alcuni colori
diamonds = diamonds[diamonds['cut'].isin(['Premium','Good']) & diamonds['color'].isin(['D','F','J'])]
print(diamonds.shape)

# faccio lo scatterplot
sns.scatterplot(data = diamonds, x = 'carat', y = 'price')
plt.show()

# vediamo parametri aggiuntivi: hue e size
# hue
sns.scatterplot(data = diamonds, x = 'carat', y = 'price', hue= 'cut')      # NB: nella legenda sono presenti tutti i tipi di cut , anche quelli rimossi dal df. per toglierli anche dalla legenda dovrei aggiungere hue_order=['Premium','Good']
plt.show()

# size
sns.scatterplot(data = diamonds, x = 'carat', y = 'price', size='cut')      
plt.show()
