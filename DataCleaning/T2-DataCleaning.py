#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:14:13 2021

@author: alex
"""

#Resumen de los datos: dimensiones y estructuras
import pandas as pd 
import os

mainpath = "/home/alex/Escritorio/Machine learning/python-ml-course-master/datasets"
filename = "titanic/titanic3.csv"
fullpath = os.path.join(mainpath, filename )
data = pd.read_csv(fullpath)
data.head(10)
data.tail()

#Indicamos que queremos ver todas las filas y columnas de nuestros datasets
pd.options.display.max_rows = None
pd.options.display.max_columns = None

#Vamos a sacar la dimesion del dataset 
data.shape

#Sacamos los valores de las columnas de nuestro df
data.columns.values

#Hacemos un resumen de los estadísticos básicos de las variables numéricas
data.describe()

data.dtypes

#El numero de valores de "age" es menor que el numero de total de muestras que tenemos
#por lo que hay datos que faltan
null_body = pd.isnull(data["body"]).values.ravel() #Con ravel hacemos un único array de datos
total_null_bodies = null_body.sum()
pd.notnull(data["body"]) #Lo contrario a "isnull"

'''Los valores que faltan en un dataset pueden venir por dos razones:
        * Extracción de los datos
        * Recolección de los datos
'''

#Borrado de valores que faltan - borrar filas o columnas
# axis = 0 borrado de filas
# axis = 1 borrado de columnas
data.dropna(axis=0, how="all") #con how=all solo borra si todas las columnas son Na
data2=data.dropna(axis=0, how ="any")

#También se puede sacar el cómputo de los valores faltantes
data3 =data.fillna(0)
data4=data.fillna("Desconocido") 

#Podemos cambiar solo algunos valores
data5=data
data5["body"]=data5["body"].fillna(0)
data5["home.dest"]=data5["home.dest"].fillna("Desconocido")
pd.isnull(data5["age"]).values.ravel().sum()
#mean() es la media 
data5["age"].fillna(data["age"].mean())
data5["age"][1291]

#Así se reemplaza los Na por el siguiente o el anterior valor conocido
data5["age"].fillna(method="ffill") #Siguiente valor conocido
data5["age"].fillna(method="backfill") #Anterior valor conocido

#Variables dummy
dummy_sex = pd.get_dummies(data["sex"], prefix = "sex") #Creacion de dos variables que indicar si el sexo es fem o mas
column_name = data.columns.values.tolist()
data = data.drop(["sex"], axis = 1)
data = pd.concat([data, dummy_sex], axis=1)

#Vamos a crear un método para crear dummies
def createDummies(df, var_name):
    dummy = pd.get_dummies(df[var_name], prefix = var_name)
    df = df.drop(var_name, axis=1)
    df = pd.concat([df, dummy], axis = 1)
    return df

data3 = createDummies(data3, "sex")

