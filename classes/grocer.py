'''
grocer.py implements the Grocer class
'''

from classes.cookbook import Cookbook

import datetime
import os


def clear():
    ''' clears the terminal screen '''
    os.system("clear")


class Grocer:

    def __init__(self, cookbook: Cookbook):
        self.cookbook = cookbook

    def view(self, plan):
        ''' prints the options that the user has to choose from for planning '''

        clear()

        title = f"Recipes from {self.cookbook.name}"
        border = "=" * len(title)

        print(title)
        print(border)
        for i, recipe in enumerate(self.cookbook.recipes):
            print(f"{i + 1}. {recipe.name}")
        print("\n" * 2)

        print(border)
        print("Current Plan")
        for recipe, date in sorted(plan, key=lambda _, d: d):
            print(f"\t- {recipe.name} ({date.isoformat()})")
        print("\n" * 2)

        print(border)

    def update(self):
        ''' asks for user input to choose the recipe and provide a date and parse it '''

        print("Enter the number of the recipe and date in YYYY-MM-DD format (type DONE to finish planning)")
        print("Example: 3 2021-04-09")

        s = []
        prompt = "Choose recipe and date: "
        while len(s) != 2:
            s = input(prompt)
            if s == "DONE":
                return False, None, None
            plan = input(prompt).strip().split(" ")
            prompt = "Try again (num YYYY-MM-DD): "

        recipe_idx, date_str = plan

        recipe = self.cookbook.recipes[str(recipe_idx) - 1]
        date = datetime.date.fromisoformat(date_str)

        return True, recipe, date

    def write_plan(self, recipes_file, plan):
        '''
        REQ: len(plan) > 0
        writes a plan to file with path recipes_file
        where each line is a "<date> - <recipe1>, <recipe2>, ..."
        where the recipe on each line is meant to be created on that date
        '''

        # sort based on date
        plan = sorted(plan, key=lambda _, d: d)

        # make a list[(date string, list[recipe names])] so unique dates are found
        merged_plan = [[plan[0][1], [plan[0][0].name]]]
        for recipe, date in plan[1:]:
            if date == merged_plan[-1][0]:
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
            ingredient_plan = list(filter(lambda recipe, _: ingredient in recipe.ingredients, plan))
            plan_list = [f"({recipe.name}, {date.isoformat()})" for recipe, date in ingredient_plan]
            grocery_list.append([ingredient.name, plan_list])

        with open(grocery_list_file, "w") as f:
            for ingredient_name, plan_list in grocery_list:
                f.write(f"{ingredient_name} - {', '.join(plan_list)}\n")

    def plan(self, recipes_file, grocery_list_file):
        ''' recipes_file and grocery_list_file must be .txt files '''

        # initialize the vars for storing the recipes
        plan = []

        # adding loop until all recipes exhausted or done
        is_planning = True
        while is_planning:
            self.view(plan)
            is_planning, recipe, date = self.update()
            plan.append((recipe, date))

        # if the no plan dont make files
        if len(plan) == 0:
            return

        # TODO: update the cookbook to new dates

        # pp the chosen data to files
        self.write_plan(recipes_file, plan)
        self.write_grocery_list(grocery_list_file, plan)
