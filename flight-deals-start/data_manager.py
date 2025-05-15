import requests
import flight_search


class DataManager():

    def __init__(self):

       self.url = "https://api.sheety.co/a81fa417d75a375b1744adc4c8af592e/copyOfFlightDeals/prices"
       self.response =requests.get(url=self.url)
       self.sheety_data = self.response.json()

    #
    # def add_iata_codes(self):
    #
    #     self.flight_info = flight_search.FlightSearch()
    #     for n in range(len(self.flight_info.iatacode)):
    #         sheety_put = f"https://api.sheety.co/a81fa417d75a375b1744adc4c8af592e/copyOfFlightDeals/prices/{n}"
    #         header = {
    #             "Content-Type": "application/json"
    #         }
    #
    #         data = {
    #             "IATA Code":self.flight_info.iatacode
    #         }
    #
    #
    #         sheets_response = requests.put(url=sheety_put,json=data,headers=header)
    #         print(sheets_response.json())