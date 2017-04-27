# coding: utf-8
import requests
if __name__ == "__main__":
    print("This is a module with weathers.")
    input("\n\nPress the enter key to exit.")

# Make an API call, and store the response. Создание вызова API и сохранение ответа.
url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=d407b756855246abad340024172704&q=Tomsk&format=json&num_of_days=1'
f = requests.get(url)

# Store API response in a variable. Сохранение ответа API в переменной.
json_string = f.json()


current_condition  = json_string['data']['current_condition'][0]
temp_c = current_condition['temp_C']

def weather_ww():
    print('worldweatheronline.com говорит, что:')
    print("Сейчас в Томске: {} °C".format(temp_c))
f.close()

