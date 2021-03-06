'''
cookbook.py implements the Cookbook class which allows for storage, management, 
and interaction with recipes
'''

from classes.recipe import Recipe
from classes.list_viewer import ListViewer

import json
import os


class Cookbook:

    def __init__(self, file):
        self.file = file

        if os.path.exists(file):
            self.load()
        else:
            with open(file, "w") as f:
                json.dump({"name": "", "recipes": []}, f, indent=4)
            self.name = ""
            self.recipes = []

    def __str__(self):
        ''' pp a cookbook '''
        border = "-" * 30 + "\n"
        title = "COOKBOOK: " + self.name + "\n"

        recipes_str = ""
        for recipe in self.recipes:
            recipes_str = border + str(recipe) + border

        return border + border + title + border + recipes_str + border

    def add(self, recipe):
        ''' add recipe to the cookbook '''
        if recipe not in self.recipes:
            self.recipes.append(recipe)

    def remove(self, recipe):
        ''' remove recipe from the cookbook '''
        if recipe in self.recipes:
            self.recipes.remove(recipe)

    def load(self):
        ''' loads a cookbook from the cookbook's file '''
        with open(self.file, "r") as f:
            data = json.load(f)
        self.name = data["name"]
        self.recipes = [Recipe.from_json(r) for r in data["recipes"]]

    def save(self):
        ''' saves current cookbook to its file '''
        unique_recipes = list(set(self.recipes))
        data = {"name": self.name,
                "recipes": [r.to_json() for r in unique_recipes]}
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def interact(self):
        ''' start interaction sim with cookbook '''
        if len(self.recipes) > 0:
            lv = ListViewer(self.recipes, self.name)
            lv.interact()
        else:
            print("No recipes to view")
            input("Press enter to continue")
