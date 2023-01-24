#Python script that uses the OpenWeatherMap API to retrieve the current weather for a specified location

import requests
import json

# API key for OpenWeatherMap
api_key = "your_api_key_here"

# location for which to retrieve the weather
city = "New York"

# make the API call
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

# parse the JSON data
data = json.loads(response.text)

# extract the relevant data from the JSON
current_temp = data["main"]["temp"]
weather_description = data["weather"][0]["description"]

# print the results
print(f"The current temperature in {city} is {current_temp} degrees.")
print(f"The weather is currently {weather_description}.")
