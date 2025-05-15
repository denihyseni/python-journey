import requests
import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("NUTRITION_API_KEY")

nutritionist_api = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "Content-Type":"application/json"

}

data = {
    "query":input("Type what you did for excercise: ")
}

today = datetime.datetime.now()
time_now = datetime.datetime.now().time()


response = requests.post(url=nutritionist_api,json=data,headers=headers)
nutrition_response = response.json()

calories = int(nutrition_response["exercises"][0]["nf_calories"])
exercise = nutrition_response["exercises"][0]["user_input"].title()
length_exercise = nutrition_response["exercises"][0]["duration_min"]

sheet_api = "https://api.sheety.co/a81fa417d75a375b1744adc4c8af592e/denisWorkouts/workouts"

headers = {
    "Content-Type": "application/json"
}

nutrition_data = {
    "workout" : {
        "date":today.strftime("%d/%m/%Y"),
        "time":time_now.strftime("%H:%M:%S"),
        "exercise":exercise,
        "duration":length_exercise,
        "calories":calories,
    }
}
sheet_response = requests.post(url=sheet_api,json=nutrition_data,headers=headers)
print(sheet_response.json())