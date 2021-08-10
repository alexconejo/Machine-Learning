#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 01:18:39 2021

@author: alex
"""

# Funciones de distribución de probabilidades


import numpy as np
import matplotlib.pyplot as plt

#Distribucion uniforme
a = 1
b = 100
n = 1000000

'''Es necesario tomar mas de 200 muestras para valores de 1 a 100 si queremos ver que sea uniforme 
   1000000 es un buen número de muestras donde ya podemos ver que es uniforme '''
data = np.random.uniform(a,b,n) #Creacion de narray con valores de 1 a 100 con 200 muestras

plt.hist(data) #Histograma que veremos si es uniforme
plt.show()


# Distribución normal - Cuanto más valores random mejor se ve la distribución
data2 = np.random.randn(1000000) #Genera unos valores random con distribución normal estándar

x = range(1,1000001)
plt.plot(x, data2) #No parece una distribución normal pero lo veremos mejor en un histograma
plt.show()

plt.hist(data2) # Ya se asemeja a una campana de Gauss
plt.show()

plt.plot(x, sorted(data2)) # Con los datos ordenados nos sale la CDF
plt.show()

mu = 5.5 # Nota media
sd = 2.5 # Desviación estándar
data3 = mu + sd * np.random.randn(10000) # Z = (X -mu) / sd -> N(0,1)
plt.hist(data3)
plt.show()

data4 = np.random.randn(2,4)
