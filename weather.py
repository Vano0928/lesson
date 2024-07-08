import requests

API_KEY = "ваш ключ api"

def get_city_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def get_weather_text(city):
    weather = get_city_weather(city)
    print(weather)

    if weather:
        weather_text = f'''
Місто :{city}
температура: {weather['current']['temp_c']}'''

    return weather_text
    
print(get_weather_text('Kyivv'))
