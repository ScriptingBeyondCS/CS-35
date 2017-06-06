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

def dir_generator(n, max_phones=None, max_recipes=None, dircount=0, max_depth=5):
	""" Takes as input an int n, and randomly generates a 
		tree of n nested subdirectories 
	"""
	# use the same num_dirs we were already counting
	global num_dirs 
	global max_dirs
	# base case
	if num_dirs>max_dirs or max_depth == 0: 
		print(max_dirs>n, max_depth==0, os.getcwd())
		return 

	# so that we can return to where we started when we finish
	while num_dirs < n: 						  # make dirs until we have n
		os.makedirs(str(num_dirs)) 				  # make a unique dir 
		os.chdir(str(num_dirs)) 	  			  # move into it
		num_dirs += 1			  				  # we have 1 more dir now
		# determine how many children this dir will have
		num_children = random.choice([5,6,7,8,9,10]) 
		# now we try to partition the number of subdirectories each gets
		partition_pts = sorted([random.randrange(num_dirs) for i in range(num_children)])
		n_values = [partition_pts[0]] + [partition_pts[i] - partition_pts[i-1] for i in range(1,num_children)]
		# print(n_values)
		children = 0
		while children < num_children: 	 # iterate through each child dir
			os.makedirs(str(num_dirs))
			os.chdir(str(num_dirs))
			num_dirs += 1
			next_n = n_values[children]
			dir_generator(next_n,max_phones,max_recipes,dircount=num_dirs, max_depth = max_depth-1)
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
	max_dirs = n
	original_dir = os.getcwd()
	os.makedirs("tree")
	os.chdir("tree")
	dir_generator(n,dircount=num_dirs)
	# tree_generator(n,max_phones,max_recipes)


def main():
	""" main takes no arguments 
	"""

main_generator(1000)