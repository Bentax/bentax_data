mport re
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
data = data.dropna(subset=['L_FOR'])
# Function to extract the second word from a string
def get_second_word(s):
    words = s.split()
    if len(words) >= 2:
        return words[1]
    else:
        return ''

# Apply the function to the column
data['L_FOR'] = data['L_FOR'].apply(get_second_word)
#data.head(10)
# генерирую облако слов
wordcloud = WordCloud(width = 2000, 
height = 1500, 
random_state=1, 
background_color='black', 
margin=20, 
colormap='Pastel1', 
collocations=False
).generate(''.join(data['L_FOR']))
# строю диаграмму
plt.figure(figsize=(30, 15))
plt.imshow(wordcloud)
plt.axis("off")
plt.title('Диаграмма "облако слов" данных "что ищет"', fontsize=30)
plt.show() ;
