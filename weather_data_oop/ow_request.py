# coding: utf-8
import requests
from weather import Weather

if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

class Weather_ow(Weather):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Tomsk,ru&APPID=3071de01ba9f5a11905a27d2bcb1fb16'
    f = requests.get(url, params={'units': 'metric', 'lang': 'ru'})
    json_string = f.json()
    temp_c = str(json_string['main']['temp'])
    def __init__(self, name, temp_c):
        super().__init__(name, temp_c)

#Экземпляр класса
ow_weather = Weather_ow('openweathermap.org', Weather_ow.temp_c)

