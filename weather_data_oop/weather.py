# module with weathers
import requests
class Weather():
    def __init__(self, name, temp_c):
        """Инициализирует атрибуты temp_c и name."""
        self.temp_c = temp_c
        self.name = name

    def weather_now(self):
        """Погода сейчас."""
        print(self.name + " говорит, что сейчас в Томске: ", self.temp_c, "°C")







