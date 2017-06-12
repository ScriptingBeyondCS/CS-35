import os
import os.path
import shutil

def copy(file1, file2):
    """Copies file1 into file2 (nothing overwritten)"""
    f1 = open(file1, 'r')
    f2 = open(file2, 'a')
    shutil.copyfileobj(f1, f2)
    f1.close()
    f2.close()

def move(file, destination):
    shutil.move(file, destination)

def change(top, origText, newText):
    """change original text in all files in top to newText"""
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
            if data != "":
                newData = data.replace(origText, newText)
                f = open(entry.path, 'w') 
                f.write(newData) 
                f.close()
        elif entry.is_dir():                    # repeat if entry is a directory
            change(entry.path, origText, newText)
            
        else:
            pass


