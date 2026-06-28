import os
import shutil

print("== JPG File Mover ==")

sourceFolder = input("Enter Source Folder Path: ")
destinationFolder = input("Enter Destination Folder Path: ")

if not os.path.exists(destinationFolder):
    os.mkdir(destinationFolder)

files = os.listdir(sourceFolder)

count = 0

for fileName in files:

    if fileName.endswith(".jpg"):

        oldPath = os.path.join(sourceFolder, fileName)
        newPath = os.path.join(destinationFolder, fileName)

        shutil.move(oldPath, newPath)

        print(fileName, "Moved Successfully")
        count = count + 1

print("\nTotal JPG Files Moved:", count)
