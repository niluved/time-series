lista_uno = ['a','b','c']
lista_due = ['a_sim','b_sim','c_sim']
mesi = [1,2,3,4,5]

# se faccio il doppio ciclo for lui itera il primo elemento della prima lista  con tutti gli elementi della seconda lista e con tutti gli elementi della terza prima di ricominciare a contare
print('triplo ciclo for')
for i in lista_uno:   
    for j in lista_due:
        for m in mesi:
            print(i,j,m)

# se voglio invece che gli elementi delle prime due liste siano iterati parallelamente devo usare la zip
print('funzione zip')
for i,j in zip(lista_uno, lista_due):
    for m in mesi:
            print(i,j,m)