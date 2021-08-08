# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os
import io
import csv 
import urllib3 #Para gestionar los csv que cojamos de Internet
import requests

mainpath = "/home/alex/Escritorio/Machine learning/python-ml-course-master/datasets"
filename = "titanic/titanic3.csv"
fullpath = os.path.join(mainpath, filename )

# Leemos el dataset, usamos .. para irnos a la carpeta anterior 
# y buscamos en la carpeta titanic nuesto dataset.
data = pd.read_csv(fullpath)
data.head()

#Podemos leer archivos txt al igual que los .csv
#data2 = pd.read_csv(mainpath + "/" + "customer-churn-model/Customer Churn Model.txt" )
#data2.columns.values

#Vamos a convertir en lista los valores de Column_Names
data_cols = pd.read_csv(mainpath + "/" + "customer-churn-model/Customer Churn Columns.csv" )
data_col_list = data_cols["Column_Names"].tolist()

#Para cambiar las cabeceras por las letras de Custmoer Churn Columns debemos escribir lo siguiente
data2 = pd.read_csv(mainpath + "/" + "customer-churn-model/Customer Churn Model.txt", header = None, names = data_col_list )
data2.columns.values

#La funcion "open" lee linea por linea como un for el dataset, la r indica solo lectura
#si quisieramos añadir contenido a un archivo es recomendable usar "a" de append en lugar de "w" de write
#esto último sobreescribiría el archivo
data3 = open(mainpath + "/" + "customer-churn-model/Customer Churn Model.txt", "r")

#readline lee la fila a la que apunta el puntero generado por open
#strip elimina espacios en blanco tanto en principio al final de la linea
#split divide esa linea por un caracter o delimitador.
cols = data3.readline().strip().split(",")
n_cols = len(cols)

counter = 0
main_dict = {}
for col in cols:
    main_dict[col] = []
    
for line in data3: 
    values = line.strip().split(",")
    for i in range(len(cols)):
        main_dict[cols[i]].append(values[i])
    counter += 1
        
#print("El data set tiene %d filas y %d columnas"%(counter, n_cols))

#Convertimos el diccionario en un dataFrame.
df3 = pd.DataFrame(main_dict)
#print(df3.head())

#Vamos a escribir la informacion de Customer Churn Model en Tab Customer Churn Model uniendolas con tabulados.
infile = mainpath + "/" + "customer-churn-model/Customer Churn Model.txt"
outfile = mainpath + "/" + "customer-churn-model/Tab Customer Churn Model.txt"

with open(infile, "r") as infile1:
    with open(outfile, "w") as outfile1:
        for line in infile1:
            fields = line.strip().split(",")
            outfile1.write("\t".join(fields))
            #Escribimos un intro
            outfile1.write("\n")
   
#Ahora lo leemos indicando el separador que es el "\t".         
df4 = pd.read_csv(outfile, sep = "\t")

#Vamos a leer datos de una URL
countries_url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
s=requests.get(countries_url).content
countries_data = pd.read_csv(io.StringIO(s.decode("utf-8")))


#Ficheros xls y xlsx
filename2 = "titanic/titanic3.xls"
#Hay que indicar en el read_excel la pestaña como segundo argumento.
titanic2 = pd.read_excel(mainpath + "/" + filename2, "titanic3")

#Creamos un dataframe con los datos que hemos trabajado
titanic2.to_csv(mainpath + "/titanic/titanic_custom.csv")
titanic2.to_excel(mainpath + "/titanic/titanic_custom.xlsx")
titanic2.to_json(mainpath + "/titanic/titanic_custom.json")

#Metodo para descargar archivos de una URL
def DownloadFromURL (url, filename, delim = "\r", sep = ","):
    #Ejercicio - convertir la variable "cr" en un dataframe
    http = urllib3.PoolManager()
    request = http.request('GET', url)
    request.status
    response = request.data
    
    position = 0
    
    #En este caso los distintos elementos del csv estan separados por \r, por lo que lo spliteamos por ello
    clean_response = response.decode('utf-8').split(delim)
    for i in clean_response:
        #Spliteamos por comas ya que en este caso los distintos elementos estan separados por comas
        clean_words = i.split(sep)
        
        #En este caso hay algunos elementos separados por comas que no son elementos distintos 
        #por lo que hay que juntarlos en el misma posición.
        if len(clean_words) > 2:
            new_clean_words = []
            new_clean_words.insert(0, "")
            
            for j in  clean_words:
                if clean_words.index(j) == (len(clean_words)-1):
                    new_clean_words.insert(1, j)
                else:
                    new_word = new_clean_words[0] + j
                    new_word = new_word.replace('"', '')
                    new_clean_words.pop(0)
                    new_clean_words.insert(0, new_word)
            clean_words = new_clean_words
         
        #Cambiamos la posición donde estaban los string por listas con tantas posiciones como columnas hay
        clean_response.pop(position)
        clean_response.insert(position, clean_words)
            
        position += 1
    
    cols = clean_response[0]
    clean_response.pop(0)
    
    #Convertimos nuestra lista en un dataFrame y lo guardamos en nuestro equipo
    df_ex = pd.DataFrame(clean_response, columns = cols)
    
    df_ex.to_csv(filename+".csv")
    df_ex.to_json(filename+".json")
    df_ex.to_excel(filename+".xlsx")
    return

filename = "/countries/countries"
fullpath = os.path.join(mainpath + filename)
DownloadFromURL(countries_url, fullpath )


        
        
                
    






