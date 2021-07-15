'''
recipe.py implements the recipe class
'''

from ingredient import Ingredient


class Recipe:

    def __init__(self, id: int, name: str, ingredients: "list[Ingredient]", instructions: "list[str]"):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
