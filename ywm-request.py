import requests
from bs4 import BeautifulSoup as bs

url = 'https://yandex.ru/pogoda/tomsk'

page = requests.get(url).content
soup = bs(page, 'lxml')

current_weather = soup.find('div', {'class': 'current-weather'})
current_weather_temperature = current_weather.find('div', {
    'class': 'current-weather__thermometer current-weather__thermometer_type_now'})
current_weather_description = current_weather.find('span', {'class': 'current-weather__comment'})
print('Сейчас\n\t{}, {}\n'.format(current_weather_temperature.text, current_weather_description.text))

forecast_weather = soup.find('ul', {'class': 'forecast-brief'})

for li in forecast_weather.find_all('li', {'class': 'forecast-brief__item day-anchor i-bem'}):
    date, description, night = li.find_all('div', recursive=False)
    description_details, day = description.find_all('div', recursive=False)

    print('{} ({})'.format(*map(lambda x: x.text, date.find_all('span'))))
    print('\t{} {} / {}\n'.format(description_details.text, day.text, night.text))