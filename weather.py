import requests  # Імпорт бібліотеки для виконання HTTP-запитів

# Ваш API ключ для доступу до WeatherAPI
API_KEY = "ваш ключ api"

# Функція для отримання погодних даних для заданого міста
def get_city_weather(city):
    # Формування URL для запиту до WeatherAPI з зазначенням міста і вимкненням індексу якості повітря (aqi)
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    # Виконання GET-запиту до API
    response = requests.get(url)
    # Перевірка успішності запиту (код 200 означає успішний запит)
    if response.status_code == 200:
        # Перетворення JSON відповіді у словник Python
        data = response.json()
        # Повернення даних про погоду
        return data
    else:
        # Повернення None, якщо запит не успішний
        return None

# Функція для отримання текстового опису погоди для заданого міста
def get_weather_text(city):
    # Виклик функції для отримання погодних даних
    weather = get_city_weather(city)
    print(weather)  # Вивід даних погоди для відлагодження

    if weather:  # Якщо погодні дані успішно отримані
        # Формування текстового опису погоди
        weather_text = f'''
Місто :{city}
температура: {weather['current']['temp_c']}°C'''
        # Повернення текстового опису погоди
        return weather_text
    else:  # Якщо погодні дані не отримані
        return "Не вдалося отримати дані про погоду."

# Виклик функції і вивід текстового опису погоди для Києва
print(get_weather_text('Kyiv'))
