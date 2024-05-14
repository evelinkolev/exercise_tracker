import os
from exercise_app import ExerciseApp


# Set up environment variables or provide values directly
gender = "YOUR_GENDER"
weight_kg = "YOUR_WEIGHT"
height_cm = "YOUR_HEIGHT"
age = "YOUR_AGE"
app_id = os.environ["NT_APP_ID"]
api_key = os.environ["NT_API_KEY"]
sheet_endpoint = os.environ["SHEET_ENDPOINT"]
token = os.environ["TOKEN"]

# Instantiate ExerciseApp
exercise_app = ExerciseApp(gender, weight_kg, height_cm, age, app_id, api_key, sheet_endpoint, token)

# Prompt user for exercise input
exercise_text = input("Tell me which exercises you did: ")

# Track exercises and log to Google Sheet
exercise_app.track_exercises(exercise_text)