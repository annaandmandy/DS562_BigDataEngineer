import requests
import json

api_key = ""
weather_url = "http://api.openweathermap.org/data/2.5/weather"
pollution_url = "http://api.openweathermap.org/data/2.5/air_pollution"

# Function to get real-time weather data
def get_weather_data(lat, lon, api_key):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    response = requests.get(weather_url, params=params)
    return response.json()

# Function to get real-time air pollution data
def get_pollution_data(lat, lon, api_key):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    response = requests.get(pollution_url, params=params)
    return response.json()

# Main function
def main():
    lat, lon = 42.3601, -71.0589  # Coordinates for Boston
    weather_data = get_weather_data(lat, lon, api_key)
    pollution_data = get_pollution_data(lat, lon, api_key)

    data = {
        "city": "Boston",
        "latitude": lat,
        "longitude": lon,
        "weather": weather_data,
        "pollution": pollution_data
    }

    print(data)
    
    # Save data to a JSON file
    with open('weather_pollution_data.json', 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()