# coding: utf-8
from weather import Weather
import requests

if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")


class Weather_wg(Weather):
    @property
    def temp(self):
        self.f = requests.get(self.url)
        self.json_string = self.f.json()
        return self.json_string['current_observation']['temp_c']


