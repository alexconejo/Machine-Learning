#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 23:04:19 2021

@author: alex
"""


#Data Wrangling - Cirugía de datos

import pandas as pd

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

#Usuarios donde se hacen más llamadas de noche que de día
data5= data[data["Day Calls"]<data["Night Mins"]]
