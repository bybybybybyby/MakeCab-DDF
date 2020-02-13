import os

dirName = 'Test';
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

createHeader() # write header to top of new file ***TODO-make selectable paths

with open(output_file, "a") as source:
    for x in listOfFiles:
        source.write("\"" + x + "\"\n")   # Output each filename between double quotes and add new line
    
