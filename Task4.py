import requests
import ipinfo
from termcolor import colored
from pyfiglet import Figlet
from groq import Groq

class WeatherError(Exception):
    pass

class NoLocationError(WeatherError):
    def __init__(self, message):
        self.message = message

class NoWeatherError(WeatherError):
    def __init__(self, message):
        self.message = message

class NoLanguageError(WeatherError):
    def __init__(self, message):
        self.message = message

class NoUnitError(WeatherError):
    def __init__(self, message):
        self.message = message

def get_location():
    try:
        ip_details = ipinfo.getHandler("eb85c6b947bbc4").getDetails()
        return [ip_details.loc.split(',')[0], ip_details.loc.split(',')[1], ip_details.city, ip_details.country]
    except:
        print(colored("Error: Could not retrieve location information. Please try again.", 'red'))
        raise NoLocationError("Could not retrieve location information")

def get_weather(lat, lng):
    # Use the latitude and longitude to get the weather information from the API
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=6e47dcf7c42dc513f02b5c7a169da1e0&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        return temp, desc, wind_speed, humidity
    else:
        print(colored("Error: Could not retrieve weather information.", 'red'))
        raise NoWeatherError("Could not retrieve weather information")

def print_outputs(temp, desc, wind_speed, humidity, city, country, unit):
    f = Figlet(font='slant')
    ascii_art = f.renderText(text = "Weather")
    print(colored(ascii_art, 'yellow'))
    if unit == 'C':
        temp_str = f"{temp:.1f}°C"
    else:
        temp = temp * 1.8 + 32
        temp_str = f"{temp:.1f}°F"
    
    print(f"You are in {city}, {country}")
    print(f"The temperature is {temp_str}")
    print(f"It is a {desc} day")
    print(f"The wind speed is {wind_speed:.1f} kmph")
    print(f"Humidity is at {humidity}%")
    print(colored(suggest_clothing(temp, wind_speed, humidity, city, country), 'cyan'))
    print(colored("The above suggestion is given by an AI assistant. AI can make mistakes.", 'red'))


def suggest_clothing(temp, wind_speed, humidity, city, country):
    client = Groq(api_key="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")
    completion = client.chat.completions.create(model="llama-3.1-8b-instant", messages=[{"role": "system", "content": "you are a helpful assistant, who informs people about what to wear based on the temperature, humidity, and wind outside."}, {"role": "user", "content": f"The temperature is {temp}, the wind speed is {wind_speed}, the humidity is {humidity}, and I am in {city}, {country}. What should I wear? Answer in one short sentence."}])
    return completion.choices[0].message.content
    
def main():
    lat, lng, city, country = get_location()
    weather_info = get_weather(lat, lng)
    if weather_info:
        temp, desc, wind_speed, humidity = weather_info
        unit = input("Enter the unit for temperature display (C/F): ").upper()
        if unit == 'C' or unit == 'F':
            print_outputs(temp, desc, wind_speed, humidity, city, country, unit)
        else:
            print(colored("Error: Invalid unit. Please enter either 'C' or 'F'.", 'red'))
            raise NoUnitError("Invalid unit")

if __name__ == '__main__':
    main()