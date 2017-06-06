import os 
import os.path 
import random 

numdirs = 0

# finish these later 
discrete_ingredients = ['eggs', 'pears', 'apples', 'oranges', 'onions']
by_weight_ingredients = ['flour', 'peanuts', 'frozen blueberries', 'mushrooms', 'chevre']
by_volume_ingredients = ['cinnamon', 'brown sugar', 'milk', '']
meat_ingredients = ['chicken', 'beef', 'pork']
fish = ['salmon', 'tilapia', 'halibut', 'cod', 'tuna']

weights = ['kilograms', 'ounces', 'grams', 'pounds']
volumes = ['cups', 'teaspoons', 'tablespoons']

def phone_number_gen(n):
	""" Takes as input an int n, and randomly generates 
		n phone numbers of various styles 
	"""


def recipe_generator(n):
	""" Takes as input an int n, and randomly generates
		n .txt files containing recipes 
	"""

def dir_generator(n, max_phones, max_recipes, dircount=0):
	""" Takes as input an int n, and randomly generates a 
		tree of n nested subdirectories 
	"""
	global numdirs
	if dircount>n:
		return 0
	first_dir = os.getcwd()
	while numdirs < n: 
		os.makedirs(str(numdirs))
		num_children = random.choice([0,1,2,3,4,5])
		children = 0
		os.chdir(str(numdirs))
		parent_dir = numdirs
		numdirs += 1
		while children < num_children:
			dirs_left = n-numdirs 
			next_n = dirs_left//num_children
			dir_generator(next_n,max_phones,max_recipes,dircount=numdirs)
			children += 1
		os.chdir('..')
		# choice = random.choice([2,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
		# if choice==1:
		# 	os.chdir(str(numdirs))
		# 	numdirs += 1
		# elif choice==0: 
		# 	if os.getcwd() != first_dir:
		# 		os.chdir("..")
		# 	numdirs += 1
		# else:
		# 	os.chdir(first_dir)
		# 	numdirs += 1
	os.chdir(first_dir)
	print('returning')
	return numdirs

def tree_generator(n, max_phones, max_recipes):
	""" Takes as input an int n, and randomly generates a 
		tree of n nested subdirectories 
	"""
	original_dir = os.getcwd()
	os.makedirs("treea")
	os.chdir("treea")
	first_dir = os.getcwd()
	numdirs = 0
	while numdirs < n: 
		os.makedirs(str(numdirs))
		choice = random.choice([2,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
		if choice==1:
			os.chdir(str(numdirs))
			numdirs += 1
		elif choice==0: 
			if os.getcwd() != first_dir:
				os.chdir("..")
			numdirs += 1
		else:
			os.chdir(first_dir)
			numdirs += 1
	os.chdir(original_dir)

def main_generator(n,max_phones,max_recipes):
	global original_dir
	original_dir = os.getcwd()
	os.makedirs("tree")
	os.chdir("tree")
	dir_generator(n,max_phones,max_recipes, dircount=numdirs)
	tree_generator(n,max_phones,max_recipes)


def main():
	""" main takes no arguments 
	"""

main_generator(1000,1,1)