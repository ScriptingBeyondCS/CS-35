import os
import os.path
import shutil

# 1
def countFilesOfType(top, extension):
    """inputs:  top: a String directory
                extension: a String file extension
        returns a count of files with a given extension in the directory 
        top and its subdirectories"""
        
    count = 0
    filenames = [x[2] for x in os.walk(top)]
    for fileList in filenames:
        for file in fileList:
            if file.endswith(extension):
                count += 1
    return count
# 2 & 3
def findMaxDepth(top):
    """inputs:  top: a String directory       
        returns maximum directory depth within top, prints path to max depth
    """
    return findMaxDepthHelper(top, [])
def findMaxDepthHelper(top, pathList):

   
    maxDepth = 0
    maxPath = getMaxSlashes(pathList)
    depth = 0
    
    allEntries = os.scandir(top)    # all files and directories in top
    for entry in allEntries:        
    
        if entry.is_dir():  
            nextDepth, maxPath = findMaxDepthHelper(entry.path, pathList) 
            pathList += [entry.path]                
            depth = 1 + nextDepth            

            if depth > maxDepth:
                maxDepth = depth
               
                           
    return maxDepth, maxPath
# 4
def countHaveTenDigits(top):
    """inputs:  top: a String directory     
        returns the number of files within top and its subdirectories that 
        have a 10 digit phone number
    """
    count = 0

    allEntries = os.scandir(top)    # all files and directories in top
    for entry in allEntries:        
        if entry.is_file():         
            try:
                f = open(entry.path, 'r')      # open and read file (used .path to prevent changing directories)
                data = f.read()
                f.close()
            except PermissionError:
                
                data = ""
            except UnicodeDecodeError: 
                
                data = ""
            except TypeError: 
                
                data = ""
            if countDigits(data) == 10:
                count += 1
        elif entry.is_dir():                    # repeat if entry is a directory
            count += countHaveTenDigits(entry.path)
            
        else:
            pass

    return count

# 5
def count909AreaCode(top):
    """inputs:  top: a String directory  
        returns number of files within top directory and its subdirectories 
        that have a 909 area code"""
    count = 0

    allEntries = os.scandir(top)    # all files and directories in top
    for entry in allEntries:        
        if entry.is_file():         
            try:
                f = open(entry.path, 'r')      # open and read file (used .path to prevent changing directories)
                data = f.read()
                f.close()
            except PermissionError:
                
                data = ""
            except UnicodeDecodeError: 
                
                data = ""
            except TypeError: 
                
                data = ""
            newData = makeDigitString(data)
            if newData[0:3] == '909':
                count += 1
        elif entry.is_dir():                    # repeat if entry is a directory
            count += count909AreaCode(entry.path)
            
        else:
            pass

    return count

# 6
def countLastName(top, name):
    """inputs:  top: a String directory   
                name: a last name   
        returns a count of files within top and subdirectories 
        that have a given last name"""
    count = 0

    allEntries = os.scandir(top)    # all files and directories in top
    for entry in allEntries:        
        if entry.is_file():         
            try:
                f = open(entry.path, 'r')      # open and read file (used .path to prevent changing directories)
                data = f.read()
                f.close()
            except PermissionError:
                
                data = ""
            except UnicodeDecodeError: 
                
                data = ""
            except TypeError: 
                
                data = ""
            newData = getName(data)
    
            if ',' in newData:
                if newData.startswith(name):
                    count += 1
            else:
                if newData.endswith(name):               
                    count += 1
        elif entry.is_dir():                    # repeat if entry is a directory
            count += countLastName(entry.path, name)
            
        else:
            pass

    return count

# 7
def countFirstName(top, name):
    """inputs:  top: a String directory   
                name: a first name   
        returns a count of files within top and its subdirectories 
        that have a given first name"""
    count = 0

    allEntries = os.scandir(top)    # all files and directories in top
    for entry in allEntries:        
        if entry.is_file():         
            try:
                f = open(entry.path, 'r')      # open and read file (used .path to prevent changing directories)
                data = f.read()
                f.close()
            except PermissionError:
                
                data = ""
            except UnicodeDecodeError: 
                
                data = ""
            except TypeError: 
                
                data = ""
            newData = getName(data)
            if ',' in newData:
                if newData.endswith(name):
                    count += 1
            else:
                if newData.startswith(name):               
                    count += 1
        elif entry.is_dir():                    # repeat if entry is a directory
            count += countFirstName(entry.path, name)
            
        else:
            pass

    return count

# 8
def countInitials(top, firstInit, lastInit):
    """inputs:  top: a String directory   
                firstInit: the name's first initial 
                lastInit: the name's last initial 
        returns a count of files within top  and its subdirectories 
        that have a name with the given initials"""
    count = 0

    allEntries = os.scandir(top)    # all files and directories in top
    for entry in allEntries:        
        if entry.is_file():         
            try:
                f = open(entry.path, 'r')      # open and read file (used .path to prevent changing directories)
                data = f.read()
                f.close()
            except PermissionError:
                
                data = ""
            except UnicodeDecodeError: 
                
                data = ""
            except TypeError: 
                
                data = ""
            newData = getName(data)
            if ',' in newData:
                if getOneAfterSpace(newData) == firstInit and newData[0] == lastInit:
                    count += 1
            else:
                if getOneAfterSpace(newData) == lastInit and newData[0] == firstInit:            
                    count += 1

        elif entry.is_dir():                    # repeat if entry is a directory
            count += countInitials(entry.path, firstInit, lastInit)
            
        else:
            pass

    return count

# 9
def diffFirstName(top):
    """inputs:  top: a String directory    
        returns a number of unique first names in 
        files of top and its subdirectories"""
    return diffFirstNameHelper(top, [])
def diffFirstNameHelper(top, nameList):
    allEntries = os.scandir(top)    # all files and directories in top
    for entry in allEntries:        
        if entry.is_file():         
            try:
                f = open(entry.path, 'r')      # open and read file (used .path to prevent changing directories)
                data = f.read()
                f.close()
            except PermissionError:
                
                data = ""
            except UnicodeDecodeError: 
                
                data = ""
            except TypeError: 
                
                data = ""
            firstName = getFirstName(data)
            if firstName not in nameList and firstName != None:
                nameList += [firstName]

        elif entry.is_dir():                    # repeat if entry is a directory
            diffFirstNameHelper(entry.path, nameList)
            
        else:
            pass
    
    return len(nameList)


# HELPER FUNCTIONS
def getMaxSlashes(L):
    maxCount = 0
    index = 0
    if L == []:
        return ''
    else:
        for i in range(len(L)):
            count = 0
            for char in L[i]:
                if char == '/':
                    count += 1
            if count > maxCount:
                maxCount = count
                index = i

        return L[index]
        
def countDigits(string):
    """return number of digits in a string (Helper for countHaveTenDigits)"""
    count = 0
    for char in string:
        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or \
        char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
            count += 1
    
    return count 
def makeDigitString(string):
    """Gathers all digits and returns them in a continuous string
    (Helper for count909AreaCode)"""
    newString =  ''
    for char in string:
        if char in '0123456789':
            newString += char
    return newString

def getOneAfterSpace(string):
    """returns next character after a space in given string
    (Helper for countInitials)"""
    result = ''
    reachedSpace = False
    for i in range(len(string)):
        if string[i] == ' ':
            return string[i+1]
            
    return ''

def getAllAfterSpace(string):
    """returns all characters after a space in given string
    (Helper for getFirstName)"""
    result = ''
    for i in range(len(string)):
        if string[i] == ' ':
            return string[i+1:]
            
    return ''
def getAllBeforeSpace(string):
    """returns all characters before a space in given string
    (Helper for getFirstName)"""
    result = ''
    for i in range(len(string)):
        if string[i] == ' ':
            return string[:i]
            

def getName(string):
    """Grab the name as written in files (Helper)"""
    newString =  ''
    reachedLetter = False
    for char in string:
        
        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            reachedLetter = True
        if reachedLetter == True and char == '\n':
            break
        if reachedLetter == True:
            newString += char
       
    return newString

def getFirstName(string):
    """return the first name (Helper for diffFirstName)"""
    name = getName(string)
    if ',' in name:
        return getAllAfterSpace(name)

    return getAllBeforeSpace(name)

# MAIN
def main():
    print(countFilesOfType('phone_files', '.txt'))
    print(findMaxDepth('phone_files'))
    print(countHaveTenDigits('phone_files'))
    print(count909AreaCode('phone_files'))
    print(countLastName('phone_files', 'DAVIS'))
    print(countFirstName('phone_files', 'DAVIS'))
    print(countInitials('phone_files', 'J', 'S'))
    print(diffFirstName('phone_files'))

# got some inconsistent answers first Name, last Name not working
if __name__ == "__main__":
    main()
