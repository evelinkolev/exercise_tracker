import requests
from datetime import datetime


class ExerciseApp:
    def __init__(self, gender, weight_kg, height_cm, age, app_id, api_key, sheet_endpoint, token):
        self.gender = gender
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.age = age
        self.app_id = app_id
        self.api_key = api_key
        self.sheet_endpoint = sheet_endpoint
        self.token = token

    def track_exercises(self, exercise_text):
        exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

        headers = {
            "x-app-id": self.app_id,
            "x-app-key": self.api_key,
        }

        parameters = {
            "query": exercise_text,
            "gender": self.gender,
            "weight_kg": self.weight_kg,
            "height_cm": self.height_cm,
            "age": self.age
        }

        response = requests.post(exercise_endpoint, json=parameters, headers=headers)
        result = response.json()

        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%X")

        bearer_headers = {
            "Authorization": f"Bearer {self.token}"
        }

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

            sheet_response = requests.post(self.sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

            print(sheet_response.text)
