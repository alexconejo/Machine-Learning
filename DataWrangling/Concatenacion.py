#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:56:55 2021

@author: alex
"""


#Concatenación y apendizar datasets

import pandas as pd
import os

red_wine = pd.read_csv("../datasets/wine/winequality-red.csv", sep =";") #Están separados por ;

red_wine.columns.values #Valores de las columnas
red_wine.shape #Número de columnas y filas

white_wine = pd.read_csv("../datasets/wine/winequality-white.csv", sep =";")
white_wine.shape

'''En python tenemos dos tipos de ejes
    * axis = 0 denota el eje horizontal
    * axis = 1 denota el eje vertical'''

wine_data = pd.concat([red_wine, white_wine], axis = 0) # Primero aparecerán los datos de red_wine y luego los de white_wine
wine_data.shape

# Efecto de scramblear o concatenar datos de esta forma
data1 = wine_data.head(10)
data2 = wine_data[300:310]
data3 = wine_data.tail(10)

wine_scramble = pd.concat([data1, data2, data3], axis = 0) # El orden de los factores afecta al producto
wine_scramble = pd.concat([data2, data1, data3], axis = 0) # Distinto orden

# Datos distribuidos
data = pd.read_csv("../datasets/distributed-data/001.csv") # Sparse Dataset - Le faltan la mayoría de datos

''' Importar el primer fichero
    Hacemos un bucle para ir recorriendo todos y cada uno de los ficheros
      * Importante una consistencia en el nombre de los ficheros 
      * Importamos los ficheros uno a uno
      * Cada uno de ellos debe apendizarse del primer fichero que ya habíamos cargado
    Repetimos el bucle hasta que no queden ficheros'''
    
filepath = "../datasets/distributed-data/"

# Esta solución solo nos sirve con este ejemplo
for i in range (2,333): # Tenemos que distinguir los menores de 10, mayores de 9 y menores que 100 y mayores que 99 
    if i < 10:
        filename = "00" + str(i)
    elif 10 <= i < 100 :
        filename = "0" +str(i)
    else:
        filename = str(i)   
    file = filepath + filename + ".csv"
    temp_data = pd.read_csv(file)
    data = pd.concat([data, temp_data], axis = 0)

# Una solución universal podría ser
list_csv = sorted(os.listdir(filepath)) # Lista ordenada con todos los nombres de los ficheros

concat_csv = pd.read_csv(filepath + list_csv[0])

for i in range(1, len(list_csv)):
    current_csv = pd.read_csv(filepath + list_csv[i])
    concat_csv = pd.concat((concat_csv, current_csv), axis = 0)

# Joins de datasets
filepath = "../datasets/athletes/"
data_main = pd.read_csv(filepath + "Medals.csv")
a = data_main["Athlete"].unique().tolist() #Con unique() nos quitamos los repetidos

data_country = pd.read_csv(filepath + "Athelete_Country_Map.csv")
# data_country = pd.read_csv(filepath + "Athelete_Country_Map.csv", encoding = "ISO-8859-1") 

data_country[data_country["Athlete"] == "Aleksandar Ciric"] # Aleksandar juega con dos paises diferentes

data_sports = pd.read_csv(filepath + "Athelete_Sports_Map.csv")
len(data_sports) # Hay algunos deportistas que ha participado en dos deportes diferentes

data_sports[(data_sports["Athlete"] == "Chen Jing") |
            (data_sports["Athlete"] == "Richard Thompson") |
            (data_sports["Athlete"] == "Matt Ryan")]
