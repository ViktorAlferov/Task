from wg_request import Weather_wg
from ya_request import Weather_ya
from ww_request import Weather_ww
from ow_request import Weather_ow

city = input('Введите город:')

weather_wg = Weather_wg('http://api.wunderground.com/api/7ba75ca3d7269b7c/geolookup/conditions/q/en/' + city + '.json')
print("{} говорит, что сейчас в {}: {} °C".format(weather_wg.domain, city, weather_wg.temp))

weather_ya = Weather_ya('https://yandex.ru/pogoda/' + city)
print("{} говорит, что сейчас в {}: {}".format(weather_ya.domain, city, weather_ya.temp))

weather_ww = Weather_ww('http://api.worldweatheronline.com/premium/v1/weather.ashx?key=d407b756855246abad340024172704&q=' + city + '&format=json&num_of_days=1')
print("{} говорит, что сейчас в {}: {} °C".format(weather_ww.domain, city, weather_ww.temp))

weather_ow = Weather_ow('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',ru&APPID=3071de01ba9f5a11905a27d2bcb1fb16')
print("{} говорит, что сейчас в {}: {} °C".format(weather_ow.domain, city, weather_ow.temp))

