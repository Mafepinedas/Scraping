# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:23:29 2024
Este script contendrá la función para generar el gráfico de la frecuencia de aparición de la palabra a lo largo del tiempo
@author: Mafe Pineda
"""

import pandas as pd
import matplotlib.pyplot as plt
from word_counter import count_word_occurrences  # Importar la función count_word_occurrences

def plot_word_occurrences_over_time(news_data, word):
    # Obtener las fechas de los artículos (simuladas, ya que no están disponibles en el sitio web)
    dates = pd.date_range(start='2022-01-01', periods=len(news_data))
    
    # Contar la frecuencia de la palabra en los títulos y resúmenes para cada fecha
    occurrences_over_time = [count_word_occurrences(news_data[:i+1], word) for i in range(len(news_data))]
    
    # Crear un gráfico de línea para visualizar la frecuencia de aparición de la palabra a lo largo del tiempo
    plt.plot(dates, occurrences_over_time, marker='o')
    plt.title(f'Frecuencia de "{word}" en Xataka')
    plt.xlabel('Fecha')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
