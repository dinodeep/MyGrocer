

'''
parse the arguments
1. text file containing ingredient names separated on each lin
2. json file for storing ingredients to a pantry
3. OPTIONAL - the name of the pantry to store it to
'''

from classes.ingredient import Ingredient
from classes.pantry import Pantry

import sys

# parse the arguments
args = sys.argv
ingredients_file = args[1]
pantry_file = args[2]

# create the pantry (update name if provided)
pantry = Pantry(pantry_file)
if len(args) > 3:
    pantry.name = args[3]

# open the file for ingredients and load each ingredient into the pantry
with open(ingredients_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        name = line.strip().lower()
        if name != "":
            pantry.add(Ingredient(name))

# save and print the pantry
pantry.save()
print(pantry)
