# -*- coding: utf-8 -*-
"""classify.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_gn7C1M3plhpvdMJY2nEBohmpR2xWyLl
"""

# Cargamos bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk # Para procesamiento de texto
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt') # Remueve signos de puntuación
nltk.download('stopwords') # Remueve articulos

ae_1= "AlejandroSanz.txt"
ae_2= "Love of lesbian.txt"
ae_3= "jose_jose.txt"
ae_4= "luis_miguel.txt"
ae_5= "melendi.txt"
ae_6= "miguel_bose.txt"
autores_español = [ae_1, ae_2, ae_3, ae_4, ae_5, ae_6]

def contador_palabras(cancion):
    """ Esta funcion toma como argumento un archivo de texto que contenga una canción en español, y regresa
    una serie con las raices de las palabras de la cancion y el numero de veces que aparece """
    cancion_cargada = open(cancion)
    lista_cancion = [verso for verso in cancion_cargada]
    formato_adecuado = '\n'.join(lista_cancion)
    palabras_cancion = word_tokenize(formato_adecuado.lower())
    raiz = SnowballStemmer('spanish')
    palabras_filtradas = [raiz.stem(palabra) for palabra in palabras_cancion if palabra not in set(stopwords.words('spanish')) and palabra.isalpha() == True]
    cantidad_palabra = pd.Series(palabras_filtradas).value_counts()
    return cantidad_palabra

def probabilidad_artista(artista):
    """ Esta funcion toma como argumento un archivo de texto con las canciones de un artista en particular,
    y regresa una serie con la probabilidad de cada palabra en dicho archivo de texto """
    return contador_palabras(artista)/contador_palabras(artista).sum()

def particion(lista_artistas, artista = 'autores_totales.txt'):
    """ Esta funcion toma como argumento una lista de archivos de texto con canciones de cada autor y resgresa
    una serie con la probabilidad de cada que palabra ocurra en todos los archivos de texto  """
    ae_1= "AlejandroSanz.txt"
    ae_2= "Love of lesbian.txt"
    ae_3= "jose_jose.txt"
    ae_4= "luis_miguel.txt"
    ae_5= "melendi.txt"
    ae_6= "miguel_bose.txt"
    autores = [ae_1, ae_2, ae_3, ae_4, ae_5, ae_6]
    prob_token= pd.DataFrame(contador_palabras(artista)-contador_palabras(artista))
    prob_token['Total']= prob_token
    for autor in autores:
        prob_token[autor] = (contador_palabras(autor)/contador_palabras(autor).sum())
    prob_token.fillna(0, inplace=True)
    prob_token['Total']= prob_token[ae_1] + prob_token[ae_2]+ prob_token[ae_3]+ prob_token[ae_4]+ prob_token[ae_5]+prob_token[ae_6]
    return prob_token['Total']

def classify(autor, cancion):
    """ Esta funcion toma como argumento un artista en particular y una cancion cualquiera. Utilizando
    las funciones previamennte creadas calculamos la probabilidad final de que la cancion sea de tal
    artista. Regresa una grafica con un punto verde si la probabilidad es alta y rojo si la probabilidad
    es baja, y que contiene un texto indicando el valor de dicha probabilidad """
    probabilidad = 0
    color_punto = ''
    palabras_cancion= contador_palabras(cancion)
    proba_artista = probabilidad_artista(autor)
    probabilidad_palabras = particion(autores_español, artista= 'autores_totales.txt')
    probabilidad_final = proba_artista/probabilidad_palabras[proba_artista.index]

    for palabra in palabras_cancion.index:
        try:
            probabilidad = probabilidad + (1/36)*probabilidad_final[palabra]
        except:
            probabilidad = probabilidad + 0

    if probabilidad >= 0.5:
        color_punto = 'green'
    else:
        color_punto = 'red'

    frase = f'La probabilidad de que tu cancion sea de {autor} es de {probabilidad}'

    #Matplotlib
    figure = plt.figure()
    ax = figure.add_axes([0, 0, 1, 1])
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    X = np.linspace(0, 1, 5)
    Y = [0.5, 0.5, 0.5, 0.5, 0.5]
    ax.plot(0.5, probabilidad, marker = 'o', color = color_punto)
    ax.plot(X, Y, color = 'black')
    ax.text(0.015, 1.1, frase, fontsize = 10, color = 'black')
    plt.show()

    return



