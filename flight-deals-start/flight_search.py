import requests
import data_manager
import time


FLIGHT_ID = "t1xsxmYU2YReK3KAiLSdQ4w86dYHyF9l",
FLIGHT_SECRET = "ESoW8ZVo1Fvh3OYU"
# Print token response


class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.header = {
            "Authorization": f"Bearer {self.token_refresh()}"
        }
        self.flight_Sheet = data_manager.DataManager()


    def flight(self):
        for city in self.city_names:
            self.token_refresh()
            self.response = requests.get(url=f"https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword={city}&max=1",headers=self.header)
            self.iatacode = self.response.json()["data"][0]["iataCode"]
            print(self.response.json())


    def token_refresh(self):
        self.url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        # Request headers and body
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        self.data = {
            "grant_type": "client_credentials",
            "client_id": FLIGHT_ID,  # Replace with env var in real projects
            "client_secret": FLIGHT_SECRET  # Replace with env var in real projects
        }
        response = requests.post(self.url, headers=self.headers, data=self.data)
        access_token = response.json()["access_token"]
        return access_token