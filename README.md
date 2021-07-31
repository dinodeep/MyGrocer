# MyGrocer 🥗
### Mange your cooking life 🥄

----------------------------------------

**MyGrocer** is an application intended for managing your cooking schedule and grocery shopping. With **MyGrocer**, you will be able to 
1. create and manage the ingredients you use and the recipes that you cook
2. develop a digital cookbook to view and manage your recipes 
3. track when you've last eaten a specific meal
4. create a grocery list and an eating schedule for meals

## Use 🥣
Clone this repository and run `./mygrocer` in the repository. Enter two files where you want to store your *ingredients* and *recipes* into your virtual pantry and cookbook respectively. Then, an interface will pop up to edit these files. 

- Start with *editing the pantry* by giving it a name and filling it with ingredients. 
- Then, you can edit the cookbook by filling it with recipes. These recipes can only have ingredients that you store from your pantry. 
- Finally, once you've populated the cookbook with recipe, create a grocery list. You will need to provide two files for storing the *plan* and the *grocery list*.

----------------------------------------

## Source </>
The source code for this application was created in `Python3` and compiled into the `mygrocer` executable using `PyInstaller`. The code consists of various classes for creating, storing, and editing ingredients, recipes, pantries, cookbooks, and more. 

Currently, this project just finished its initial phase; however, there are other plans to enhance this application to make it more usable. Some of which include:
- [ ] porting this application to a web-app via Django or some other framework (opens new features: accounts, database storing, global recipe accesses, and more)
- [ ] improving the GUI of the interface for ease of use
- [ ] logging the grocery manager to create a history of meals cooked over time
- [ ] easy editing for recipes - the only way to edit a recipe is to delete it and replace it
- [ ] adding recommendations to the grocery list creator to recommend recipes based on ingredient similarity and more
- [ ] implementing ingredient and recipe quantities to allow for quantities in grocery lists
- [ ] creating a grocery list filter so that users can safely ignore recipes they typically always have like salt or butter
