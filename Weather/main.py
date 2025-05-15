#with open("weather_data.csv") as weather:
    #data = weather.readlines()
    #print(data)

import csv

 # with open("weather_data.csv") as data_file:
 #     data = csv.reader(data_file)
 #     temperature = []
 #     for row in data:
 #        if row[1] != "temp":
 #            temperature.append(int(row[1]))
 #    print(temperature)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# # data_to_dict = data.to_dict()
# # print(data_to_dict)
# temp_list = data["temp"].to_list()
#
# print(data["temp"].max())
#
# # Get Data in columns
# print(data.condition)

# Get data in row
# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.temp[0]*9/5+32)

# Create a dataframe from scratch
fur_color = data["Primary Fur Color"].value_counts()
fur_color = fur_color.reset_index()
fur_color.columns = ["Fur Color","Count"]
fur_color.to_csv("squirrel_count.csv")

