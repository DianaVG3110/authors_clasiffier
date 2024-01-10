# authors_clasiffier

Este proyecto proporciona funciones que calculan la probabilidad de que algún texto sea escrito por algún autor en el conjunto de datos de entrenamiento. Los autores que fueron elegidos para dichos datos de entrenamiento fueron Alejandro Sanz, José José, Luis Miguel, Miguel Bosé. Melendi y Love of Lesbian. Además proporciona un análisis de sentiminetos del texto dado y una nube de palabras.
El proyecto consta de tres módulos:
# 1. Módulo classify: 
En primera instancia contiene las funciones necesarias para limpiar el texto que el usuario ingrese, así como los textos utilizados para el entrenamiento del algoritmo; esto es quitar signos de puntuación, pronombres y artículos, extrayendo las raíces de las palabras principales del texto. Por ejemplo, si en los textos aparecen las palabras amigo, amiga, amigos, se utiliza la raíz 'amig' para contarlas.
Función 'contador_palabras': Contiene una función contadora que, una vez limpio el texto, cuenta la cantidad de veces que ocurre la raíz de cada palabra en el texto proporcionado.
Funciones 'probabilidad artista' y 'particion': Contiene dos funciones que nos ayudan a calcular la probabilidad de las palabras en el texto de un autor partícular y en el texto que incluye las canciones de todos los autores.
Función 'classify': Finalmente, la función principal 'classify' se encarga de proporcionarnos información a través de una gráfica, sobre qué tan probable es que un texto sea de cierto autor.

# 2. Módulo sentiment_analysis:
En este módulo se incluyen funciones que nos dicen si el sentimiento de un texto es positivo o negativo.
Función 'english_analysis': Se encarga de analizar un texto en inglés.
Función 'spanish_analysis': Se encarga de analizar un texto en español.
Función 'analysis': Con ayuda de las funciones anteriores, recibe un texto y el idioma de dicho texto para proceder a hacer su análisis.

# 3. Módulo word_cloud:
Este módulo se encarga de generar una nube de palabras del texto ingresado, con la intención de visualizar mejor el hecho de que si una o ciertas palabras está en el texto, existe mayor probabilidad de que sea de cierto autor.
Función 'detect_language': Se encarga de detectar el idioma de un archivo.
Función 'gen_wordcloud': Genera nubes de palabras de un archivo.
Función 'truncate_filname': Trunca el nombre del archivo, para que no tenga la extensión de él.
Función 'is_text_file': Verifica que el archivo dado sea un archivo de texto.
Función 'gen_wordcloud_directory': Itera a través de archivos para generar las nubes de palabras.

# Autores:
García Bernal Axel Iván
Olmedo Alonso Ana Luisa
Ríos Carrillo Luis Horacio
Vera González Diana 
