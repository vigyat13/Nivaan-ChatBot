import requests

def get_weather():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=YOUR_CITY&appid=22aa163fad24d67d2c4e8df5475b3f1a")
    data = response.json()
    return f"The weather in your city is {data['response'][0]['description']}."