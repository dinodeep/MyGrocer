'''
pantry.py implements the pantry class that allows for device storage of a list of ingredients
'''

from classes.ingredient import Ingredient

import json
import os


class Pantry:

    def __init__(self, name: str, file: str):
        self.name = name
        self.file = file

        # load ingredients from file (create file if it does not exists)
        if os.path.exists(file):
            self.ingredients = self.load()
        else:
            self.ingredients = []
            with open(file, "w") as f:
                json.load([], f, indent=4)

    def __str__(self) -> str:
        ''' pretty print pantry '''

        border = "=" * 30
        title = "| " + "PANTRY: " + self.name + "\n"

        ingredients_str = "| INGREDIENTS\n"
        for i, ingredient in enumerate(self.ingredients):
            ingredients_str += f"| - {str(ingredient)}\n"

        return border + title + border + ingredients_str + border

    def load(self):
        ''' sets pantry ingredients to that from file '''

        # data from a file must be a list of ingredients converted to dicts
        with open(self.file, "r") as f:
            ingredients = json.load(f)
        self.ingredients = [Ingredient.from_json(ingredient) for ingredient in ingredients]

    def save(self):
        ''' saves pantry ingredients to its file '''

        data = [ingredient.to_json() for ingredient in self.ingredients]
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
