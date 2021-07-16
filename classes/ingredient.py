'''
ingredient.py implements the ingredient class
'''


class Ingredient:

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        ''' converting ingredient to string '''
        return self.name

    @classmethod
    def from_json(cls, d):
        return cls(**d)

    def to_json(self):
        return {"name": self.name}
