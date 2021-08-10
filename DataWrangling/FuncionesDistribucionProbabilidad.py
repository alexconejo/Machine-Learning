#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 01:18:39 2021

@author: alex
"""

# Funciones de distribución de probabilidades

import pandas as pd
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


# La simulación de Monte Carlo
''' Generamos dos números aleatorios uniformes x e y entre 0 y 1 en total 1000 veces

   Calcularemos x² + y²
       Si el valor es inferior a 1 -> estamos dentro del círculo
       Si es valor es superior a 1 -> estamos fuera del círculo
       
    Calculamos el número total de veces que están dentro del círuclo y lo dividimos entre el número total
    de intentos para obtener una aproximación de la probabilidad de caer dentro del círculo.
    
    Usamos dicha probabilidad para aproximar el valor de pi.
    
    Repetimos el experimento un número suficiente de veces (100 p.ej), para obtener diferentes aproximaciones de pi.
    Calculamos el promedio de los 100 experimentos anteriores para dar un valor final de pi.'''

def pi_montecarlo (n, n_exp):
    pi_avg = 0
    pi_value_list = []
    
    for i in range (n_exp):
        value = 0
        x = np.random.uniform(0,1,n).tolist()
        y = np.random.uniform(0,1,n).tolist()
        for j in range (n):
            z = x[j] * x[j] + y[j] * y[j]
            if z <= 1:
                value += 1 #Hemos caido dentro del círculo
        float_value = float(value)
        pi_value = float_value * 4 / n # Probabilidad pi/4 dividido entre el número de veces que lo hemos hecho
        pi_value_list.append(pi_value)
        pi_avg += pi_value
    
    pi = pi_avg / n_exp #Promedio de 100 valores
    print(pi)
    fig = plt.plot(pi_value_list)
    plt.show()
    return (pi, fig)

pi_montecarlo(10000, 200) # Simulación de Montecarlo con 10000 puntos dentro o fuera del círculo y 200 experimentos
    
# Generación de Dummy Data Sets 
n  = 10000
data5 = pd.DataFrame(     # Creación de DataFrame con 3 variables de n filas de cada columna
        {
                'A' : np.random.randn(n),             # Distribución normal estándar
                'B' : 1.5 + 2.5 * np.random.randn(n), # Distribución normal con nota media de 1.5 y desviación de 2.5
                'C' : np.random.uniform(5, 32, n)     # Distribución uniforme entre 5 y 32
        }
)
   
data5.describe()   
plt.hist(data5["C"]) 
plt.show()

data6 = pd.read_csv("../datasets/customer-churn-model/Customer Churn Model.txt")
column_names = data6.columns.values.tolist()
n_columns = len(column_names)
new_data = pd.DataFrame(
        {
                'Column Name' : column_names,
                'A' : np.random.randn(n_columns),
                'B' : np.random.uniform(0,1,n_columns)               
        }, index = range (42,42+n_columns) # Así el índice va desde 42 hasta 62
)
