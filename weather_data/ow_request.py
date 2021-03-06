# coding: utf-8
import requests

if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

# Make an API call, and store the response. Создание вызова API и сохранение ответа.
url = 'http://api.openweathermap.org/data/2.5/weather?q=Tomsk,ru&APPID=3071de01ba9f5a11905a27d2bcb1fb16'
f = requests.get(url, params={'units': 'metric', 'lang': 'ru'})

# Store API response in a variable. Сохранение ответа API в переменной.
json_string = f.json()

temp_c = json_string['main']['temp']

def weather_ow():
    print('openweathermap.org говорит, что:')
    print("Сейчас в Томске: {} °C".format(temp_c))
f.close()

