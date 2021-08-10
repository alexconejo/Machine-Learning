#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:04:22 2021

@author: alex
"""

# Agrupación de datos por categoría

import pandas as pd
import numpy as np

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
                'Height': np.std #Promedio
                })
    
double_group.aggregate( # Así vemos
        {
                'Age' : np.mean,
                'Height': lambda h: np.mean(h)/np.std(h)
                })
    
double_group.aggregate([np.sum, np.mean, np.std]) # Así aplicamos a todas las columnas la suma, media y promedio
double_group.aggregate([lambda x: np.mean(x)/ np.std(x)])

# Filtrado de datos
double_group["Age"].filter(lambda x: x.sum() > 2400) # Así va a filtrar elementos donde la suma de su edad sea mayor a 2400
