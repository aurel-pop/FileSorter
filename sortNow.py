import os
import shutil

# Setting the path to the current directory
path = "."

# Getting a list of files in the directory
files = os.listdir(path)

# Looping through each file in the list
for file in files:
    # Splitting the file name and extension into separate variables
    filename, extension = os.path.splitext(file)

    # Skip over files with the ".py" extension
    if extension == ".py":
        continue

    # Removing the dot from the extension
    extension = extension[1:]

    # Check if a directory with the same name as the extension already exists
    if os.path.exists(path + "/" + extension):
        # If it does, move the file into that directory
        shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
    else:
        # If it doesn't, create a new directory with that name
        os.makedirs(path + "/" + extension)
    
    # Move the file into the new directory
    shutil.move(path + "/" + file, path + "/" + extension + "/" + file)


