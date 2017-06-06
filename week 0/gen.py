import os 
import os.path 
import random 
import functools

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

def dir_generator(n, max_phones, max_recipes, dircount=0, max_depth=10):
	""" Takes as input an int n, and randomly generates a 
		tree of n nested subdirectories 
	"""
	global numdirs # use the same numdirs we were already counting
	if dircount>n or max_depth == 0: # base case 
		return 
	first_dir = os.getcwd() # so that we can return here after finishing
	while numdirs < n: 
		os.makedirs(str(numdirs)) # make a unique dir 
		os.chdir(str(numdirs)) 	  # move into it
		numdirs += 1			  # account for this change
		num_children = random.choice([1,2,3,4,5]) # decide how many children it has
		children = 0
		dirs_left = n-numdirs		 # make sure we don't go over
		partition_pts = [random.randint(0,dirs_left) for i in range(num_children)]
		n_values = [partition_pts[0]] + [partition_pts[i] - partition_pts[i-1] for i in range(1, len(partition_pts))]
		while children < num_children: 	 # iterate through each child dir
			os.makedirs(str(numdirs))
			os.chdir(str(numdirs))
			numdirs += 1
			next_n = n_values[children]
			dir_generator(next_n,max_phones,max_recipes,dircount=numdirs, max_depth = max_depth-1)
			children += 1
			os.chdir('..')
		os.chdir('..')
	os.chdir(first_dir) # return to where the function was called

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
	global numdirs
	original_dir = os.getcwd()
	os.makedirs("tree")
	os.chdir("tree")
	dir_generator(n,max_phones,max_recipes, dircount=numdirs)
	# tree_generator(n,max_phones,max_recipes)


def main():
	""" main takes no arguments 
	"""

main_generator(1000,1,1)