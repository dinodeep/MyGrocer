'''
recipe.py implements the recipe class
'''

from classes.ingredient import Ingredient
import datetime


class Recipe:

    def __init__(self, name: str, ingredients: "list[Ingredient]", instructions: "list[str]", date: str = ""):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

        try:
            self.last_eaten = datetime.date.fromisoformat(date)
        except:
            if date != "":
                print("Date provided not in ISO format")
            self.last_eaten = datetime.date.today()

    def __eq__(self, other: object) -> bool:
        return self.name == other.name and self.ingredients == other.ingredients

    def __hash__(self) -> int:
        return hash((self.name, tuple(self.ingredients)))

    def __str__(self) -> str:
        ''' converting recipe to string '''

        border = "+ " + "=" * 30 + "\n"
        title = "+ RECIPE: " + self.name + "\n"
        subtitle = "+ Last eaten " + self.last_eaten.isoformat() + "\n"

        # string ingredients together
        ingredients = "+ INGREDIENTS\n"
        for ingredient in self.ingredients:
            ingredients += f"+ - {str(ingredient)}\n"

        # string instructions together
        instructions = "+ INSTRUCTIONS\n"
        for i, instr in enumerate(self.instructions):
            instructions += f"+ {i}. {instr}\n"

        #  put everything together
        return border + title + subtitle + border + ingredients + border + instructions + border

    @classmethod
    def from_json(cls, d):
        name = d["name"]
        ingredients = [Ingredient.from_json(i) for i in d["ingredients"]]
        instructions = d["instructions"]
        last_eaten = d["last_eaten"]
        return cls(name, ingredients, instructions, last_eaten)

    def to_json(self):
        return {"name": self.name,
                "ingredients": [i.to_json() for i in self.ingredients],
                "instructions": self.instructions,
                "last_eaten": self.last_eaten.isoformat()}
