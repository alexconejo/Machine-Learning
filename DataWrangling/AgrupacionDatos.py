#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:04:22 2021

@author: alex
"""

# Agrupación de datos por categoría

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sklearn

gender = ["Male", "Female"]
income = ["Poor", "Middle Class", "Rich"]

n = 500 # filas
gender_data = []
income_data = []

for i in range(0,n):
    gender_data.append(np.random.choice(gender)) #Cogemos un valor aleatorio de la lista gender
    income_data.append(np.random.choice(income)) #Cogemos un valor aleatorio de la lista income
    
gender_data[:10]

# Z = (X -mu) / sd -> N(0,1)
height = 160 + 30 * np.random.randn(n)
weight = 65 + 25 * np.random.randn(n)
age = 30 + 12 * np.random.randn(n)
income = 18000 + 3500 * np.random.randn(n)

data = pd.DataFrame(
        {
                'Gender' : gender_data,
                'Economic Status' : income_data,
                'Height' : height,
                'Weight' : weight,
                'Age' : age,
                'Income': income
                }
        )

# Agrupación de datos
grouped_gender = data.groupby("Gender") # Creamos objeto con nombre y grupo como atributos, 
grouped_gender.groups

'''for names,groups in grouped_gender:
    print(names)
    print(groups)'''
    
grouped_gender.get_group("Female") # Podemos acceder al grupo y al nombre a través de los getter

# Agrupación de más categorías
double_group = data.groupby(["Gender", "Economic Status"])
len(double_group) # 6 grupos - Gender groups * Economic Status groups

'''for names,groups in double_group: # Todas las combinaciones posibles
    print(names)
    print(groups)'''
    
# Operaciones sobre datos agrupados
double_group.sum()  # Sumamos los datos de las distintos combinaciones
double_group.mean() # Media de los datos de las distintos combinaciones
double_group.size() # Cantidad de elementos de las distintas combinaciones  
double_group.describe()

grouped_income = double_group["Income"]
grouped_income.sum()
grouped_income.describe()

double_group.aggregate(
        {
                'Income' : np.sum,
                'Age' : np.mean,
                'Height': np.std #Desviación típica
                })
    
double_group.aggregate( # Así vemos
        {
                'Age' : np.mean,
                'Height': lambda h: np.mean(h)/np.std(h)
                })
    
double_group.aggregate([np.sum, np.mean, np.std]) # Así aplicamos a todas las columnas la suma, media y la desviación típica
double_group.aggregate([lambda x: np.mean(x)/ np.std(x)])

# Filtrado de datos
double_group["Age"].filter(lambda x: x.sum() > 2400) # Así va a filtrar elementos de los grupos cuya suma de edades supera los 2400

#Transformación de variables
zscore = lambda x: (x - np.mean(x))/np.std(x) #Función de la distribución normal 
z_group = double_group.transform(zscore) #Se puede hacer tanto a un dataFrame ordenado o desordenado como a una columna
'''plt.hist(z_group["Age"])
plt.show()'''

fill_na_mean = lambda x: x.fillna(np.mean(x)) # Así rellenamos con la media los huecos sin valor
double_group.transform(fill_na_mean)

#Operaciones diversas muy útiles
double_group.head(1) #Primera fila de cada una de las colecciones de datos
double_group.tail(1) #Última fila de cada una de las colecciones de datos
double_group.nth(32) #Elemento trigesimo segundo de cada una de las filas. Asegurarse antes de que existe

data_sorted = data.sort_values(["Age", "Income"])
age_grouped = data_sorted.groupby("Gender")
age_grouped.head(1)


# Conjunto de entrenamiento y conjunto de testing
data = pd.read_csv("../datasets/customer-churn-model/Customer Churn Model.txt")

# Dividir utilizando la distribución normal
a = np.random.randn(len(data))
perc_80 = np.percentile(a, 80) #Calculamos el percentil 80
check = (a<perc_80) # Creamos el vector check
check # Así le asignamos un 80% al training y un 20% al testing
plt.hist(check*1) # Al multiplicar el resultado por 1 se cambia el resultado de booleanos a binarios
plt.show()

training = data[check]
testing = data[~check]

# Librería sklearn - Mucho más sencillo
train, test = train_test_split(data, test_size = 0.2) # 20 % usado para testing

# Usando una función de Shuffle
data = sklearn.utils.shuffle(data)
cut_id = int(0.75 * len(data)) # 75 % para entrenar y 25 % para testear 
train_data = data[:cut_id]
test_data = data[cut_id+1:]

