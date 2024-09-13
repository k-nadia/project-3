import json
import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

"""
API Credentials - loaded via hidden file
"""
load_dotenv()
api_key = os.getenv("API_KEY")
"""
OpenWeather API URLS
"""
GEOCODING_BASE_URL = 'http://api.openweathermap.org/geo/1.0/direct?'
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},
# {country code}&limit={limit}&appid={api key}
CURRENT_AND_FORECAST_BASE_URL = (
    'https://api.openweathermap.org/data/3.0/onecall?'
)
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}
# &exclude={part}&appid={api key}
PAST_WEATHER_BASE_URL = 'https://api.openweathermap.org/'
'data/3.0/onecall/timemachine?'
# https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon=
# {lon}&dt={time}&appid={api key}

def initialise_json_file(filename='weather_history.json'):
    """
    Function to initialise the JSON file if it doesn't exist.
    """
    if not os.path.exists(filename):
        try:
            with open(filename, 'w') as f:
                f.write('')
            print(f"{Fore.GREEN}Weather history file initialised.\n")
        except IOError as e:
            print(f"{Fore.RED}Error initialising weather history file: {e}")


def save_to_json(data, filename='weather_history.json'):
    """
    Function to save the weather data (that the user has retrieved
    from the OpenWeather API) to a JSON file
    """
    try:
        with open(filename, 'a') as f:
            json.dump(data, f)
            f.write('\n')
    except IOError as e:
        print(f"{Fore.RED}Error saving data: {e}")


def read_from_json(filename='weather_history.json'):
    try:
        with open(filename, 'r') as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        return []


def clear_json(filename='weather_history.json'):
    try:
        open(filename, 'w').close()
        print(f"{Fore.GREEN}\nWeather data history cleared successfully.")
    except IOError as e:
        print(f"{Fore.RED}Error clearing weather history: {e}")


def view_weather_history():
    history = read_from_json()
    if not history:
        print(f"{Fore.YELLOW}No weather history available.")
        return
    
    print(f"\n{Fore.CYAN}Weather History:")
    for entry in history:
        print(f"\n{Fore.GREEN}Type: {entry['type']}")
        print(f"{Fore.GREEN}City: {entry['city']}")
        if entry['type'] == 'forecast':
            print(f"{Fore.GREEN}Date: {entry['date']}")
        elif entry['type'] == 'current':
            print(f"{Fore.GREEN}Date: Current")
        
        data = entry['data']
        # Log to check data structure
        #print(f"{Fore.YELLOW}Debug: {data}")

        if entry['type'] == 'current':
            if 'current' not in data:
                print(f"{Fore.RED}Error: Missing 'current' key in entry for {entry['city']}.")
                continue
            current = data['current']

            print(f"{Fore.GREEN}Weather: {current.get('weather', [{}])[0].get('main', 'N/A')}")
            print(f"{Fore.GREEN}Temperature: {current.get('temp', 'N/A')}°C")
            print(f"{Fore.GREEN}Humidity: {current.get('humidity', 'N/A')}%")
            print(f"{Fore.GREEN}Wind Speed: {current.get('wind_speed', 'N/A')} m/s")
            print(f"{Fore.GREEN}Rain (last 1h): {current.get('rain', {}).get('1h', 0)} mm")
        elif entry['type'] == 'forecast':
            daily = data['daily'][0]
            print(f"{Fore.GREEN}Weather: {daily['weather'][0]['main']}")
            print(f"{Fore.GREEN}Temperature: Min {daily['temp']['min']}°C, Max {daily['temp']['max']}°C")
            print(f"{Fore.GREEN}Humidity: {daily['humidity']}%")
            print(f"{Fore.GREEN}Wind Speed: {daily['wind_speed']} m/s")
            print(f"{Fore.GREEN}Rain: {daily.get('rain', 0)} mm")
        print(f"{Fore.CYAN}-----------------------------")


def welcome_message():
    print(
        f"{Fore.CYAN + Style.BRIGHT}\n"
        "  W E L C O M E   T O   W E A T H E R W I S E   A P P . . .  \n"
        )
    print(
        f"{Fore.CYAN}*******************************"
        "*****************************"
        )


def input_name():
    while True:
        name = input(f"{Fore.CYAN} Please enter your name: ")
        if name == "" or name == " ":
            print(f"{Fore.MAGENTA} This is not a valid name,"
                  " please try again...\n")
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
            city = requests.get(f'{GEOCODING_BASE_URL}q={input_city}'
                                f'&limit=1&appid={api_key}')
            city.raise_for_status()

            city_geo_data = city.json()

            if not city_geo_data:
                print(f"{Fore.RED}Error: City not found."
                      "Please check the spelling or try a different city.")
                continue

            city_geo_data = city.json()[0]
            city_name = city_geo_data["name"]
            latitude = city_geo_data["lat"]
            longitude = city_geo_data["lon"]
            state = city_geo_data["state"]
            country = city_geo_data["country"]

            print(f"\n{Fore.GREEN}Your location is {city_name},"
                  f" {state}, {country}.")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")

            return {
                'lat': latitude,
                'lon': longitude,
                'name': city_name,
                'state': state,
                'country': country
            }

        except requests.exceptions.RequestException as e:
            print(
                f"{Fore.RED}"
                f"Error: Unable to connect to the OpenWeather API."
                f"Please check your internet connection and API key."
                )
            print(f"Error details: {e}")
            continue


def current_weather(lat, lon, name):
    """
    Function to get the current weather of the city chosen by the user.
    Prints details of main weather, temperature and humidity
    """
    weather_data = requests.get(
        f'{CURRENT_AND_FORECAST_BASE_URL}'
        f'lat={lat}&'
        f'lon={lon}&'
        f'exclude=minutely,hourly&'
        f'units=metric&'
        f'appid={api_key}'
    )
    weather_info = weather_data.json()

    if weather_data.status_code == 200:
        save_to_json({'type': 'current', 'city': name, 'data': weather_info})
        current = weather_info['current']
        daily = weather_info['daily']

        weather = current['weather'][0]['main']
        temp = current['temp']
        humidity = current['humidity']
        feels_like = current['feels_like']
        wind_speed = current['wind_speed']
        daily_summary = daily.get('summary', 'No summary available')
        current_rain = current.get('rain', {}).get('1h', 0)
        daily_rain_chance = daily.get('pop', 0) * 100
        daily_rain_volume = daily.get('rain', 0)

        print(f"\n{Fore.GREEN}Here are the current weather stats for {name}:")
        print(f"\n{Fore.GREEN}Weather: {weather}")
        print(f"{Fore.GREEN}Temperature: {temp}°C")
        print(f"{Fore.GREEN}Humidity: {humidity}%")
        print(f"{Fore.GREEN}Wind Speed: {wind_speed} m/s")

        print(f"\n{Fore.BLUE}Rain Information:")
        print(f"{Fore.BLUE}Current Rain (last 1h): {current_rain} mm")
        print(f"{Fore.BLUE}Chance of Rain Today: {daily_rain_chance:.1f}%")
        print(f"{Fore.BLUE}Expected Rain Volume Today: {daily_rain_volume} mm")

        print(f"\n{Fore.GREEN}Today's Weather Summary: {daily_summary}")
    else:
        print(f"{Fore.RED} Error: Unable to retrieve weather data.")


def weather_alerts(lat, lon, name):
    """
    Function to get the weather alerts for the city chosen
    by the user. Prints details of any active weather alerts
    or a message if there are no alerts.
    """
    weather_data = requests.get(
        f'{CURRENT_AND_FORECAST_BASE_URL}' +
        f'lat={lat}&lon={lon}&exclude=current' +
        f',minutely,hourly,daily&' +
        f'units=metric&appid={api_key}'
    )
    weather_info = weather_data.json()

    if weather_data.status_code == 200:
        if 'alerts' in weather_info:
            print(f"\n{Fore.RED}Weather Alerts for {name}: ")
            for alert in weather_info['alerts']:
                print(f"\n{Fore.RED}Alert: {alert['event']}")
                print(f"{Fore.YELLOW}Sender: "
                      f"{alert.get('sender_name', 'Not specified')}")
                print(f"{Fore.WHITE}Description: ", end="")
                print(alert.get('description', 'No description available'))
        else:
            print(f"{Fore.GREEN}"
                  f"\nGood news! There are no active weather alerts for {name}.")
    else:
        print(f"{Fore.RED}Error: Unable to retrieve weather alert data.")


def forecast_weather(lat, lon, name):
    """
    Function to get the weather forecast for a specific date chosen by the
    user up to 8 days into the future. It retrieves data for the requested
    date and prints it.
    """
    print(f"{Fore.CYAN}Enter a date to view the weather forecast "
          f"up to 8 days from today (DD/MM/YYYY):")

    weather_data = requests.get(
        f'{CURRENT_AND_FORECAST_BASE_URL}'
        f'lat={lat}&'
        f'lon={lon}&'
        f'exclude=current,minutely,hourly,alerts&'
        f'units=metric&'
        f'appid={api_key}'
    )
    weather_info = weather_data.json()

    while True:
        date_input = input("Enter the date: ")

        try:
            forecast_date = datetime.strptime(date_input, '%d/%m/%Y')
            today = datetime.now()
            max_date = datetime.now() + timedelta(days=8)

            if forecast_date < today or forecast_date > max_date:
                print(f"{Fore.RED}Error: Please enter a date within "
                      f"8 days from today and not in the past.")
                continue
            
            days_offset = (forecast_date - today).days

            if weather_data.status_code == 200:
                save_to_json({'type': 'daily', 'city': name, 'data': weather_info})
                daily = weather_info['daily']

                weather = daily['weather'][0]['main']
                temp_min = daily['temp']['min']
                temp_max = daily['temp']['max']
                humidity = daily['humidity']
                wind_speed = daily['wind_speed']
                daily_summary = daily.get('summary', 'No summary available')
                daily_rain_chance = daily.get('pop', 0) * 100
                daily_rain_volume = daily.get('rain', 0)
                
                print(f"\n{Fore.GREEN}Weather forecast for {name} on "
                      f"{forecast_date.strftime('%A, %B %d %Y')}:")
                print(f"\n{Fore.GREEN}Weather: {weather}")
                print(f"{Fore.GREEN}Temperature: Min {temp_min}°C, Max {temp_max}°C")
                print(f"{Fore.GREEN}Humidity: {humidity}%")
                print(f"{Fore.GREEN}Wind Speed: {wind_speed} m/s")

                print(f"\n{Fore.BLUE}Rain Information:")
                print(f"{Fore.BLUE}Chance of Rain: {daily_rain_chance:.1f}%")
                print(f"{Fore.BLUE}Expected Rain Volume: {daily_rain_volume} mm")

                print(f"\n{Fore.GREEN}Forecast Summary: {daily_summary}")
            else:
                print(f"{Fore.RED} Error: Unable to retrieve weather forecast data.")
            break

        except ValueError:
            print(f"{Fore.RED}Invalid date format. Please use DD/MM/YYYY.")


def options_menu():
    while True:
        print(f"\n{Fore.CYAN}Please choose an option: ")
        print("1: View the current weather")
        print("2: View weather alerts")
        print("3: View daily weather forecast")
        print("4: Choose a new location")
        print("5: View weather data history")
        print("6: Clear weather data history")
        print("7: Start over")
        choice = input("Enter your choice (1-7): ")
        
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            return choice
        else:
            print(f"{Fore.RED}Invalid option. Please enter a number between 1 and 7.")


def main():
    welcome_message()
    initialise_json_file()

    while True:
        name = input_name()

        while True:
            city_geo_data = geocode_city()
            if city_geo_data:
                while True:
                    choice = options_menu()
                    actions = {
                        '1': current_weather,
                        '2': weather_alerts,
                        '3': forecast_weather,
                        '4': geocode_city,
                        '5': view_weather_history,
                        '6': clear_json,
                        '7': welcome_message
                    }

                    if choice in actions:
                        if actions[choice] == geocode_city:
                            break
                        elif actions[choice] == welcome_message:
                            print("\nRestarting WeatherWise application...\n")
                            break
                        elif actions[choice] in [view_weather_history, clear_json]:
                            actions[choice]() 
                        else:
                            latitude = city_geo_data["lat"]
                            longitude = city_geo_data["lon"]
                            city_name = city_geo_data["name"]
                            actions[choice](latitude, longitude, city_name)
                    else:
                        print(f"{Fore.RED}Invalid option. Please try again.")
            else:
                print(f"{Fore.RED}Failed to get city data. Please try again.")


main()