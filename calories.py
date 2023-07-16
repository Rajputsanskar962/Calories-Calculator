
import requests

headers = {
    "X-RapidAPI-Key": "03b52183f2msh98e480b34bf2ddcp1c21dcjsn0cb504272488",
    "X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com",
}

url = "https://fitness-calculator.p.rapidapi.com/dailycalorie"

def get_user_input(message, data_type=str):
    while True:
        try:
            return data_type(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def get_calories_data():
    age = get_user_input("Enter your age: ", int)
    gender = get_user_input("Enter your gender: ")
    height = get_user_input("Enter height in cms: ", int)
    weight = get_user_input("Enter weight in kg: ", int)
    activitylevel = get_user_input("Enter 1 for sedentary, 2 for lightly active, 3 for moderately active, or 4 for highly active: ", int)

    activitylevel = "level_" + str(activitylevel)
    querystring = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "activitylevel": activitylevel,
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an error if the response is not successful
        return response.json()
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def display_weight_goals(calories_data):
    if not calories_data:
        return

    goals = calories_data["data"]["goals"]
    print("Your maintenance calories are:", goals["maintain weight"], "calories")
    weight_loss_goals = ["Mild weight loss", "Weight loss", "Extreme weight loss"]
    weight_gain_goals = ["Mild weight gain", "Weight gain", "Extreme weight gain"]

    for goal in weight_loss_goals:
        data = goals.get(goal)
        if data:
            print(f"To {data['loss weight']} a week, eat: {data['calory']} calories")

    for goal in weight_gain_goals:
        data = goals.get(goal)
        if data:
            print(f"To {data['gain weight']} a week, eat: {data['calory']} calories")

if __name__ == "__main__":
    calories_data = get_calories_data()
    if calories_data:
        display_weight_goals(calories_data)

