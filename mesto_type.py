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

# Convert DATE column to datetime format with coercion for errors
data['DATE'] = pd.to_datetime(data['DATE'], format='%d.%m.%Y %H:%M:%S', errors='coerce')
# Calculate the average date, ignoring NaT values
average_date = data['DATE'].dropna().mean()
# Fill NaT values with the average date
data['DATE'] = data['DATE'].fillna(average_date)

# Function to extract the first number from a string and convert it to float
def extract_first_number(text):
    if isinstance(text, str):
        numbers = re.findall(r'\d+', text)
        return float(numbers[0]) if numbers else np.nan
    return np.nan

# Fill NaN values in AGE with the first number found in the ABOUT column
data['AGE'] = data.apply(
    lambda row: extract_first_number(row['ABOUT']) if pd.isna(row['AGE']) else row['AGE'],
    axis=1
)
# Replace non-numeric with NaN
data['AGE'] = pd.to_numeric(data['AGE'], errors='coerce')
# Handle NaN values
data['AGE'] = data['AGE'].fillna(0)
# Convert the column to integers
data['AGE'] = data['AGE'].astype(int)
# Function to keep only two-digit positive values and set the rest to zero
def filter_two_digit_positive(value):
    if 10 <= value < 100:
        return value
    else:
        return 0
# Apply the function to the 'assists' column
data['AGE'] = data['AGE'].apply(filter_two_digit_positive)
# Split the column at the '—' delimiter and expand into separate columns
split_type = data['TYPE'].str.split('—', expand=True)
# Extract the first part and save it to a new column
data['WHO'] = split_type[0]
data['WHO'] = data['WHO'].astype(str).apply(lambda x: x.rstrip())
data[data['WHO']=='Я «человек с руками»']='Рукастый'
data[data['WHO']=='Я «человек, который хочет научиться»']='Научиться'
data[data['WHO']=='Я «человек с идеями»']='Идея'
data[data['WHO']=='Я «человек с продуктом»']='Продукт'
data[data['WHO']=='Я «человек с деньгами»']='Деньги'
data[data['WHO']=='Я «человек с опытом»']='Опыт'
data[data['WHO']=='Я «человек, который хочет научиться»\nЯ «человек, который хочет научиться»']='Научиться'
data[data['WHO']=='Я «человек, который хочет научиться»\nЯ «человек с идеями»']='Научиться'
data[data['WHO']=='Я «человек, который хочет научиться»\nИщу интересных людей для нетворкинга\nЯ из оффлайна, но хочу в онлайн :)']='Научиться'
data[data['WHO']=='Это определенный опыт для меня  и для будущего выполнения планов.\nЯ «человек с идеями»']='Идея'
data[data['WHO']=='Я «человек, который хочет научиться»\nЯ «человек с руками»']='Научиться'
data[data['WHO']=='Человек с идеей']='Идея'
data.info()
#data.tail(10)
print(data['WHO'].nunique())
print(data['WHO'].unique())
# генерирую облако слов
wordcloud = WordCloud(width = 2000, 
height = 1500, 
random_state=1, 
background_color='black', 
margin=20, 
colormap='Pastel1', 
collocations=False
).generate(''.join(data['WHO']))
# строю диаграмму
plt.figure(figsize=(30, 15))
plt.imshow(wordcloud)
plt.axis("off")
plt.title('Диаграмма "облако слов" данных "WHO"', fontsize=30)
plt.show() ;
