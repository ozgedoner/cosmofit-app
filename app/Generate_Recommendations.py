import requests
import json

class Generator:
    def __init__(self, nutrition_input: list, ingredients: list = [], params: dict = {'n_neighbors': 5, 'return_distance': False}):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def set_request(self, nutrition_input: list, ingredients: list, params: dict):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def generate(self):
        url = "http://127.0.0.1:8000/generate"
        payload = {
            "nutrition": self.nutrition_input,
            "ingredients": self.ingredients,
            "params": self.params
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        # Hata ayıklama çıktısı
        print("RESPONSE STATUS:", response.status_code)
        print("RESPONSE JSON:", response.text)

        return response
