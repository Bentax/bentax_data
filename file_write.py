import requests
import re

url = 'http://www.lib.ru/POECHIN/lao5.txt'
response = requests.get(url)
input_text = response.text
print(len(input_text))
clean_text = re.sub('<[^<]+?>', '', input_text)
clean_text = re.sub('[^а-яА-Я0-9\s]', '', clean_text)
#clean_text = re.sub('\s+', ' ', clean_text)
print(clean_text)
with open('dao_de_czin.txt','w') as file:
    file.write(clean_text)
