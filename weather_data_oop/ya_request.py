# coding: utf-8
import requests
from bs4 import BeautifulSoup as bs
from weather import Weather

if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")


class Weather_ya(Weather):
    @property
    def temp(self):
        self.page = requests.get(self.url).content
        soup = bs(self.page, 'lxml')
        self.current_weather = soup.find('div', {'class': 'current-weather'})
        self.current_weather_temperature = self.current_weather.find('div', {'class': 'current-weather__thermometer current-weather__thermometer_type_now'})
        return self.current_weather_temperature.text








