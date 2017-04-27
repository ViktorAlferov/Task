# coding: utf-8
import requests
if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

# Make an API call, and store the response. Создание вызова API и сохранение ответа.
url = 'http://api.wunderground.com/api/7ba75ca3d7269b7c/geolookup/conditions/q/RU/Tomsk.json'
f = requests.get(url)

# Store API response in a variable. Сохранение ответа API в переменной.
json_string = f.json()

# Создание переменной для объекта ответа.
temp_c = json_string['current_observation']['temp_c']

def weather_wg():
    print('wunderground.com говорит, что:')
    print("Сейчас в Томске: {} °C".format(temp_c))
f.close()


