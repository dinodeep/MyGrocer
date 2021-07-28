

'''
parse the arguments
1. text file containing recipes in the text file
2. json file containing pantry for referring to ingredients in recipe file
3. json file for storing the recipes into a cookbook
4. OPTIONAL - the name of the cookbook to store it to
'''

from classes.ingredient import Ingredient
from classes.pantry import Pantry
from classes.recipe import Recipe
from classes.cookbook import Cookbook

import datetime
import re
import sys


def add_recipe(cookbook: Cookbook, recipe_lines: "list[str]", pantry: Pantry):
    # parse name and date strings
    recipe_name = re.sub("RECIPE:", "", recipe_lines[0], re.IGNORECASE).strip()
    date_str = re.sub("DATE:", "", recipe_lines[1], re.IGNORECASE).strip()

    # get list of ingredients in pantry
    ingredients = re.sub("INGREDIENTS:", "", recipe_lines[2], re.IGNORECASE).strip().split(",")
    ingredients = [Ingredient(ing.strip().lower()) for ing in ingredients]
    ingredients = [ing for ing in ingredients if ing in pantry.ingredients]

    # create and store recipe
    recipe = Recipe(recipe_name, ingredients, recipe_lines[3:], date_str)
    cookbook.add(recipe)


# parse the arguments
args = sys.argv
recipes_file = args[1]
pantry_file = args[2]
cookbook_file = args[4]

# create the cookbook
cookbook = Cookbook(cookbook_file)
if len(args) > 4:
    cookbook.name = args[5]

# load the pantry
pantry = Pantry(pantry_file)

# parse the recipes file and store into the cookbook (terminate if ingredient not found)
with open(recipes_file) as f:
    lines = f.readlines()
    lines = [line for line in lines if line.strip() != ""]

    # get start and end lines of recipes
    start_lines = [i for i, line in enumerate(lines) if line.lower().startswith("recipe")]
    start_lines.append(len(lines))
    recipe_segments = [[start_lines[i], start_lines[i + 1]] for i in range(len(start_lines) - 2)]
    for start, end in recipe_segments:
        add_recipe(cookbook, lines[start:end], pantry)

# save cookbook and interact with it
cookbook.save()
cookbook.interact()
