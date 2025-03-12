import requests
import json

weather_api_key = "2f44ab8d94825710392977b37c24d3ac"
city = "Kazan"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Kazan&appid=2f44ab8d94825710392977b37c24d3ac&units=metric"

def get_weather():
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        print(f"Погода в {city}: {weather}")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} гПа")
    else:
        print("Что-то пошло не так")

holiday_api_key = "bec066c5-e1c2-4a19-aa2d-319598febea0"
holiday_url = f"https://holidayapi.com/v1/holidays?key=bec066c5-e1c2-4a19-aa2d-319598febea0&country=CN&year=2024"

def get_holidays():
    response = requests.get(holiday_url)
    if response.status_code == 200:
        data = response.json()
        holidays = data['holidays']
        
        month_holidays = {}
        for holiday in holidays:
            month = holiday['date'][:7] 
            if month not in month_holidays:
                month_holidays[month] = []
            month_holidays[month].append(holiday)
        
        for month, holidays in month_holidays.items():
            print(f"\nПраздники в {month}:")
            for i in range(0, len(holidays), ): 
                holiday_name = holidays[i]['name']
                holiday_date = holidays[i]['date']
                print(f"{holiday_date}: {holiday_name}")
    else:
        print("Не получилось вывести праздники")

get_weather()
get_holidays()