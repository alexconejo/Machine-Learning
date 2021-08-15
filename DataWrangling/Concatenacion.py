#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:56:55 2021

@author: alex
"""


#Concatenación y apendizar datasets

import pandas as pd

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
