from datetime import datetime
import requests
from bs4 import BeautifulSoup
#from random import randint

#test = randint(-4000, 8500)  # debug code for testing

url = "http://192.168.1.225"  # ESP32 websever

response = requests.get(url)  # get htlm from the url
content = response.content  # store the html in content

soup = BeautifulSoup(content, 'html.parser')  # parse the html

body_content = soup.body  # store the body in body_content

# setting up starting vallues
temperature = 0
temp_prev = 0

# getting data from html into variables
for index, element in enumerate(body_content.find_all('p')):
    if index == 0:  # temperatture
        try:
            temperature = int(float(element.text)*100)
            temp_prev = temperature
        except Exception as e:
            print(f'{datetime.now()} {e}')
            if temp_prev != 0:
                temperature = temp_prev
            else:
                temperature = 0
    elif index == 1:  # humidity
        humidity = element.text
    elif index == 2:  # pressure
        pressure = element.text
    elif index == 3:  # altitude (very inacurate)
        altitude = element.text
