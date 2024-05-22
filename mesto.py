import re
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mtl
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from datetime import datetime
import datetime as dt
# Load data
data = pd.read_csv('Mesto.csv')
data.columns = ['ID', 'DATE', 'AGE', 'COUNTRY', 'PROJ', 'FROM', 'FROM1', 'ABOUT', 'PROF', 'PROF1', 'VALUE', 'VALUE1', 'L_FOR', 'L_FOR1', 'TYPE', 'ROLE']
# Convert DATE column to datetime format with coercion for errors
data['DATE'] = pd.to_datetime(data['DATE'], format='%d.%m.%Y %H:%M:%S', errors='coerce')
# Calculate the average date, ignoring NaT values
average_date = data['DATE'].dropna().mean()
# Fill NaT values with the average date
data['DATE'] = data['DATE'].fillna(average_date)
# Create YEARMONTH column
data['YEARMONTH'] = data['DATE'].dt.strftime('%Y%m').astype(np.int64)
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
#data[data['COUNTRY']=='Соединенные Штаты Америки'] = 'США'
data.info()
print(data['COUNTRY'].nunique())
print(data['COUNTRY'].unique())
