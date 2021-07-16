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
        ''' converting recipe to string '''
        border = "+ " + "=" * 30 + "\n"
        title = "+ " + self.name + "\n"

        # string ingredients together
        ingredients = "+ Ingredients\n"
        for i, ingred in enumerate(self.ingredients):
            ingredients += f"+ {i}. {str(ingred)}\n"

        # string instructions together
        instructions = "+ Instructions\n"
        for i, instr in enumerate(self.instructions):
            instructions += f"+ {i}. {instr}\n"

        #  put everything together
        return border + title + border + ingredients + border + instructions + border

    @classmethod
    def from_json(cls, d):
        return cls(**d)

    def to_json(self):
        return {"name": self.name,
                "ingredients": self.ingredients,
                "instructions": self.instructions}
