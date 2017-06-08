import os
import os.path

#Problem 5

def createFile(filePath, text):
    """creates a file named filePath with specified text"""
    f = open(filePath, 'a+')
    f.write(text)
    f.close()

def createNewDir(top, dirName, text, fileName=None, newDirName=None):
    """inputs:  top: a String directory
                dirName: subdirectory in which the new directory/files will go
                text: text in the file
                fileName: name of the new file
                newDirName: name of the new directory
               
    Creates a new directory with or without a file OR file alone and places them
    in the specified location"""
        
    if top == dirName:
        if not newDirName == None:
            dirPath = os.path.join(top, newDirName)
            os.mkdir(dirPath)
            if not fileName == None:
                filePath = os.path.join(dirPath, fileName)
                createFile(filePath, text)
        else:
            if not fileName == None:
                filePath = os.path.join(entry.path, fileName)
                createFile(filePath, text)

    allEntries = os.scandir(top)
    for entry in allEntries:        
        
        if entry.is_dir():
            if entry.name == dirName:
                if not newDirName == None:
                    dirPath = os.path.join(entry.path, newDirName)
                    os.mkdir(dirPath)
                    if not fileName == None:
                        filePath = os.path.join(dirPath, fileName)
                        createFile(filePath, text)
                else:
                    if not fileName == None:
                        filePath = os.path.join(entry.path, fileName)
                        createFile(filePath, text)
            else:
                createNewDir(entry.path, dirName, fileName, text)
                               
        