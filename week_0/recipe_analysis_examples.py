import os
import os.path
import random
import recipe_generator
import subprocess
import shutil

#Which recipe uses the most nutmeg? -> actually not an easy question... Maybe elective q?

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

def is_sweet(recipe):
    return not is_savory(recipe)

def list_recipes_by_condition(path, condition):
    """ Takes a path and a condition function and returns a list of all recipes
        at or below that path that satisfy the given condition
    """
    recipes = []
    for root, directories, files in os.walk(path):
        for f in files:
            with open(os.path.join(root, f), 'r') as f_in:
                if(condition(f_in)):
                    recipes.append(os.path.join(root, f))
    return recipes


def move_recipes_by_condition(path, directory_name, condition):
    """ Moves the recipes that satisfy conditon to a new directory called directory_name
    """
    os.mkdir(directory_name)
    recipe_list = list_recipes_by_condition(path, condition)
    for recipe in recipe_list:
        shutil.move(recipe, os.getcwd()+"/"+directory_name)


#Check if a given recipe is vegetarian i.e. no chicken, pork, or beef.
def is_vegetarian(recipe):
    """ Takes a path to a recipe (.txt file) and determines if that recipe
        is vegetarian
    """
    r = recipe.read()
    if not (("chicken" in r) or ("beef" in r) or("pork" in r)):
        return True
    else:
        return False


#List all vegetarian recipes
def list_veg_recipes(path):
    """ Takes a path and lists the paths of all vegetarian recipes at or below
        that path
    """
    veg_recipes = []
    for root, directories, files in os.walk(path):
        for f in files:
            with open(os.path.join(root, f), 'r') as f_in:
                if(is_vegetarian(f_in)):
                    veg_recipes.append(os.path.join(root, f))
    return veg_recipes


#Move all vegetarian recipes into a directory called "vegetarian_recipes"
def move_veg_recipes(from_path):
    """ Takes a path and moves all vegetarian recipes from that path into a
        directory called vegetarian_recipes
    """
    os.mkdir("vegetarian_recipes")
    veg_recipes = list_veg_recipes(from_path)
    for recipe in veg_recipes:
        shutil.move(recipe, os.getcwd()+"/vegetarian_recipes")

#Comparing all recipes, which has the most measurements in volume rather than weight?

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



if __name__ == '__main__':
        main()
