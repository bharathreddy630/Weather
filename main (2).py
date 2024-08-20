import requests
def w(a, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={a}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        condition = weather['description']
        print(f"Weather in {location.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    else:
        print("Error: Unable to fetch weather data. Please check the location and try again.")
a= "your_openweathermap_api_key_here"
location = input("Enter city or ZIP code: ")
w(a,location)