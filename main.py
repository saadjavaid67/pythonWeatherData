import requests
import os
from datetime import datetime

user_api = 'Your APIkey'
location = input("Enter your city name : ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid city : {}, Please check again".format(location))
else:
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %y | %I:%M:s %p")

    print("++------------------------------------------------------------------------++")
    print("The status of the weather at - {} || {}".format(location.upper(), date_time))
    print("++------------------------------------------------------------------------++")

    print("Current temp is : {:.2f} deg C".format(temp_city))
    print("Current weather description is : ", weather_desc)
    print("Current humidity : ", hmdt ,'%')
    print("Current wind speed : ", wind_spd, 'KMpH')
