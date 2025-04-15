import requests

def get_weather(city):
    api_key = "your_api_key"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data["current"]

# Example usage:
# weather = get_weather("Kingston")
# print(weather)
