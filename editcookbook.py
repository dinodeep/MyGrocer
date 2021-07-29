from classes.recipe import Recipe
from classes.cookbook import Cookbook

import os


def clear(): os.system("clear")


def display(cookbook):
    clear()
    print("===============================================")
    print("RECIPES:")

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

    print("===============================================")
    for idx, recipe in enumerate(cookbook.recipes):
        print(f"{(idx + 1):>2}. {recipe.name}")
    print("===============================================")

    print("===============================================")
    print("REMOVE commands are below")
    print("<number> - enter number of recipe to remove")
    print("stop     - stop removing recipes from cookbook")
    print("===============================================")

    command = input("Enter command: ").strip().lower()
    if command == "stop":
        return
    else:
        idx = int(command) - 1
        ingredient = cookbook.recipes[idx]
        cookbook.remove(ingredient)

        remove_item()


def add_item(cookbook):
    pass


def main():
    # ask and load cookbook with JSON file to change
    cookbook_file = input("Enter the cookbook file: ")
    cookbook = Cookbook(cookbook_file)

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
            add_item(cookbook)
        elif command == "quit":
            break

    cookbook.save()


main()
