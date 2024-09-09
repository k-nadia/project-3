import requests
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from pprint import pprint

""" 
API Credentials
"""
API_KEY = open('api_key', 'r').read()

"""
OpenWeather API URLS
"""
GEOCODING_BASE_URL = 'http://api.openweathermap.org/geo/1.0/direct?'
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
CURRENT_AND_FORECAST_BASE_URL = 'https://api.openweathermap.org/data/3.0/onecall?'
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
PAST_WEATHER_BASE_URL = 'https://api.openweathermap.org/data/3.0/onecall/timemachine?'
# https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}

""" 
Google Sheets 
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project-3')

sales = SHEET.worksheet('sales')
data = sales.get_all_values()


def welcome_message():
    print(f"{Fore.CYAN}\n W E L C O M E   T O   W E A T H E R W I S E   A P P . . .\n")

def input_name():
    while True:
        name = input(f"{Fore.CYAN} Please enter your name: ")
        if name == "" or name == " ":
            print(f"{Fore.MAGENTA} This is not a valid name, please try again...\n")
            continue
        else:
            break

def geocode_city():
    """
    Prompts the user to enter a city name and retrieves the geographical 
    coordinates (latitude and longitude) of that city using the OpenWeather 
    API's geocoding service.
    """
    while True:
        input_city = input(f"{Fore.CYAN} Please enter your city: ")
        try:
            city = requests.get(f'{GEOCODING_BASE_URL}q={input_city}&limit=1&appid={API_KEY}')
            city.raise_for_status()

            city_geo_data = city.json()

            if not city_geo_data:
                print(f"{Fore.RED}Error: City not found. Please check the spelling or try a different city.")
                continue

            city_geo_data = city.json()[0]
            city_name = city_geo_data["name"]
            latitude = city_geo_data["lat"]
            longitude = city_geo_data["lon"]
            state = city_geo_data["state"]
            country = city_geo_data["country"]

            print(f"\n{Fore.GREEN}Your location is {city_name}, {state}, {country}.")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")

            return latitude, longitude  

        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Error: Unable to connect to the OpenWeather API. Please check your internet connection and API key.")
            print(f"Error details: {e}")
            continue

def current_weather(lat, lon):
    """
    Function to get the current weather of the city chosen by the user.
    Prints details of main weather, temperature and humidity
    """
    weather_data = requests.get(f'{CURRENT_AND_FORECAST_BASE_URL}lat={lat}&lon={lon}&appid={API_KEY}')
    
    if weather_data.status_code == 200:
        weather_info = weather_data.json()
        print(weather_info) 
    else:
        print(f"{Fore.RED} Error: Unable to retrieve weather data.")

def options_menu():
    while True:
        print(f"\n{Fore.CYAN}Please choose an option:")
        print("5: Choose a new location")
        print("6: Start over")
        
        choice = input("Enter your choice (5 or 6): ")
        
        if choice == '5':
            return 'geocode_city'
        elif choice == '6':
            print(f"\n Restarting WeatherWise application...\n")
            return 'input_name'
        else:
            print(f"{Fore.RED}Invalid option. Please enter 5 or 6.")

def main():
    welcome_message()
    while True:
        input_name()
        while True:
            city_geo_data = geocode_city()
            if city_geo_data:
                choice = options_menu()

                if choice == 'geocode_city':
                    continue
                elif choice == 'input_name':
                    break
            else:
                print(f"{Fore.RED}Failed to get city data. Please try again.")


#main()
geocode_city()
current_weather(latitude, longitude)









# Write your code to expect a terminal of 80 characters wide and 24 rows high
