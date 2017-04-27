# coding: utf-8
import requests
from weather import Weather
if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

# Make an API call, and store the response. Создание вызова API и сохранение ответа.
url = 'http://api.wunderground.com/api/7ba75ca3d7269b7c/geolookup/conditions/q/RU/Tomsk.json'
f = requests.get(url)

# Store API response in a variable. Сохранение ответа API в переменной.
json_string = f.json()

# Создание переменной для объекта ответа.
temp_c = str(json_string['current_observation']['temp_c'])

wg_weather = Weather('wunderground.com', temp_c)



