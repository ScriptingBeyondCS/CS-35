import os 
import os.path 
import random 
import functools

num_dirs = 0

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

def dir_generator(n, depth):
	""" Takes as input an int n, and randomly generates a 
		tree of n nested subdirectories 
	"""
	global num_dirs 
	global max_dirs
	global max_depth
	if num_dirs>max_dirs or depth > max_depth: 
		print(num_dirs>max_dirs, depth>max_depth, os.getcwd())
		return 
	# numdirs = 0
	# os.makedirs(str(num_dirs))
	# os.chdir(str(num_dirs))
	# num_dirs += 1
	# numdirs += 1
	num_children = random.choice([3,4,5,6,7]) 
	# partition_pts = sorted([random.randrange(num_dirs) for i in range(num_children)])
	try:
		partition_pts = sorted([random.randrange(n) for i in range(num_children)])
		n_values = [partition_pts[0]] + [partition_pts[i] - partition_pts[i-1] for i in range(1,num_children)]
		children = 0
		while children < num_children: 	 
			os.makedirs(str(num_dirs))
			os.chdir(str(num_dirs))
			num_dirs += 1
			next_n = n_values[children]
			dir_generator(next_n, depth+1)
			children += 1
			os.chdir('..')
	except: 
		return

def tree_generator(n, max_phones, max_recipes):
	""" Takes as input an int n, and randomly generates a 
		tree of n nested subdirectories 
	"""
	original_dir = os.getcwd()
	os.makedirs("treea")
	os.chdir("treea")
	first_dir = os.getcwd()
	num_dirs = 0
	while num_dirs < n: 
		os.makedirs(str(num_dirs))
		choice = random.choice([2,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
		if choice==1:
			os.chdir(str(num_dirs))
			num_dirs += 1
		elif choice==0: 
			if os.getcwd() != first_dir:
				os.chdir("..")
			num_dirs += 1
		else:
			os.chdir(first_dir)
			num_dirs += 1
	os.chdir(original_dir)

def main_generator(n):
	global original_dir
	global num_dirs
	global max_dirs 
	global max_depth
	max_dirs = n
	max_depth = 5
	original_dir = os.getcwd()
	os.makedirs("tree")
	os.chdir("tree")
	dir_generator(n, 0)


def main():
	""" main takes no arguments 
	"""

main_generator(10000)