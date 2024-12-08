import requests

query_url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=ef2136e3787f182c09441daecd26b3e1"
response = requests.get(query_url)
print(response.json())