#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 00:00:15 2021

@author: alex
"""


#Plots y visualización de los datos

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data= pd.read_csv("../datasets/customer-churn-model/Customer Churn Model.txt")
data.head()

#savefig("path.(formato)")

#Scatter Plot - Nube de dispersión
data.plot(kind="scatter", x = "Day Mins", y = "Day Charge")
data.plot(kind="scatter", x = "Night Mins", y = "Night Charge")


#Creamos un panel 2x2 donde se comparten ejes y por lo tanto se puede observar a escala la diferencia
#figure, axs = plt.subplots(2,2, sharey= True, sharex= True)


#Buscamos la relacion entre minutos, carga y llamadas en dia y noche
'''data.plot(kind="scatter", x="Day Mins", y = "Day Charge", ax=axs[0][0])
data.plot(kind="scatter", x="Night Mins", y = "Night Charge", ax=axs[0][1])
data.plot(kind="scatter", x="Day Calls", y = "Day Charge", ax=axs[1][0])
data.plot(kind="scatter", x="Night Calls", y = "Night Charge", ax=axs[1][1])'''


#Histogramas de frecuencias: podemos ver como se distribuye una información numérica
#La regla de Sturges sirve para saber cuantas divisiones hay que hacer en el histograma
sturges_rule = 1+int(np.ceil(np.log2(3333)))
plt.hist(data["Day Calls"], bins = sturges_rule)
plt.xlabel("Número de llamadas al día")
plt.ylabel("Frecuencia")
plt.title("Histograma del número de llamadas al día")


#Boxplot, diagrama de caja y bigotes
plt.boxplot(data["Day Calls"])
plt.ylabel("Número de llamadas diarias")
plt.title("Boxplot de las llamadas diarias")

#Valor intercuantílico, los valores por debajo y encima se muestran con esferas
IQR = data["Day Calls"].quantile(0.75)- data["Day Calls"].quantile(0.25)
data["Day Calls"].quantile(0.25)-1.5*IQR
data["Day Calls"].quantile(0.75)+1.5*IQR

