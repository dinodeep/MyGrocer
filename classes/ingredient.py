'''
ingredient.py implements the ingredient class
'''


class Ingredient:

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        # REQUIRED: instances that are equal should have the same hash value (reverse not necessarily true)
        # good tip: take attributes that are used in equality, put in tuple, and hash that jawn
        return hash((self.name))

    def __str__(self) -> str:
        ''' converting ingredient to string '''
        return self.name

    @classmethod
    def from_json(cls, d):
        return cls(**d)

    def to_json(self):
        return {"name": self.name}
