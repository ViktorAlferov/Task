# coding: utf-8
import requests
from bs4 import BeautifulSoup as bs
from weather import Weather

if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

# Make an html call, and store the response. Создание вызова html и сохранение ответа.
url = 'https://yandex.ru/pogoda/tomsk'
page = requests.get(url).content

# Store html response in a variable. Сохранение ответа html в переменной.
soup = bs(page, 'lxml')
current_weather = soup.find('div', {'class': 'current-weather'})
current_weather_temperature = current_weather.find('div', {
    'class': 'current-weather__thermometer current-weather__thermometer_type_now'})
current_weather_description = current_weather.find('span', {'class': 'current-weather__comment'})
temp_c = current_weather_temperature.text

#Экземпляр класса
ya_weather = Weather('yandex.ru', temp_c)


