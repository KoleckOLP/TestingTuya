from datetime import datetime
import requests
from bs4 import BeautifulSoup

url = "http://192.168.1.225"  # ESP32 websever

response = requests.get(url)  # get html from the url
content = response.content  # store the html in content

soup = BeautifulSoup(content, 'html.parser')  # parse the html

body_content = soup.body  # store the body in body_content

# setting up starting vallues
in_temp = 0
in_temp_prev = 0
in_hum = 0
in_hum_prev = 0
in_press = 0
in_press_prev = 0
in_alt = 0
in_alt_prev = 0

out_temp = 0
out_temp_prev = 0
out_hum = 0
out_hum_prev = 0
out_press = 0
out_press_prev = 0
out_alt = 0
out_alt_prev = 0

def get_data(data, data_prev):
    try:
        data = int(float(element.text)*100)
        data_prev = data
    except Exception as e:
        print(f'{datetime.now()} {e}')
        if data_prev != 0:
            data = data_prev
        else:
            data = 0

# getting data from html into variables
for index, element in enumerate(body_content.find_all('p')):
    # Indoor
    if index == 0:  # indoor temperatture
        get_data(in_temp, in_temp_prev)
    elif index == 1:  # indoor humidity
        get_data(in_hum, in_hum_prev)
    elif index == 2:  # indoor pressure
        get_data(in_press, in_press_prev)
    elif index == 3:  # indoor altitude (very inacurate)
        get_data(in_alt, in_alt_prev)
    # Outdoor
    elif index == 4:  # outdoor temperatture
        get_data(out_temp, out_temp_prev)
    elif index == 5:  # outdoor humidity
        get_data(out_hum, out_hum_prev)
    elif index == 6:  # outdoor pressure
        get_data(out_press, out_press_prev)
    elif index == 7:  # outdoor altitude (very inacurate)
        get_data(out_alt, out_alt_prev)
