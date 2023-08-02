#Name: David McGlade
#Date: 07/23/2023
import requests

def get_weather_data(location):
   # API key from OpenWeatherMap
   api_key = '64e2fedccff1dcd7bc74afbd05d8ab39'
   
   # Base URL for weather API
   base_url = 'http://api.openweathermap.org/data/2.5/weather'
   
   # Create parameters for API request
   params = {
       'q': location,
       'appid': api_key,
       'units': 'metric'  # Use metric units for temperature
   }
   
   try:
       # Send GET request to OpenWeatherMap API
       response = requests.get(base_url, params=params)
       
       # Check if request was successful
       if response.status_code == 200:
           # Parse JSON data from the response
           data = response.json()
           
           # Extract relevant weather information
           weather_description = data['weather'][0]['description']
           temperature = data['main']['temp']
           humidity = data['main']['humidity']
           wind_speed = data['wind']['speed']
           
           # Print the weather information
           print(f"Weather forecast for {location}:")
           print(f"Description: {weather_description}")
           print(f"Temperature: {temperature} Â°C")
           print(f"Humidity: {humidity}%")
           print(f"Wind Speed: {wind_speed} m/s")
       else:
           print("Error: Unable to retrieve weather data.")
   except requests.exceptions.RequestException as e:
       print(f"Error: {e}")

def main():
   # Prompt the user for location
   location = input("Enter a city or zip code: ")
   
   # Get weather data for the location
   get_weather_data(location)

# Run the main function
if __name__ == '__main__':
   main()
  #I'm just testing this to see if it is working
  