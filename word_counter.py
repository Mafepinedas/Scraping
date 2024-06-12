# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:23:14 2024
Este script contendrá la función para contar cuántas veces aparece una palabra específica en los títulos y resúmenes de los artículos.
@author: Mafe Pineda
"""
def count_word_occurrences(news_data, word):
    # Contar cuántas veces aparece la palabra en los títulos y resúmenes
    occurrences = sum(1 for article in news_data for field in article.values() if word.lower() in field.lower())
    return occurrences

