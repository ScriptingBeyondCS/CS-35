import os
import os.path
import random
import itertools
from collections import defaultdict


# How many directories are there on the Hard Drive?
def num_directories(path):
    """ Takes a path and returns the number of directories at or below that path
        including the current directory
    """
    count = 0
    for root, directories, files in os.walk(path):
        count += 1
    return count

# How many files are stored on the Hard Drive?
def num_files(path):
    """ Takes a path and returns the number of files at or below that path
    """
    count = 0
    for root, directories, files in os.walk(path):
        for name in files:
            count += 1
    return count

# What types of files are stored on the Hard Drive?
def file_types(path):
    """ Takes a path and returns a list of the file types of files at or below
        that path
    """
    file_types_list = []
    for root, directories, files in os.walk(path):
        for name in files:
            filename, file_extension = os.path.splitext(name)
            if(not(file_extension in file_types_list)):
                file_types_list.append(file_extension)
    return file_types_list

# How many of each file type are there on the Hard Drive?
def num_files_by_type(path):
    """ Takes a path and returns a dictionary with a file type as the key and
        the number of files of that type as the value
    """
    file_type_counts = defaultdict(int)
    for root, directories, files in os.walk(path):
        for name in files:
            filename, file_extension = os.path.splitext(name)
            file_type_counts[file_extension] += 1
    return file_type_counts

def main():
    path = os.getcwd() + "/tree/"
    number_of_directories = num_directories(path)
    print("There are "+str(number_of_directories)+" total directories on the Hard Drive")
    number_of_files = num_files(path)
    print("There are "+str(number_of_files)+" total files on the Hard Drive")
    file_types_list = file_types(path)
    print("File types on this Hard Drive include: "+str(file_types_list))
    file_type_counts_dict = num_files_by_type(path)
    print("The number of files of each type are as follows: " + str(file_type_counts_dict))
if __name__ == '__main__':
    main()
