# pagina web del codice con qualche informazione in più: https://quantpy.com.au/python-for-finance/simulated-stock-portolio/ 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as pdr

# import data
def get_data(stocks, start, end):
    stockData = pdr.get_data_yahoo(stocks, start, end)
    stockData = stockData['Close']                          # dal df che ottengo in risposta prendo solo la colonna Close
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

stockList = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']
stocks = [stock + '.AX' for stock in stockList]         # list comprehension per aggiungere il '.AX' ad ogni nome di azione per la borsa australiana (yahoo li vuole così)
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

weights = np.random.random(len(meanReturns))            # assegna un peso casuale tra 0 e 1 a ciascuna azione nel portafoglio
weights /= np.sum(weights)                              # la somma dei pesi è impostata pari a 1

# Monte Carlo Method
mc_sims = 400 # number of simulations
T = 100 #timeframe in days

meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns)        # creo una matrice (full) con certe dimensioni (shape) e  riempio con valori in fill_value: in questo caso i ritorni medi
meanM = meanM.T                                                     # faccio la trasposta

portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0)

initialPortfolio = 10000                # valore in dollari del portafoglio iniziale , al quale verranno sommati i ritorni giornalieri casuali durante il loop sottostante

for m in range(0, mc_sims):
    Z = np.random.normal(size=(T, len(weights)))#uncorrelated RV's
    L = np.linalg.cholesky(covMatrix) #Cholesky decomposition to Lower Triangular Matrix
    dailyReturns = meanM + np.inner(L, Z) #Correlated daily returns for individual stocks
    portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*initialPortfolio

plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value ($)')
plt.xlabel('Days')
plt.title('MC simulation of a stock portfolio')
plt.show()