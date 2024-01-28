import requests
from dotenv import load_dotenv
import os  # we need to call the api from the .env
from pprint import pprint # for beauty when printing json from the api

#it is gonna load in those environments variables, so we can retrieve them
load_dotenv()  #This line initializes the process of loading environment variables from the .env filen, and allows to use os.getenv

def get_current_weather():
    print('\n***Get Current Wather Conditions***\n')

    city = input("\nPlease enter a city name: \n")


    #we modify the url , and it kinda different from the documentation 
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)
    #json is the way data is sent  back and forth for many many applications
    weather_data = requests.get(request_url).json()
    pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp in Celsius  {weather_data["main"]["temp"]}')
    print(f'\nFeels like  {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')



if __name__ == "__main__":
    get_current_weather()