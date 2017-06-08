import os
import os.path

# Problem 2

def countFilesOfType(top, extension):
    """inputs:  top: a String directory
                extension: a String file extension
        returns a count of files with a given extension in the directory top and its subdirectories"""
        
    count = 0
    filenames = [x[2] for x in os.walk(top)]
    for fileList in filenames:
        for file in fileList:
            if file.endswith(extension):
                count += 1
    return count

# Have to change directories
def countString(top, string):
    
    total = countStringHelper(top, string)
    os.chdir('../')
    return total


def countStringHelper(top, string):
    """inputs:  top: a String directory
                string: a string to search for
        returns a count of files within a given directory and its subdirectories that contain a given string"""
    count = 0
    allEntries = os.scandir(top)
    os.chdir(top)
    for entry in allEntries:
        if entry.is_file():
            try:
                f = open(entry.name, 'r')
                data = f.read()
                f.close()
            except PermissionError:
                print(entry.name, "couldn't be opened: permission error")
                data = ""
            except UnicodeDecodeError: 
                print(entry.name, "couldn't be opened: encoding error")
                data = ""
            except TypeError: 
                print(entry.name, "couldn't be opened: type error")
                data = ""
            if string in data:
                count += 1
        elif entry.is_dir():
            count += countStringHelper(entry.name, string)
            os.chdir('../')
        else:
            pass
    return count


def countNumDigits(top, numDigits):
    total = countNumDigitsHelper(top, numDigits)
    os.chdir('../')
    return total



def countNumDigitsHelper(top, numDigits):
    """inputs:  top: a String directory
                string: a string to search for
        returns a count of files within a given directory and its subdirectories that contain a given string"""
    count = 0
    allEntries = os.scandir(top)
    os.chdir(top)
    for entry in allEntries:
        if entry.is_file():
            try:
                f = open(entry.name, 'r')
                data = f.read()
                f.close()
            except PermissionError:
                print(entry.name, "couldn't be opened: permission error")
                data = ""
            except UnicodeDecodeError: 
                print(entry.name, "couldn't be opened: encoding error")
                data = ""
            except TypeError: 
                print(entry.name, "couldn't be opened: type error")
                data = ""
            if countDigits(data) == numDigits:
                count += 1
        elif entry.is_dir():
            count += countNumDigitsHelper(entry.name, numDigits)
            os.chdir('../')
        else:
            pass
    return count

def countDigits(string):
    count = 0
    for char in string:
        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or \
        char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
            count += 1
    
    return count 



# Uses Global Pathways
def globalCountString(top, string):
    """inputs:  top: a String directory
                string: a string to search for
        returns a count of files within a given directory and its subdirectories that contain a given string
        * Doesn't change the current working directory"""
    count = 0
    
    allEntries = os.scandir(top)    # all files and directories in top
    for entry in allEntries:        
        if entry.is_file():         
            try:
                f = open(entry.path, 'r')      # open and read file (used .path to prevent changing directories)
                data = f.read()
                f.close()
            except PermissionError:
                print(entry.path, "couldn't be opened: permission error")
                data = ""
            except UnicodeDecodeError: 
                print(entry.path, "couldn't be opened: encoding error")
                data = ""
            except TypeError: 
                print(entry.path, "couldn't be opened: type error")
                data = ""
            if string in data:
                count += 1
        elif entry.is_dir():                    # repeat if entry is a directory
            count += globalCountString(entry.path, string)
            
        else:
            pass

    return count



    

        