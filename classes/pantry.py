'''
pantry.py implements the pantry class that allows for device storage of a list of ingredients
'''

from classes.ingredient import Ingredient

import json
import os


class Pantry:

    def __init__(self, file: str):
        self.file = file

        # load pantry from file (create file and init pantry if file does not exists)
        if os.path.exists(file):
            self.load()
        else:
            with open(file, "w") as f:
                json.dump([], f, indent=4)
            self.name = ""
            self.ingredients = []

    def __str__(self) -> str:
        ''' pretty print pantry '''

        border = "=" * 30
        title = "| " + "PANTRY: " + self.name + "\n"

        ingredients_str = "| INGREDIENTS\n"
        for ingredient in self.ingredients:
            ingredients_str += f"| - {str(ingredient)}\n"

        return border + title + border + ingredients_str + border

    def load(self):
        ''' sets pantry ingredients to that from file '''

        # data from a file must be a list of ingredients converted to dicts
        with open(self.file, "r") as f:
            data = json.load(f)
        self.name = data["name"]
        self.ingredients = [Ingredient.from_json(ingredient) for ingredient in data["ingredients"]]

    def save(self):
        ''' saves pantry ingredients to its file '''

        data = {"name": self.name,
                "ingredients": [ingredient.to_json() for ingredient in self.ingredients]}
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
