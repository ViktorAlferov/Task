# coding: utf-8
import requests
from weather import Weather

if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

class Weather_ow(Weather):
    @property
    def temp(self):
        self.f = requests.get(self.url, params={'units': 'metric', 'lang': 'ru'})
        self.json_string = self.f.json()
        return self.json_string['main']['temp']






