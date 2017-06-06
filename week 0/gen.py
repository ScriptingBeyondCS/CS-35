import os 
import os.path 
import random 

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
	### Get global tallies 
	global num_dirs  # So that we don't have to pass current dirs whenever we call
	global max_dirs	 # Max dir number
	global max_depth # Don't want files nested deeper than this

	### Base cases
	if num_dirs>max_dirs or depth > max_depth or n==0: 
		# print(num_dirs>max_dirs, depth>max_depth, n==0, os.getcwd()) 
		return 

	### Main function body
	# How many subdirectories do we want to make here?
	num_children = random.choice([3,4,5,6,7]) 
	
	## Distribute the n directories between each of the subdirectories 
	# pick some random numbers on the interval 
	partition_pts = sorted([random.randrange(n) for i in range(num_children)])
	# take the differences between them --> [1,2,3,5] --> [1,1,1,2]
	# tells us the "size" of each part of our partition. 
	n_values = [partition_pts[0]] + # first element always stays the same
			   [partition_pts[i] - partition_pts[i-1] # diff. from prev. gives size
			   for i in range(1,num_children)]
	## Loop through all of the children 
	children = 0 # number of children we've called the function on so far
	while children < num_children: 	 
		os.makedirs(str(num_dirs)) 		# make child dir
		os.chdir(str(num_dirs))	   		# move into it
		num_dirs += 1			   		# account for this change
		next_n = n_values[children] 	# find how many subdirs the child gets
		dir_generator(next_n, depth+1)  # recurse!
		children += 1					# called the function on one more child
		os.chdir('..')					# move back to parent dir



def main_generator(n):
	## Global vars
	# To return to once done (just in case)
	global original_dir
	original_dir = os.getcwd()

	# Set a global tally of the number of dirs we've made so far
	global num_dirs
	num_dirs = 0

	# Set a global limit on the global tally!
	global max_dirs 
	max_dirs = n

	# Maximum number of layers for file tree
	global max_depth
	max_depth = 7

	## 
	# Make a tree directory to not clutter workspace
	os.makedirs("tree")
	# Move into tree directory
	os.chdir("tree")
	# Create n subdirectories
	dir_generator(n, 0)
	# Return to where we started
	os.chdir(original_dir)

def main():
	""" main takes no arguments 
	"""

main_generator(10000)