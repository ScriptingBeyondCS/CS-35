import os
import os.path
import random
import itertools


weights = ['kilograms', 'ounces', 'grams', 'pounds']
volumes = ['cups', 'teaspoons', 'tablespoons']
one_ingredient_instructions = [('Chop the ', '.'), ('Stir in the ', '.'), ('Heat up the ', '.'), ('Add the ', '.'), ('Simmer the ', ' on low heat.')]
two_ingredient_instructions = [('Combine the ', ' and the ', '.'), ("Mix the ", " and the ", " together.")]

meats = ['chicken', 'beef', 'pork', 'tofu']
meat_spices = ['garlic', 'cumin', 'chili powder', 'parsley']
vegetables = ['carrots', 'peas', 'poblanos', 'bell peppers', 'onions']
all_meat_pie_ingredients = [meats, meat_spices, vegetables]

fruits = ['apples', 'cherries', 'blueberries', 'peaches', 'pecans']
fruit_spices = ['cinnamon', 'vanilla', 'nutmeg', 'lemon juice']
all_fruit_pie_ingredients = [fruits, fruit_spices]

crust = ['flour', 'sugar', 'butter', 'shortening', 'salt']

all_ingredients = meats+meat_spices+vegetables+fruits+fruit_spices+crust

def generate_recipes(upper_num, lower_num = 0):
	""" Takes as input a range, and randomly generates upper_num-lower_num
		 .txt files containing recipes, named with the given range
	"""
	for i in range(lower_num, upper_num):
		f = open("recipe"+str(i+1)+".txt", "w+")
		f.write("Experimental pie number "+str(i+1)+"!\n\n")

		all_chosen_ingredients = []
		#Pies are either meat or fruit. Print the filling ingredients.
		if(random.choice([0,1])):
			meat_pie_ingredients_list = choose_ingredients(all_meat_pie_ingredients)
			f.write("Fruit Pie\n")
			f.write("Ingredients:\n")
			f.write("For the filling:\n")
			print_ingredient_amounts(f, meat_pie_ingredients_list)
			all_chosen_ingredients = list(itertools.chain.from_iterable(meat_pie_ingredients_list))
		else:
			fruit_pie_ingredients_list = choose_ingredients(all_fruit_pie_ingredients)
			f.write("Meat Pie\n")
			f.write("Ingredients:\n")
			f.write("For the filling:\n")
			print_ingredient_amounts(f, fruit_pie_ingredients_list)
			all_chosen_ingredients = list(itertools.chain.from_iterable(fruit_pie_ingredients_list))

		#Print the crust ingredients
		f.write("\n")
		f.write("For the crust:\n")
		crust_ingredients = random.sample(crust, random.randint(1, len(crust)))
		for i in crust_ingredients:
			f.write(str(random.randint(2,5))+" "+random.choice(volumes)+" of "+i+"\n")

		#Print the instructions
		f.write("\nInstructions:\n")
		f.write("For the filling:\n")
		print_instructions(f, all_chosen_ingredients)
		f.write("\nFor the crust:\n")
		print_instructions(f, crust_ingredients)
		f.write("\nBake at "+str(random.randrange(200,500, 50))+" degrees for "+str(random.randrange(20,100, 10))+" minutes\n")

def choose_ingredients(all_pie_ingredients):
	""" Takes a list of lists of pie ingredients organized by ingredient type
		Randomly chooses a subset of ingredients of each type, keeping the list of lists structure
	"""
	chosen_ingredients = []
	for ingredient_type in all_pie_ingredients:
		chosen_ingredients.append(random.sample(ingredient_type, random.randint(0,len(ingredient_type))))
	return chosen_ingredients

def print_ingredient_amounts(my_file, pie_ingredients_list):
	for ingredient_type in pie_ingredients_list:
		for ingredient in ingredient_type:
			my_file.write(str(random.randint(2,10))+" "+random.choice(weights+volumes)+" of "+ingredient+"\n")

def print_instructions(my_file, all_chosen_ingredients):
	count = 1
	while(len(all_chosen_ingredients) > 0):
		if(random.choice([0,1]) or len(all_chosen_ingredients) <= 1):
			instruction_choice = random.choice(one_ingredient_instructions)
			ingredient_choice = random.choice(all_chosen_ingredients)
			all_chosen_ingredients.remove(ingredient_choice)
			full_instruction = instruction_choice[0]+ingredient_choice+instruction_choice[1]
		else:
			instruction_choice = random.choice(two_ingredient_instructions)
			ingredient_choice_1 = random.choice(all_chosen_ingredients)
			all_chosen_ingredients.remove(ingredient_choice_1)
			ingredient_choice_2 = random.choice(all_chosen_ingredients)
			all_chosen_ingredients.remove(ingredient_choice_2)
			full_instruction = instruction_choice[0]+ingredient_choice_1+instruction_choice[1]+ingredient_choice_2+instruction_choice[2]
		my_file.write(str(count)+'. '+full_instruction+ '\n')
		count+=1

def main():
	""" Main
	"""
	generate_recipes(5)

if __name__ == '__main__':
	main()
