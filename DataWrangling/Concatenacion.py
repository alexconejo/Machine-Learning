#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:56:55 2021

@author: alex
"""


#Concatenación y apendizar datasets

import pandas as pd
import os
from IPython.display import Image
import numpy as np


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
athletes_unique = data_main["Athlete"].unique().tolist() #Con unique() nos quitamos los repetidos

data_country = pd.read_csv(filepath + "Athelete_Country_Map.csv")
# data_country = pd.read_csv(filepath + "Athelete_Country_Map.csv", encoding = "ISO-8859-1") 

data_country[data_country["Athlete"] == "Aleksandar Ciric"] # Aleksandar juega con dos paises diferentes

data_sports = pd.read_csv(filepath + "Athelete_Sports_Map.csv")
len(data_sports) # Hay algunos deportistas que ha participado en dos deportes diferentes

data_sports[(data_sports["Athlete"] == "Chen Jing") |
            (data_sports["Athlete"] == "Richard Thompson") |
            (data_sports["Athlete"] == "Matt Ryan")]

# Concatenación de varios DataFrames
# Hacemos la combinación del data_main y de data_country 
data_country_duplicate = data_country.drop_duplicates(subset = "Athlete")
len(data_country_duplicate) == len(athletes_unique) #Comprobamos que tenemos las mismas filas y por lo tanto no hay duplicados

data_main_country = pd.merge(left = data_main, right = data_country,
                             left_on = "Athlete", right_on = "Athlete") # Se produce un innerjoin por lo que se duplican las medallas

# Aleksandar está duplicado debido al cambio de nombre en el pais
data_main_country[data_main_country["Athlete"] == "Aleksandar Ciric"]

data_main_country_new = pd.merge(left = data_main, right = data_country_duplicate,
                             left_on = "Athlete", right_on = "Athlete") 

data_main_country_new[data_main_country_new["Athlete"] == "Aleksandar Ciric"]

# Vamos a quitar los duplicados del data_sports
data_sports_duplicate = data_sports.drop_duplicates(subset = "Athlete")

len(data_sports_duplicate) == len(athletes_unique)
data_final = pd.merge(left = data_main_country_new, right = data_sports_duplicate,
                      left_on = "Athlete", right_on = "Athlete")

len(data_final)

# Eliminación de datos
out_athletes = np.random.choice(data_main["Athlete"],size = 6, replace = False)# Atletas que vamos a eliminar
data_country_dlt = data_country_duplicate[(~data_country_duplicate["Athlete"].isin(out_athletes)) &
                                          (data_country_duplicate["Athlete"] != "Michael Phelps")]

data_sports_dlt = data_sports_duplicate[(~data_sports_duplicate["Athlete"].isin(out_athletes)) &
                                          (data_sports_duplicate["Athlete"] != "Michael Phelps")]

data_main_dlt = data_main[(~data_main["Athlete"].isin(out_athletes)) &
                          (data_main["Athlete"] != "Michael Phelps")]

## Inner Join devuelve un df con las filas que tienen valor tanto en el primer como en el segundo df
Image(filename = "../resources/inner-join.png")
# Data_main contiene toda la info
# Data_country_dlt le falta la info de 7 atletas
merged_inner = pd.merge(left = data_main, right = data_country_dlt, how = "inner", left_on = "Athlete", right_on = "Athlete")

## Left Join devuelve un df con las filas que tienen valor en el dataset de la izq sin importar si tienen correspondencia con el de la der
Image(filename = "../resources/left-join.png")
merged_left = pd.merge(left = data_main, right = data_country_dlt, how = "left", left_on = "Athlete", right_on = "Athlete")

## Right Join devuelve un df con las filas que tienen valor en el dataset de la der sin importar si tienen correspondencia con el de la izq
Image(filename = "../resources/right-join.png")
merged_right = pd.merge(left = data_main, right = data_country_dlt, how ="right", left_on = "Athlete", right_on = "Athlete")

## Outter Join devuelve un df con todas las filas de ambos df
Image(filename = "../resources/outer-join.png")
data_country_dlt = data_country_dlt.append(
        {
                'Athlete': "Alex Conejo",
                'Country': "España"
                }, ignore_index =True)

data_country_dlt.tail()

merged_outer = pd.merge(left = data_main, right = data_country_dlt, how = "outer", left_on = "Athlete", right_on = "Athlete")

merged_outer.tail()



