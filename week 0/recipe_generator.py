import os
import os.path
import random

discrete_ingredients = ['eggs', 'pears', 'apples', 'oranges', 'onions']
by_weight_ingredients = ['flour', 'peanuts', 'frozen blueberries', 'mushrooms', 'chevre']
by_volume_ingredients = ['cinnamon', 'sugar', 'milk', '']

fish = ['salmon', 'tilapia', 'halibut', 'cod', 'tuna']

weights = ['kilograms', 'ounces', 'grams', 'pounds']
volumes = ['cups', 'teaspoons', 'tablespoons']


meats = ['chicken', 'beef', 'pork', 'tofu']
meat_spices = ['red pepper', 'garlic', 'cumin', 'chili powder', 'parsley']
vegetables = ['carrots', 'peas', 'poblanos', 'bell peppers', 'onions']

fruits = ['apples', 'cherries', 'blueberries', 'peaches', 'pecans']
fruit_spices = ['cinnamon', 'vanilla', 'nutmeg', 'lemon juice']

crust = ['flour', 'sugar', 'butter', 'shortening', 'salt']

def recipe_generator(n):
	""" Takes as input an int n, and randomly generates
		n .txt files containing recipes
	"""
	for i in range(n):
		f = open("recipe"+str(i+1), "w+")
		f.write("Experimental pie number "+str(i+1)+"!\n")
		f.write("Ingredients:\n")

		#Pies are either meat or fruit
		if(random.choice([0,1])):
			f.write("Meat pie")

		else:
			f.write("Fruit pie")

		f.write("Instructions:\n")
		f.write("Bake at "+str(random.randrange(200,500, 50))+" degrees for "+str(random.randrange(20,100, 10))+" minutes")


def main():
	""" Main
	"""
	recipe_generator(5)

if __name__ == '__main__':
	main()
