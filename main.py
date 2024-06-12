# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:23:50 2024
Este será el script principal que utilizará las funciones de los otros scripts para realizar la ejecución y la interacción con el usuario.
@author: Mafe Pineda
"""

from fetch_news import fetch_news, save_news_to_csv
from word_counter import count_word_occurrences
from plot_generator import plot_word_occurrences_over_time

def main():
    print("Fetching news...")
    news_data = fetch_news()
    print(f"Fetched {len(news_data)} articles")  
    
    
    # Solicitar al usuario la palabra que desea buscar
    word_to_search = input("Ingrese la palabra que desea buscar: ").lower()
    
    # Contar la frecuencia de la palabra en los títulos y resúmenes
    word_occurrences = count_word_occurrences(news_data, word_to_search)
    print(f'La palabra "{word_to_search}" aparece {word_occurrences} veces en los títulos y resúmenes.')
    
    # Guardar los datos en un archivo CSV dentro de la carpeta 'data'
    save_news_to_csv(news_data)
    print("Saved news data to data/news_data.csv")
    # Crear y mostrar un gráfico de la frecuencia de la palabra a lo largo del tiempo
    plot_word_occurrences_over_time(news_data, word_to_search)

    
if __name__ == "__main__":
    main()
