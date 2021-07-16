'''
pantry.py implements the pantry class that allows for device storage of a list of ingredients
'''

import copy
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

    def load():
        ''' sets pantry ingredients to that from file '''
        pass
