import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

# ---- VISUALIZZAZIONE------

print(penguins.head())

# verifico le dimensioni del df (numero righe e numero colonne)
print(penguins.shape)

# stampo i nomi delle colonne
print(penguins.columns)

# elimino le righe con i valori null
penguins.dropna(inplace=True) 

print(penguins.shape)

# creo un grafico con barre verticali (gli arg sono il df e il nome della colonna come asse x)
sns.histplot(data = penguins, x = 'bill_length_mm')
plt.show()

# per fare un grafico a barre orizzontali basta mettere y al posto della x
sns.histplot(data = penguins, y = 'bill_length_mm')
plt.show()

# posso aggiungere un "kernel density estimation" cioè una stima della funzione di densità
sns.histplot(data = penguins, y = 'bill_length_mm', kde = True)
plt.show()

# posso modificare gli intervalli degli istogrammi (bins) impostandone l'ampiezza (binwidth) e/o il bin iniziale e finale (binrange)
sns.histplot(data = penguins, y = 'bill_length_mm', kde = True, binwidth = 5, binrange = (40,70))
plt.show()

# ---- STATISTICHE------

# STAT =
# il parametro di default per l'altra colonna negli histogram è 'count' , come abbiamo visto
# adesso però lo posso cambiare con i seguenti argomenti (stat = ....): 
# 'density' - AREA of histogram sums to one
# 'probability' - HEIGHT of histogram bars to one
# 'frequency'
# 'percent'

sns.histplot(data = penguins, x = 'bill_length_mm', stat = 'frequency')
plt.show()

# HUE =
# posso visualizzare diversi gruppi di dati dividendo gli istogrammi per categoria, dandogli la colonna che riporta le diverse categorie (in questo esempio 'species')
sns.histplot(data = penguins, x = 'bill_length_mm', hue = 'species')
plt.show()

# MULTIPLE = 'layer' (default)
# posso cambiare il parametro 'multiple' per avere colonne impilate (multiple = 'stack') o colonne che sommano a 1 (multiple = 'fill')
sns.histplot(data = penguins, x = 'bill_length_mm', hue = 'species', multiple='stack')
plt.show()

#------BIVARIATE HISTOGRAMS (heat maps) ------
# posso impostare la seconda colonna degli istogrammi mettendo il nome di un'altra colonna del df, in questo modo il grafico diventa di fatto una heat map
sns.histplot(data = penguins, x = 'bill_length_mm', y = 'bill_depth_mm')
plt.show()

# per riavere l'informazione del numero di osservazioni di prima (count) imposto il parametro 'cbar' (color bar) come true
sns.histplot(data = penguins, x = 'bill_length_mm', y = 'bill_depth_mm', cbar = True)
plt.show()

# posso anche utilizzare di nuovo il parametro hue per avere una heatmap divisa per categorie!
sns.histplot(data = penguins, x = 'bill_length_mm', y = 'bill_depth_mm', hue = 'species')
plt.show()