#
# cs35 examples in-class  1/23/17
#

"""
DEMO 1:

Building paths to directories and accessing their contents

the os and os.path libraries are documented here:
  https://docs.python.org/3/library/os.html
  https://docs.python.org/3/library/os.path.html
"""

import os
import os.path
import shutil

def directory_examples():
    """ examples for directory navigation and contents... """
    # get current working directory
    original_dir = os.getcwd()
    print("original_dir is", original_dir)

    # construct a path to a directory
    path = os.path.join(original_dir, "addresses")  # the path to the addresses directory
    print("now, I can access", path)

    # get a listing of all of the contents of the directory
    DirContents = os.listdir(path)
    print("DirContents:", DirContents)

    # change back!
    path = os.path.dirname(path) # back to original
    print("and now, path points back to ", path)

    # make a directory called not-hp
    os.mkdir(os.path.join(path, "not-hp"))
    print("Now the contents include not-hp: ", os.listdir(path))

    # move samiam.txt into not-hp
    shutil.move(os.path.join(path, "hp/samiam.txt"), os.path.join(path, "not-hp"))

    # move samiam back to hp
    shutil.move(os.path.join(path, "not-hp/samiam.txt"), os.path.join(path, "hp"))

    # delete the not-hp directory
    os.rmdir(os.path.join(path, "not-hp"))

    # loop through every directory in a tree and print its subdirectories and files
    # os.walk(path) will be useful for the hard drive scavenger hunt!
    for current_directory, sub_directories, files in os.walk(path):
        print(current_directory)
        for file_name in files:
            print(" -" + file_name)
        for sub_directory_name in sub_directories:
            print(" +" + sub_directory_name)


    # +++ Challenge: access the hp directory and list its contents:
    # +++ Challenge: walk the inclass directory and count the number of files



"""
DEMO 2:

Opening files and reading their contents

Documentation:
  https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files
  [Extra] file encodings:  https://docs.python.org/3/library/codecs.html
"""

# Assuming path points to the hp directory, let's open samiam.txt
def file_examples(path):
    """ examples of file reading and exceptions """
    filepath = os.path.join(path, "samiam.txt")
    try:
        f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
        data = f.read()   # read all of the file's data
        f.close()         # close the file
    except PermissionError:  # example of "exceptions": atypical errors
        print("file", filename, "couldn't be opened: permission error")
        data = ""
    except UnicodeDecodeError:
        print("file", filename, "couldn't be opened: encoding error")
        data = "" # no data
    except FileNotFoundError:  # try it with and without this block...
        print("file", filename, "couldn't be opened: not found!")
        print("Check if you're running this in the correct directory... .")
        data = ""

    # We return the data we obtained in trying to open the file
    #print("File data:", data)
    return data    # remember print and return are different!

    # ++ Challenge: loop over all of the files in this directory, add up their contents
    #            and return the results (helpful for problem #2)

    # ++ Challenge: change the function to include an input filename
    #            and return the data from that file (also helpful for #2 and #3)



"""
DEMO 3:

Text analysis of data obtained from a file...

Here we introduce the _much_ nicer alternative to dictionaries, called
    default dictionaries, or defaultdict, with documentation here:
    https://docs.python.org/3/library/collections.html#collections.defaultdict

In addition, we introduce some useful parts of the string library:
    https://docs.python.org/3.1/library/string.html
    Methods such as s.lower(), s.upper(), s.split(), ... are wonderful!
"""

from collections import defaultdict      # be sure to import it!


# We will write a function that counts all of the 'A's and 'a's in the input
def count_a( data ):
    """ this function returns a default dictionary that contains
        the key 'a': its value is equal to the number of 'a's in the input, data
        NOTE: everything is lower-cased, so this really counts 'A's and 'a's
    """
    counts = defaultdict(int)
    # data = data.lower()       # lower case all of the data
    for c in data:            # loop over each character in the data
        if c == 'a' or c == 'A':
            counts['a'] += 1

    return counts


# Here is a function to read the file and call count_a
def main():
    """ This "main" function will read the file "samiam.txt"
        and then count it's A's (or a's) and print the total number present
    """
    # This is an example of a function that you should create so that
    # the graders can test your solutions...
    # Note that it uses other function calls that return values - this one
    # simply prints the results:

    #first, we build a path to the hp directory
    path = os.path.join(os.getcwd(), "hp" )
    data = file_examples(path)
    counts = count_a( data )
    num_of_a = counts['a']
    print("The number of a's in samiam is", num_of_a)

    # For consistency, reset path to inclass
    path = os.path.dirname(path)

    directory_examples()


if __name__ == '__main__':
    main()



# ++ Challenge: create a copy of this function to count _all_ of the letters in the input

# ++ Question: Why does this _not_ count the number of _words_ "a" or "A"?

# ++ Challenge: create a copy of this function that counts all of the _words_ "a" or "A"

# ++ Challenge: create a copy of this function that counts all of the distinct words in the input data
#               how could you ensure that no punctuation is part of the word?

# (Each of these functions should return a default dictionary with appropriate keys and values!)

# ++ Challenge: how many times does "harry" appear in hp1.txt? in hp4.txt?

# ++ Challenge: in which book does "harry" appear more frequently - relative to the size of the book?


"""
PROBLEMS:

With this background, dive into the hw0 problems #2 and #3
  They're linked from here: https://www.cs.hmc.edu/~dodds/cs35/

Here are reminders of each - please include them in separate files,
so that they're easier to grade...  (Feel free to copy this file!)
"""

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Problem 2:  phone-number forensics: analyzing a large set of number/name files

Concrete questions:
1. How many .txt files are in the whole set?
2. Across all of the files, how many of the phone numbers contain exactly 10 digits?
   2b. Of these exactly-ten-digit phone numbers, how many are in the area code 909 (the area code will be the first three digits of a ten-digit number).
3. How many people have the name "GARCIA" in the whole set?


Plus, ask - and answer - three questions of your design. Here were three suggestions,
  but don't take more than one of these: invent your own!
(E1) Area codes beginning with "2" are in the northeast;
      those beginning with "9" are in the southwest. Are there more NE or SW
      phone numbers across the whole dataset (meaning area codes beginning with "2" or "9" respectively)?
(E2) How many different last names (or first names) are present across the entire dataset?
(E3) How many of the phone numbers contain the substring "42" somewhere within them?
     Or, how many have digits that add up to 42 ?
"""




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Problem 3:  A recipe for disaster: organizing a large set of experimental pie recipes

Concrete tasks and questions:
1. How many savory recipes are there?
2. How many sweet recipes are there?
3. How many vegetarian recipes are there?
4. Organize sweet and savory recipes by moving the files into separate directories
    named savory_recipes and sweet_recipes
5. Within savory_recipes, move all vegetarian recipes into a directory named
    vegetarian_recipes
6. Delete all empty directories
7. Across all recipes, which uses the most kilograms of one ingredient? What is the
    ingredient and how many kilograms does the recipe use?

Plus, ask - and answer - three questions of your own. This could also include another
file organization task.
"""




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Problem 4 is to create an initial GitHub page/account
Problem 5 is extra credit (file-writing, in addition to reading...)

Good luck on hw0, everyone!
"""
