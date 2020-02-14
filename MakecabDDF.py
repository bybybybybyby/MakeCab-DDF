import os
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()  # show only dialog, hides root window GUI elements
dirName = filedialog.askdirectory(initialdir = root)

print(dirName)

##path = os.path.split(root.filename)[0] # path of file selected
##file = os.path.split(root.filename)[1] # filename
##file_no_ext = os.path.splitext(file)[0] # filename with extension removed



output_file = 'Output_Test.ddf'

def createHeader():
    with open(output_file, "w") as source:    
        header = r""";*** MakeCAB Directive file;
.OPTION EXPLICIT
.Set CabinetNameTemplate="TESThardcode.cab"
.Set DiskDirectory1="C:\BRIAN\Tools\Brian Tools\MakeCab DDF Directive File Creator\TestOutput"
.Set MaxDiskSize=0
.Set Cabinet=on
.Set Compress=on
"""    
        source.write(header)


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles


# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)

createHeader() # write DDF file header

with open(output_file, "a") as source:  # Append list of files below header
    for x in listOfFiles:
        source.write("\"" + x + "\" ")   # Output full file path and name
        short_dir = x.replace(dirName, '')  # Create filepath after chosen directory
        source.write("\"" + short_dir + "\"\n")   # Output shortened path that ends up in cab
    
