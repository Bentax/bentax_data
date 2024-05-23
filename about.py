import re
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mtl
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.stats import pearsonr
from datetime import datetime
import datetime as dt
# Load data
data = pd.read_csv('Mesto.csv')
data = data.dropna(thresh=6)
#reset index of DataFrame
data = data.reset_index(drop=True)
data.columns = ['ID', 'DATE', 'AGE', 'COUNTRY', 'PROJ', 'FROM', 'FROM1', 'ABOUT', 'PROF', 'PROF1', 'VALUE', 'VALUE1', 'L_FOR', 'L_FOR1', 'TYPE', 'ROLE']
data = data.dropna(subset=['ABOUT'])

# Список предлогов для удаления
prepositions = {'и', 'в', 'на', 'с', 'по', 'у', 'но', 'из', 'все', 'для', 'как','я','что','это','не','лет','а','то'}

# Функция для удаления предлогов из строки
def remove_prepositions(s):
    words = s.split()
    filtered_words = [word for word in words if word.lower() not in prepositions]
    return ' '.join(filtered_words)
data['ABOUT'] = data['ABOUT'].astype(str).apply(remove_prepositions)
# генерирую облако слов
wordcloud = WordCloud(width = 2000, 
height = 1500, 
random_state=1, 
background_color='black', 
margin=20, 
colormap='Pastel1', 
collocations=False
).generate(''.join(data['ABOUT']))
# строю диаграмму
plt.figure(figsize=(30, 15))
plt.imshow(wordcloud)
plt.axis("off")
plt.title('Диаграмма "облако слов" данных "обо мне"', fontsize=30)
plt.show() ;
