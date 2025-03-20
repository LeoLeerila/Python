import geopy.location
import requests
import geopy

Paikkakunta = "Helsinki"
APIKey = "7b8eab2690bd9d85452ab3ce66b3c637"
excludelista = "minutely,hourly,daily,alerts"
lat = ""
lon = ""

APICoords = f"http://api.openweathermap.org/geo/1.0/direct?q={Paikkakunta}&appid={APIKey}"
APICall = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&exclude={excludelista}&appid={APIKey}"

asda = requests.get(APICoords)
print(asda)
