from shutil import copy2

# importing os module  
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# import sleep to show output for some time period 
from time import sleep 

# Path 
path = os.path.join(dir_path, "..", "images")

def saveImageToDatabse(imagePath, newName):
    try:
        # FIXME: Add an inspector to check if image exists with same name.
        # newName + imagePath.split(".")[1] => gives you the extension as it will be filename.ext => [filename, ext]
        imageExtension = imagePath.split(".")[1]
        copy2(imagePath, os.path.join(path, newName + "." + imageExtension))
        print("Success")
        sleep(1)
    except:
        print("Somethings wrong. Code: 517")
