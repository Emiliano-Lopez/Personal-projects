import datetime 
import requests
import pprint
from datetime import datetime

class Weather():
    def __init__(self):
        self.weather= "weather"
        self.temp = "temp"
        self.feels_like = "feels_like"
        self.state = "state"
        self.city = "city"
        self.country = "country"



    def get_weather(self):

        base_url = "https://api.openweathermap.org/data/2.5/weather?q="
        api_key = "c13bf96dabbdad9c4471886bdaa3ee63"

        url =  base_url + self.city+"&units=Metric&APPID=" +api_key 

        response = requests.get(url).json()
        print(response)

        self.feels_like = str(response["main"]["feels_like"])
        self.temp = str(response["main"]["temp"])
        self.hum = str(response["main"]["humidity"])

        self.city = response["name"]
        self.country = response["sys"]["country"]

        self.weather = response["weather"][0]["main"]
        self.weather_code = response["weather"][0]["id"]
        


