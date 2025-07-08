import requests

response = requests.get("https://api.genderize.io?name=peter")
gender = response.json()
