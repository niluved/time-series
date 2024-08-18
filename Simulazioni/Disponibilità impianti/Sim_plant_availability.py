import pandas as pd
import numpy as np

forecast = pd.read_csv('programmi_forecast.csv', sep=';', parse_dates=['mese'], dayfirst=True)
storici = pd.read_csv('programmi_storici.csv', sep=';', parse_dates=['mese'], dayfirst=True)

# calcolo la dev_St e la media storica della disponibilità
dev_st_storica = storici.std()  
media_storica = storici.mean()       
# print(media_storica)
# print(dev_st_storica['plant_a'])

# print(forecast['plant_a'][0])

# numero righe nel df forecast
righe_forecast = forecast.index.stop        

# lista con nomi colonne in forecast
colonne_forecast = list(forecast.columns)
colonne_forecast.remove('mese')         # elimino il nome colonna 'mese' dalla lista per avere solo i nomi degli impianti

'''
# con un loop creo una nuova colonna con valori di disponibilità previsti estratti a caso da una normale con media=valore di forecast e devst = devst storica

temp = []

for i in range(righe_forecast):
    plant_a_sim = np.random.normal(forecast['plant_a'][i],dev_st_storica['plant_a'])
    temp.append(plant_a_sim)

forecast['plant_a_sim'] = temp
print(forecast)

      
'''
# creo un dizionario in cui metto come chiavi i nomi delle colonne con i nuovi valori della simulazione (al momento questi valori sono liste vuote) 
dict_sim = {
    'sim_a': [],
    'sim_b': [],
    'sim_c': []
}

# creo una lista con i nomi delle chiavi
chiavi_dict = list(dict_sim.keys())

# creo un ciclo for in cui uso la funzione zip per iterare in parallelo i nomi delle colonne del df forecast con i nomi delle colonne degli impianti simulati, e poi per ogni mese estraggo un valore casuale dalla normale con media pari al valore di forecast e devst pari alla devst storica dell'impianto
'''
for p,i in zip(colonne_forecast, chiavi_dict):
    temp = []
    for m in range(righe_forecast):
        plant_sim = np.random.normal(forecast[p][m],dev_st_storica[p])
        # plant_sim = f'{p},{i},{m}'
        temp.append(plant_sim)
            
    dict_sim[i] = temp

print(dict_sim)
'''
# devo creare ora nuove sim per ciasun impianto

numero_scenari = 10

for p,i in zip(colonne_forecast, chiavi_dict):
    temp = []
    for j in range(numero_scenari):
        for m in range(righe_forecast):
            plant_sim = np.random.normal(forecast[p][m],dev_st_storica[p])
            # plant_sim = f'{p},{i},{m}'
            temp.append(plant_sim)
                
        dict_sim[i] = temp


# print(dict_sim)

# creo il df contenente tutte le serie simulate per ogni impianto
simulati = pd.DataFrame.from_dict(dict_sim)

# creo una nuova lista dei mesi contenenti la lista dei mesi ripetuta per ogni sim
mesi_sim = list(forecast['mese']) * numero_scenari

# inserisco la nuova colonna con i mesi simulati all'inizio del df
simulati.insert(0, 'mesi_sim', mesi_sim)

print(simulati)
