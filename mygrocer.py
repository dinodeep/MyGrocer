from classes.pantry import Pantry
from classes.cookbook import Cookbook
from classes.grocer import Grocer

from edit.editpantry import editpantry
from edit.editcookbook import editcookbook

import os


def display(cookbook, pantry):
    os.system("clear")
    print("========================================================")
    print("MyGrocer")
    print(f"  Pantry:   {pantry.name}")
    print(f"  Cookbook: {cookbook.name}")
    print("========================================================")
    print()


def prompt():
    print("========================================================")
    print("MyGrocer Command Options:")
    print("create list       - for creating a grocery list and plan")
    print("view pantry       - for viewing the pantry")
    print("interact cookbook - for interacting with the cookbook")
    print("edit pantry       - for modifying the pantry")
    print("edit cookbook     - for modifying the cookbook")
    print("quit              - for quiting MyGrocer")
    print("========================================================")


def main():
    # ask for pantry and cookbook files
    pantry_file = input("Enter pantry JSON file: ")
    cookbook_file = input("Enter cookbook JSON file: ")

    pantry = Pantry(pantry_file)
    cookbook = Cookbook(cookbook_file)
    grocer = Grocer(cookbook)

    # enter infinite loop
    while True:
        display(cookbook, pantry)
        prompt()
        command = input("Enter command: ").strip().lower()

        if command == "create list":
            recipes_file = input("Enter text file to store recipes: ")
            grocery_list_file = input("Enter text file to store grocery list: ")
            grocer.plan(recipes_file, grocery_list_file)
        elif command == "view pantry":
            os.system("clear")
            print(pantry)
            print()
            input("Press enter to stop viewing")
        elif command == "interact cookbook":
            os.system("clear")
            cookbook.interact()
        elif command == "edit pantry":
            editpantry(pantry)
        elif command == "edit cookbook":
            editcookbook(cookbook, pantry)
        elif command == "quit":
            break


if __name__ == "__main__":
    main()
