import requests
import datetime


USERNAME = "deniii"
TOKEN  =  "siemens123lklk!"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":ID,
    "name":"Weightloss Graph",
    "unit":"kilogram",
    "type":"float",
    "color":"momiji"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.datetime(year=2025,month=5,day=4)

graph_info = {
    "date" : today.strftime('%Y%m%d'),
    "quantity":"86.0",
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
# response = requests.post(url=pixel_endpoint, json=graph_info, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity":"87.1"
}
#
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_pixel_endpoint,headers=headers)
print(response.text)

