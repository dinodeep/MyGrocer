'''
this file implements functions for generating random
ingredients, recipes, pantries, and cookbooks
'''

from src.classes.ingredient import Ingredient
from src.classes.recipe import Recipe
from src.classes.pantry import Pantry
from src.classes.cookbook import Cookbook

import random
import string


def randstring(len, is_caps=False):
    ''' function for generating random string '''
    letters = string.ascii_uppercase if is_caps else string.ascii_lowercase
    return ''.join(random.choices(letters, k=len))


def randingredient():
    ''' generatrs a random instance of type Ingredient '''
    len = random.randint(4, 10)
    name = randstring(len).capitalize()
    return Ingredient(name)


def randrecipe():
    ''' generates a random isntance of type Recipe '''
    name_len = random.randint(6, 12)
    num_ingredients = random.randint(3, 7)
    num_instructions = random.randint(2, 5)

    year = str(random.randint(2014, 2021))
    month = str(random.randint(1, 12)).zfill(2)
    day = str(random.randint(1, 29)).zfill(2)

    name = randstring(name_len, is_caps=True)
    ingredients = [randingredient() for _ in range(num_ingredients)]
    instructions = [randstring(random.randint(10, 20)) for _ in range(num_instructions)]
    date_str = f"{year}-{month}-{day}"

    return Recipe(name, ingredients, instructions, date_str)


def randpantry(filename, name, num_ingredients):
    ''' generates and saves a random instance of type Pantry '''
    p = Pantry(filename)
    p.name = name

    for _ in range(num_ingredients):
        p.add(randingredient())

    p.save()
    return p


def randcookbook(filename, name, num_recipes):
    ''' generates and saves a random instance of type Cookbook '''
    c = Cookbook(filename)
    c.name = name

    for _ in range(num_recipes):
        c.add(randrecipe())

    c.save()
    return c
