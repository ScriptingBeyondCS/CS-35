import os
import os.path
import random
import recipe_generator
import subprocess
import shutil

#Comparing all recipes, which uses the fewest ingredients? ...kinda hacky
def fewest_ingredients(path):
    """ Takes a path and returns the recipe txt file with the fewest ingredients
        in the tree specified by that path.
        We take advantage of the recipe structure
    """
    fewest_ingredients = 50
    fewest_ingredients_file_path = ""
    for root, directories, files in os.walk(path):
        for f in files:
            with open(os.path.join(root, f), 'r') as f_in:
                lines = f_in.readlines()
            i = 0
            while(not(lines[i] == "Instructions:\n")):
                i +=1
            if i < fewest_ingredients:
                fewest_ingredients = i
                fewest_ingredients_file_path = os.path.join(root, f)
    return fewest_ingredients_file_path, (fewest_ingredients-7)

#Check if a given recipe is a savory pie
def is_savory(recipe):
    """ Takes a recipe and determines if it is Savory
    """
    r = recipe.read()
    if "Savory" in r:
        return True
    else:
        return False

#Check if a given recipe is a sweet pie
def is_sweet(recipe):
    """ Takes a recipe and determines if it is Sweet
    """
    return not is_savory(recipe)

#Check if a given recipe is vegetarian i.e. no chicken, pork, or beef.
def is_vegetarian(recipe):
    """ Takes a recipe and determines if it is vegetarian
    """
    r = recipe.read()
    if not (("chicken" in r) or ("beef" in r) or("pork" in r)):
        return True
    else:
        return False

#List all of the vegetarian recipes
def list_recipes_by_condition(path, condition):
    """ Takes a path and a condition function and returns a list of the paths of all recipes
        at or below that path that satisfy the given condition
    """
    recipes = []
    for root, directories, files in os.walk(path):
        for f in files:
            with open(os.path.join(root, f), 'r') as f_in:
                if(condition(f_in)):
                    recipes.append(os.path.join(root, f))
    return recipes

#Move all of the vegetarian recipes to a directory called vegetarian_recipes
def move_recipes_by_condition(path, directory_name, condition):
    """ Moves the recipes that satisfy conditon to a new directory called directory_name
    """
    os.mkdir(directory_name)
    recipe_list = list_recipes_by_condition(path, condition)
    for recipe in recipe_list:
        shutil.move(recipe, os.getcwd()+"/"+directory_name)

#Remove all empty directories
def remove_empty_directories(path):
    """ Remove empty directories at or below path
    """
    for root, directories, files in os.walk(path):
        if not os.listdir(root):
            os.rmdir(root)

#Across all recipes, which crust uses the most butter?

#Across all recipes, which recipe calls for the most kilograms of one ingredient?
#What is the ingredient and how much of it does the recipe call for?
def most_kilograms_of_one_ingredient(path):
    most_kilos = 0
    most_kilos_ingredient = ""
    for root, directories, files in os.walk(path):
        for f in files:
            with open(os.path.join(root, f), 'r') as f_in:
                lines = f_in.readlines()
                for l in lines:
                    if "kilograms" in l:
                        l_split = l.split(" ")
                        kilos = int(l_split[0])
                        if kilos > most_kilos:
                            most_kilos = kilos
                            most_kilos_ingredient = l_split[3]
                            most_kilos_file = f
    return most_kilos, most_kilos_ingredient, most_kilos_file

    
#Across all recipes, how many use the metric system, how many use the imperial system,
# and how many use a mix of both?


def main():
    # Generate a tree of recipes for testing
    ls = os.listdir()
    if "recipes" in ls:
        shutil.rmtree("recipes")
    os.mkdir("recipes")
    os.chdir("recipes")
    recipe_generator.generate_recipes(50)
    for i in range(5):
        os.mkdir("recipes"+str(i))
        os.chdir("recipes"+str(i))
        recipe_generator.generate_recipes(60+(i*10), 50+(i*10))
        os.chdir("..")

    #test questions
    path = os.getcwd()
    fewest_ingredients_answer = fewest_ingredients(path)
    print(fewest_ingredients_answer)
    move_recipes_by_condition(path, "savory_recipes", is_savory)
    move_recipes_by_condition(path, "sweet_recipes", is_sweet)
    move_recipes_by_condition(path+"/savory_recipes","savory_recipes/vegetarian_recipes", is_vegetarian)
    remove_empty_directories(path)
    print(most_kilograms_of_one_ingredient(path))


if __name__ == '__main__':
        main()
