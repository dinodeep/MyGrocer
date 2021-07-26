'''
grocer.py implements the Grocer class
'''

from classes.cookbook import Cookbook

import datetime
import os

day_str = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']


def clear():
    ''' clears the terminal screen '''
    os.system("clear")


def isisoformat(date_str):
    ''' returns True if the date_str is isoformat 'YYYY-MM-DD', False otherwise '''
    # parts[0] = "YYYY", parts[1] = "MM", parts[2] = "DD"
    parts = date_str.split("-")
    return len(parts) == 3 and \
        len(parts[0]) == 4 and parts[0].isnumeric() and \
        len(parts[1]) == 2 and parts[1].isnumeric() and 1 <= int(parts[1]) <= 12 and \
        len(parts[2]) == 2 and parts[2].isnumeric() and 1 <= int(parts[2]) <= 31


def isshortformat(date_str):
    ''' returns True if the date_str is a shorter format 'MM-DD' '''
    parts = date_str.lower().split("-")
    return len(parts) == 2 and \
        len(parts[0]) == 2 and parts[0].isnumeric() and 1 <= int(parts[1]) <= 12 and \
        len(parts[1]) == 2 and parts[1].isnumeric() and 1 <= int(parts[1]) <= 31


def isdayformat(date_str):
    ''' returns True if the date_str is in the day format as Mon, Tue, Wed, Thu, Fri, Sat, Sun, False otherwise '''
    return date_str.lower() in day_str


def convertdate(date_str):
    ''' converts the given date string to the next satisfying date including this date '''
    today = datetime.date.today()

    if isisoformat(date_str):
        return datetime.date.fromisoformat(date_str)

    if isshortformat(date_str):
        date = datetime.date.fromisoformat(f"{today.year}-{date_str}")
        # set to next year if necessary
        if date < today:
            date.year += 1
        return date

    if isdayformat(date_str):
        day_idx = day_str.index(date_str.lower())
        today_idx = today.weekday()
        day_delta = day_idx - today_idx
        day_delta = day_delta if day_delta >= 0 else day_delta + 7
        return today + datetime.timedelta(days=day_delta)

    return None


class Grocer:

    def __init__(self, cookbook: Cookbook):
        self.cookbook = cookbook

    def view(self, plan):
        ''' prints the options that the user has to choose from for planning '''

        clear()

        title = f"Recipes from {self.cookbook.name}"
        border = "=" * len(title)
        sorted_recipes = sorted(self.cookbook.recipes, key=lambda recipe: recipe.last_eaten)

        print(title)
        print(border)
        for i, recipe in enumerate(sorted_recipes):
            print(f"{i + 1:>2}. {recipe.name:12} {recipe.last_eaten.isoformat()}")
        print("\n" * 2)

        print(border)
        print("Current Plan")
        for recipe, date in sorted(plan, key=lambda tup: tup[1]):
            print(f"\t- {recipe.name} ({date.isoformat()})")
        print("\n" * 2)

        print(border)

    def update(self):
        ''' asks for user input to choose the recipe and provide a date and parse it '''

        def well_formated(plan) -> bool:
            return len(plan) == 2 and plan[0].isnumeric() and 1 <= int(plan[0]) <= len(self.cookbook.recipes) and \
                convertdate(plan[1]) is not None

        print("Enter the number of the recipe and date format (type DONE to finish planning)")
        print("The date can be: YYYY-MM-DD, MM-DD, or the first three letters of a day (ex: 2021-09-23, 09-23, Thu)")
        print("Example: 3 2021-04-09")

        plan = []
        prompt = "Choose recipe and date: "
        while True:
            s = input(prompt)
            plan = s.strip().split(" ")
            if s == "DONE":
                return False, None, None
            if well_formated(plan):
                break
            prompt = "Try again (num YYYY-MM-DD): "

        recipe_idx, date_str = plan

        sorted_recipes = sorted(self.cookbook.recipes, key=lambda recipe: recipe.last_eaten)
        recipe = sorted_recipes[int(recipe_idx) - 1]
        date = convertdate(date_str)

        return True, recipe, date

    def write_plan(self, recipes_file, plan):
        '''
        REQ: len(plan) > 0
        writes a plan to file with path recipes_file
        where each line is a "<date> - <recipe1>, <recipe2>, ..."
        where the recipe on each line is meant to be created on that date
        '''

        # sort based on date
        plan = sorted(plan, key=lambda tup: tup[1])

        # make a list[(date string, list[recipe names])] so unique dates are found
        merged_plan = [[plan[0][1].isoformat(), [plan[0][0].name]]]
        for recipe, date in plan[1:]:
            if date.isoformat() == merged_plan[-1][0]:
                merged_plan[-1][1].append(recipe.name)
            else:
                merged_plan.append([date.isoformat(), [recipe.name]])

        with open(recipes_file, "w") as f:
            for date_str, recipe_names in merged_plan:
                f.write(f"{date_str} - {', '.join(recipe_names)}\n")

    def write_grocery_list(self, grocery_list_file, plan):
        '''
        REQ: len(plan) > 0
        writes a grocery list to a file with path grocery_list_file
        where each line is an "<ingredient> - (<recipe1, date1>), (<recipe2, date2>), ..."
        '''

        # get a list of all ingredients from the plan
        ingredients = [ingr for recipe, _ in plan for ingr in recipe.ingredients]

        # create a list[(ingredient names, list[(recipe name, date string)])]
        grocery_list = []
        for ingredient in ingredients:
            # get (recipe, date) pairs where ingredient is in recipe and convert to string
            ingredient_plan = list(filter(lambda plan_item: ingredient in plan_item[0].ingredients, plan))
            plan_list = [f"({recipe.name}, {date.isoformat()})" for recipe, date in ingredient_plan]
            grocery_list.append([ingredient.name, plan_list])

        with open(grocery_list_file, "w") as f:
            for ingredient_name, plan_list in grocery_list:
                f.write(f"{ingredient_name:15} - {', '.join(plan_list)}\n")

    def plan(self, recipes_file, grocery_list_file):
        ''' recipes_file and grocery_list_file must be .txt files '''

        # initialize the vars for storing the recipes
        plan = []

        # adding loop until all recipes exhausted or done
        while True:
            self.view(plan)
            is_planning, recipe, date = self.update()
            if not is_planning:
                break
            plan.append((recipe, date))

        # if the no plan dont make files
        if len(plan) == 0:
            return

        # TODO: update the cookbook to new dates

        # pp the chosen data to files
        self.write_plan(recipes_file, plan)
        self.write_grocery_list(grocery_list_file, plan)
