'''
ingredient.py implements the ingredient class
'''


class Ingredient:

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name
