import pandas

# costruiamo un dataframe
calendario = {
    'Mesi': ['gennaio', 'febbraio', 'marzo', 'aprile'],
    'Giorni': [31,28,31,30]
    
}

df = pandas.DataFrame(calendario)

print(df)  # stampo tutto il dataframe

# costruiamo una serie (cioè un array, che era una lista per python)
dati = [2,4532,32,56,32,876,4,55,90]
serie = pandas.Series(dati)

print (serie)

# leggo da un file csv/json e importo i dati

df = pandas.read_csv('pokemon.csv')
df = pandas.read_json('pokemon.json')


print(df[['Name','Attack']].head(5))   # prendo le prime 5 righe delle colonne name e attack
print(df[['Name','Attack']][10:15])   # prendo dalla riga 10 alla riga 14 delle colonne name e attack

print(df.loc[[0,5]]) # stampo solo la prima riga e la riga 5 (loc è come un cerca verticale che legge i dati a partire dalla prima colonna, quella indice )

'''
# leggo da un file csv/json ma imposto come colonna "indice" la prima colonna , la colonna name (questo mi serve per usare meglio la funzione loc che mi permette di localizzare gli elementi dando come riferimento la colonna indice)
df = pandas.read_csv('pokemon.csv', index_col=1) 
print(df.loc['Bulbasaur'])                         # stampo solo la riga relativa a Bulbasaur
print(df.iloc[0])                               # stampo solo la riga relativa alla prima riga nella colonnna indice (che è la stessa cosa della riga sopra)

print(df.loc['Squirtle', 'Total'])              # prendo il valore delle coordinate individutato tra squirtle e total
print(df.iloc[9,3])                             # stessa cosa di sopra ma con gli indici delle righe e colonne


for index,row in df.iterrows():                 # come iterare le righe del dataframe (iterrows regge due parametri: l'indice della riga e il valore associato)
    print(index, row)                       # stampo sia l'indice della riga che il contenuto della riga intera
    print(row)                          # stampo solo la riga senza l'indice



sorted_df = df.head(10).sort_values('Total')            # ordino i dati per la colonna che voglio (scelgo solo le prime 10 righe del df per brevità)
print(sorted_df)

df['colonna_Aggiunta'] = 'ciao'             # aggiungo in fondo una colonna con il valore ciao su tutte le righe
print(df)

df2 = df[['Name','Attack']]
df2.to_csv('temp.csv')                      # scrivo un sottoinsieme del df in un file csv
'''

print(df[df['Name']=='Bulbasaur'])             # Esempi di filtri

nomi = ['Bulbasaur', 'Charmander', 'Squirtle']          
print(df[df['Name'].isin(nomi)])

print(df[(df['Total'] > 700) & (df['Sp. Atk'] > 20)])        # esempio di AND
print(df[(df['Total'] < 400) | (df['Total'] > 700)])        # esempio di OR
