
from classes.ingredient import Ingredient
from classes.pantry import Pantry

import os

# ask and load pantry with JSON file to change
pantry_file = input("Enter the pantry file: ")
pantry = Pantry(pantry_file)


def clear(): os.system("clear")


def display(pantry):
    clear()
    print(pantry)


def prompt():
    print("===============================================")
    print("Commands are below")
    print("name     - edit the name of the pantry")
    print("remove   - remove an ingredient from the pantry")
    print("add      - add an ingredient to the pantry")
    print("quit     - exit the pantry editor")
    print("===============================================")
    return input("Enter command: ").strip().lower()


def edit_name():
    display(pantry)
    name = input("Enter pantry name: ")
    pantry.name = name


def remove_item():

    clear()

    print("===============================================")
    for idx, ingredient in enumerate(pantry.ingredients):
        print(f"{(idx + 1):>2}. {ingredient}")
    print("===============================================")

    print("===============================================")
    print("REMOVE commands are below")
    print("<number> - enter number of ingredient to remove")
    print("stop     - exit the pantry editor")
    print("===============================================")

    command = input("Enter command: ").strip().lower()
    if command == "stop":
        return
    else:
        idx = int(command) - 1
        ingredient = pantry.ingredients[idx]
        pantry.remove(ingredient)

        remove_item()


def add_item():
    display(pantry)

    print("===============================================")
    print("ADD commands are below")
    print("<name>   - enter the name of ingredient to add ")
    print("stop     - exit the pantry editor")
    print("===============================================")

    command = input("Enter command: ").strip().lower()
    if command == "stop":
        return
    else:
        ingredient = Ingredient(command)
        pantry.add(ingredient)

        add_item()


# while loop asking for edit
# make edit, break if necessary
while True:
    display(pantry)

    command = prompt()
    if command == "name":
        edit_name()
    elif command == "remove":
        remove_item()
    elif command == "add":
        add_item()
    elif command == "quit":
        break
