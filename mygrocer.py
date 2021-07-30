from classes.pantry import Pantry
from classes.cookbook import Cookbook
from classes.grocer import Grocer

import os


def display(pantry, cookbook):
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
    cookbook = Cookbook(pantry_file)
    grocer = Grocer(cookbook)

    # enter infinite loop
    while True:
        display(pantry, cookbook)
        prompt()
        command = input("Enter command: ").strip().lower()

        if command == "create list":
            pass
        elif command == "view pantry":
            pass
        elif command == "interact cookbook":
            pass
        elif command == "edit pantry":
            pass
        elif command == "edit cookbook":
            pass
        elif command == "quit":
            break


main()
