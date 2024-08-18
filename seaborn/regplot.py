import seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset('diamonds')

print(diamonds.shape)

# prendo un campione di righe a caso perchè non mi servono tutte
diamonds = diamonds.sample(n=200)

print(diamonds.head())
print(diamonds.shape)

# faccio la regplot
sns.regplot(data = diamonds, x ='carat', y = 'price')
plt.show()

# faccio una stima con funzione polinomiale aggungendo il parametro order 
sns.regplot(data = diamonds, x ='carat', y = 'price', order=2)      # in questo caso uso una quadratica
plt.show()

# NB: per utilizzare il parametro HUE e avere diverse categorie devo usare "lmplot" invece di "regplot"
sns.lmplot(data = diamonds, x ='carat', y = 'price', hue='cut')
plt.show()

