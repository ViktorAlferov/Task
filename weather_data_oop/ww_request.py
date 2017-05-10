# coding: utf-8
import requests
from weather import Weather
if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

class Weather_ww(Weather):
    @property
    def temp(self):
        self.f = requests.get(self.url)
        self.json_string = self.f.json()
        self.current_condition = self.json_string['data']['current_condition'][0]
        return self.current_condition['temp_C']









