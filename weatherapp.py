import requests

running = True
while running:
    
    city = input("Enter a city: ")
    city = city.strip()

    location_url = "https://geocoding-api.open-meteo.com/v1/search"

    location_parameters = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    location_response = requests.get(
        location_url,
        params=location_parameters
    )

    location_data = location_response.json()

    location = location_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m",
        "timezone": "auto"
    }

    weather_response = requests.get(
        weather_url,
        params=weather_parameters
    )

    weather_data = weather_response.json()

    current = weather_data["current"]

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]

    print()
    print("Weather in", location["name"])
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    
    answer=input("Want to check another city? (y/n):  ").strip().lower()
    
    if answer == "n":
        running = False
      
