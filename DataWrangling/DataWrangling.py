#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 23:04:19 2021

@author: alex
"""


#Data Wrangling - Cirugía de datos

import pandas as pd
import numpy as np
import random 

data = pd.read_csv("../datasets/customer-churn-model/Customer Churn Model.txt")
data.head()

# Creamos un subconjunto de datos
account_length = data["Account Length"]
type(account_length) #Al ser una sola columna es de tipo Series

subset = data[["Account Length", "Phone", "Eve Charge", "Day Calls"]]
subset.head()
type(subset)#Al tener varias columnas es de tipo DataFrame

desired_columns = ["Account Length", "Phone", "Eve Charge", "Day Calls"]
subset = data[desired_columns]
subset.head() 

#Vamos a hacer el complementario entre dos listas
desired_colums = ["Account Length", "VMail Message", "Day Calls"]
all_columns_list = data.columns.values.tolist()
sublist = [x for x in all_columns_list if x not in desired_columns] #Complementario
 
#Otra forma puede ser
a = set(desired_columns)
b = set(all_columns_list)
sublist = b-a
sublist = list(sublist)


data[3320:] #Datos desde la fila 3320 hasta el final

# Usuarios con Day Mins > 300
data1 = data[data["Day Mins"]>300]

# Usuarios de Nueva York (State = "NY")
data2 = data[data["State"]=="NY"]

#Usuarios de NY y Minutos en Día > 300
data3 = data[(data["Day Mins"] > 300) & (data["State"]=="NY")]

#Usuarios de NY o Minutos de Dia > 300
data4 = data[(data["Day Mins"]>300) | (data["State"]=="NY")]

#Usuarios que hacen más llamadas de noche que de día
data5= data[data["Day Calls"]<data["Night Calls"]]

#Usuarios que gastan más minutos de noche que de día
data6 = data[data["Day Mins"]<data["Night Mins"]]

# Minutos de día, de noche y longitud de la cuenta de los primeros 50 individuos
# Primer corchete condición sobre columnas, segundo corchete condición sobre filas
subset_first_50 = data[["Day Mins", "Night Mins", "Account Length"]][:50]

# .iloc nos permite poner en un solo corchete nuestro filtrado de filas y columnas por posicion
# .loc nos permite los mismo que iloc pero por etiquetas
data.iloc[:10, 3:6] #Primeras 10 filas, columnas de la 3 a la 6
data.iloc[:,3:6] #Todas las filas, columnas de la 3 a la 6
data.iloc[:10, :] #Primeras 10 filas, todas las columnas
data.iloc[:10, [2,5,7]] #Primeras 10 filas, columnas 2, 5 y 7

data.loc[[1,5,7,8],["Area Code", "VMail Plan", "Day Mins"]]

# Vamos a añadir una nueva columna, en este caso "Total Mins" que indicará la suma entre minutos de día, tarde y noche
data["Total Mins"] = data["Day Mins"] + data["Eve Mins"] + data["Night Mins"]

# Vamos a añadir una nueva columna, en este caso "Total Calls" que indicará la suma entre llamadas de día, tarde y noche
data["Total Calls"] = data["Day Calls"] + data["Eve Calls"] + data["Night Calls"]

# Generación de números aleatorios
np.random.randint(1, 100) #Números aleatorios del 1 al 100

#La forma más clásica de general un número aleatorio es entre 0 y 1 con decimales
np.random.random()

random_number = random.randrange(0, 100, 7) #Número random entre 0 y 100 múltiplos de 7

# Shuffling : desordenar una lista
a = np.arange(100) #Array con una lista de números de 0 a 100
np.random.shuffle(a)


column_list = data.columns.values.tolist()
np.random.choice(column_list) # Nos coge un valor random de la lista de columnas

# Seed: establecer una semilla es importante para mantener los números random en futuras ejecuciones
np.random.seed(2021) #Número random para fijar la semilla
for i in range(5):
    print(np.random.random()) #Los números random siempre serán los mismos en todas las ejecuciones
    
 

