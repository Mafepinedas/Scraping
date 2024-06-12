# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:22:31 2024
Este script se encargará de obtener los datos de noticias del sitio web de Xataka.
@author: Mafe Pineda
"""

import requests
from bs4 import BeautifulSoup

def fetch_news():
    # URL del sitio web de Xataka
    url = 'https://www.xataka.com/'
    
    # Realizar la solicitud GET al sitio web
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el contenido HTML de la página web
        html_content = response.content
        
        # Crear un objeto BeautifulSoup para analizar el contenido HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Encontrar todos los títulos y resúmenes de los artículos
        article_titles = soup.find_all('h2', class_='abstract-title')
        article_summaries = soup.find_all('div', class_='abstract-content')
        
        # Crear una lista de diccionarios para almacenar los datos de noticias
        news_data = []
        
        # Iterar sobre los títulos y resúmenes y almacenarlos en la lista de datos de noticias
        for title, summary in zip(article_titles, article_summaries):
            news_data.append({
                'Título': title.text.strip(),
                'Resumen': summary.text.strip()
            })
        
        return news_data
    
    else:
        print('Error al obtener el contenido de la página:', response.status_code)
        return []

import os
import pandas as pd

def save_news_to_csv(news_data):
    # Crear el directorio 'data' si no existe
    os.makedirs('data', exist_ok=True)
    
    # Ruta completa del archivo CSV dentro de la carpeta 'data'
    filepath = os.path.join('data', 'news_data.csv')
    
    # Convertir los datos de noticias a un DataFrame de pandas
    df = pd.DataFrame(news_data)
    
    # Guardar el DataFrame en un archivo CSV
    df.to_csv(filepath, index=False)
