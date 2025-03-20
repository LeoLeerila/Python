import requests

jsonquote = requests.get("https://api.chucknorris.io/jokes/random").json()

print(jsonquote["value"])