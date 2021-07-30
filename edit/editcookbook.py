from classes.pantry import Pantry
from classes.recipe import Recipe
from classes.cookbook import Cookbook
from classes.grocer import isisoformat

import datetime
import os


def clear(): os.system("clear")


def display(cookbook):
    clear()
    print("===============================================")
    print(f"RECIPES from {cookbook.name}:")

    for recipe in sorted(cookbook.recipes, key=lambda r: r.last_eaten):
        print(f"{recipe.name:15} {recipe.last_eaten}")

    print("===============================================")
    print()


def prompt():
    print("===============================================")
    print("Commands are below")
    print("name     - edit the name of the cookbook")
    print("remove   - remove a recipe from the cookbook")
    print("add      - add a recipe to the cookbook")
    print("quit     - exit the cookbook editor")
    print("===============================================")
    return input("Enter command: ").strip().lower()


def edit_name(cookbook):
    display(cookbook)
    name = input("Enter cookbook name: ")
    cookbook.name = name


def remove_item(cookbook):

    clear()

    # empty cookbook - quit recipe removal
    if len(cookbook.recipes) == 0:
        return

    print("===============================================")
    for idx, recipe in enumerate(cookbook.recipes):
        print(f"{(idx + 1):>2}. {recipe.name}")
    print("===============================================")

    print("===============================================")
    print("REMOVE commands are below")
    print("<number> - enter number of recipe to remove")
    print("stop     - stop removing recipes from cookbook")
    print("===============================================")

    while True:
        command = input("Enter command: ").strip().lower()
        if command == "stop":
            return
        elif command.isdigit():
            idx = int(command) - 1
            ingredient = cookbook.recipes[idx]
            cookbook.remove(ingredient)

            remove_item(cookbook)
            return


def add_item(cookbook, pantry):

    def display_add(recipe):
        clear()
        print(f"Recipe to add to the {cookbook.name}:\n")
        print(recipe)

    recipe = Recipe("", [], [])

    # ask for name
    display_add(recipe)
    recipe.name = input("Enter recipe name: ").strip()

    # ask for date last eaten
    display_add(recipe)
    while True:
        date_str = input("Enter date last eaten (YYYY-MM-DD): ").strip().lower()
        if isisoformat(date_str):
            break
    recipe.last_eaten = datetime.date.fromisoformat(date_str)

    # ask for pantry and ingredients from there
    display_add(recipe)
    while True:
        display_add(recipe)
        print(pantry)
        name = input("Enter ingredient to add (q to stop): ")
        if name.lower() != "q":
            same_ingredients = [i for i in pantry.ingredients if i.name == name]
            if len(same_ingredients) > 0:
                recipe.ingredients.append(same_ingredients[0])
        else:
            break

    # ask for instructions
    while True:
        display_add(recipe)
        s = input("Enter instruction (q to stop): ").strip()
        if s.lower() != "q":
            recipe.instructions.append(s)
        else:
            break

    cookbook.recipes.append(recipe)


def editcookbook(cookbook, pantry):

    # while loop asking for edit
    # make edit, break if necessary
    while True:
        display(cookbook)

        command = prompt()
        if command == "name":
            edit_name(cookbook)
        elif command == "remove":
            remove_item(cookbook)
        elif command == "add":
            add_item(cookbook, pantry)
        elif command == "quit":
            break

    cookbook.save()


if __name__ == "__main__":
    pantry = Pantry(input("Enter the pantry file: "))
    cookbook = Cookbook(input("Enter the cookbook file: "))
    editcookbook(cookbook, pantry)
