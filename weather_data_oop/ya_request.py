# coding: utf-8
import requests
from bs4 import BeautifulSoup as bs
from weather import Weather

if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

class Weather_ya(Weather):
    url = 'https://yandex.ru/pogoda/tomsk'
    page = requests.get(url).content
    soup = bs(page, 'lxml')
    current_weather = soup.find('div', {'class': 'current-weather'})
    current_weather_temperature = current_weather.find('div', {
        'class': 'current-weather__thermometer current-weather__thermometer_type_now'})
    current_weather_description = current_weather.find('span', {'class': 'current-weather__comment'})
    temp_c = current_weather_temperature.text
    def __init__(self, name, temp_c):
        super().__init__(name, temp_c)

#Экземпляр класса
ya_weather = Weather_ya('yandex.ru', Weather_ya.temp_c)


