'''
recipe.py implements the recipe class
'''

from classes.ingredient import Ingredient


class Recipe:

    def __init__(self, name: str, ingredients: "list[Ingredient]", instructions: "list[str]"):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self) -> str:
        border = "+ " + "=" * 30 + "\n"
        title = "+ " + self.name + "\n"

        ingredients = "+ Ingredients\n"
        for i, ingred in enumerate(self.ingredients):
            ingredients += f"+ {i}. {str(ingred)}\n"

        instructions = "+ Instructions\n"
        for i, instr in enumerate(self.instructions):
            instructions += f"+ {i}. {instr}\n"

        return border + title + border + ingredients + border + instructions + border
