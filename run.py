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
GEOCODING_BASE_URL = "http://api.openweathermap.org/geo/1.0/direct?" 
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
CURRENT_AND_FORECAST_BASE_URL = "https://api.openweathermap.org/data/3.0/onecall?"
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
PAST_WEATHER_BASE_URL = "https://api.openweathermap.org/data/3.0/onecall/timemachine?"
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
        name = input(f"{Fore.CYAN} Please enter your name:")
        if name == "" or name == " ":
            print(f"{Fore.MAGENTA} This is not a valid name, please try again...\n")
            continue
        else:
            break

input_city = input(f"{Fore.CYAN} Please enter your city:")
print(input_city)

# welcome_message()
# input_name()




# Write your code to expect a terminal of 80 characters wide and 24 rows high
