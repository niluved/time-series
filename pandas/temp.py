import random

def casuale(x):
    numero = random.random() * x
    return numero

numero = casuale(100) 
print(numero)
