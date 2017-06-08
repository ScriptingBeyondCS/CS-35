import os
import os.path

#Problem 3

def compareTwo(top, file1, file2, word):
    
    """inputs:  top: a String directory
                file1: first file to check within top or its subdirectories
                file2: second file to check within top or its subdirectories
                word: a string to search for
        returns either file1 or file2, whichever contains more occurrences of word"""
    count1 = 0
    count2 = 0
    
    allEntries = os.scandir(top)
    for entry in allEntries:        
        if entry.is_file():
            if entry.name == file1:
                try:
                    f = open(entry.path, 'r')
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
                count1 = data.count(word)
            elif entry.name == file2:
                try:
                    f = open(entry.path, 'r')
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
                count2 = data.count(word)
        elif entry.is_dir():
            compareTwo(entry.path, file1, file2, word)
            
        else:
            pass

    print(file1, ": ", word, "appeared", count1, "times")
    print(file2, ": ", word, "appeared", count2, "times")

    if count1 > count2:
        return file1
    else:
        return file2

def compareAll(top, word):
    
    """inputs:  top: a String directory
                word: a string to search for
        returns the file within top or its subdirectories in which word appears most often"""
    mostOccurrences = 0
    fileWithMost = ''
    
    allEntries = os.scandir(top)
    for entry in allEntries:        
        if entry.is_file():
            try:
                f = open(entry.path, 'r')
                data = f.read()
                f.close()
            except PermissionError:
                
                data = ""
            except UnicodeDecodeError: 
                
                data = ""
            except TypeError: 
                
                data = ""
            count = data.count(word)
            if count > mostOccurrences:
                mostOccurrences = count
                fileWithMost = entry.name
        elif entry.is_dir():
            file, count = compareAll(entry.path, word)
            if count > mostOccurrences:
                mostOccurrences = count
                fileWithMost = file
            
        else:
            pass
    
    return fileWithMost, mostOccurrences


def main():
    pass