# coding: utf-8
import requests
from weather import Weather

if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

class Weather_wg(Weather):
    url = 'http://api.wunderground.com/api/7ba75ca3d7269b7c/geolookup/conditions/q/RU/Tomsk.json'
    f = requests.get(url)
    json_string = f.json()
    temp_c = str(json_string['current_observation']['temp_c'])
    def __init__(self, name, temp_c):
        super().__init__(name, temp_c)


wg_weather = Weather_wg('wunderground.com', Weather_wg.temp_c)









