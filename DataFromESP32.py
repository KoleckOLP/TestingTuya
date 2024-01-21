import time
import requests
from bs4 import BeautifulSoup
from random import randint

test = 42

url = "http://192.168.1.225"

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

body_content = soup.body

for index, element in enumerate(body_content.find_all('p')):
    if index == 0:
        temperature = element.text
    elif index == 1:
        humidity = element.text
    elif index == 2:
        pressure = element.text
    elif index == 3:
        altitude = element.text
