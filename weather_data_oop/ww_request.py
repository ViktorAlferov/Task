# coding: utf-8
import requests
from weather import Weather


if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

class Weather_ww(Weather):
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=d407b756855246abad340024172704&q=Tomsk&format=json&num_of_days=1'
    f = requests.get(url)
    json_string = f.json()
    current_condition = json_string['data']['current_condition'][0]
    temp_c = str(current_condition['temp_C'])
    def __init__(self, name, temp_c):
        super().__init__(name, temp_c)

#Экземпляр класса
ww_weather = Weather_ww('worldweatheronline.com', Weather_ww.temp_c)

