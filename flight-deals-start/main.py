#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import data_manager
import flight_search

Sheety = data_manager.DataManager()
Flights = flight_search.FlightSearch()


print(Flights.flight_Sheet.sheety_data)

