import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 48
HEIGHT_CM = 165
AGE = 22

APP_ID = [YOUR_APP_ID]
API_KEY = [YOUR_API_KEY]

USERNAME_FOR_AUTH = [USERNAME]
PASS_FOR_AUTH = [PASS]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/64035c75cd87df73ae366d18e83ebf84/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

#Saving Data into Google Sheets.
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(USERNAME_FOR_AUTH, PASS_FOR_AUTH))
    print(sheet_response.text)