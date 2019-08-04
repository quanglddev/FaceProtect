'''
Handles all input/output
'''

from Tools.ClearTool import clear
from Tools.SaveImageTool import saveImageToDatabse
from Tools.RecognizerTool import startRecognition
from Tools.TakePictureTool import takePictureUsingWebcam

def showHeader():
    clear()
    print("================================================")
    print("======== Welcome to [________] program =========")
    print("================================================")
    print()
    
def showMenu():
    print("1. Add new Face")
    print("2. Start Face Recognition")
    print("3. Exit")
    print()

def showRequestImageOption():
    print("================================================")
    print("1. Use existing image (provide image path)")
    print("2. Take new image (press 'o' to take new picture)")
    print()

option = None
if __name__ == "__main__":
    while option != "3":
        showHeader()
        showMenu()
        option = input("What you wanna do?: ")
        if option == "1":
            showHeader()
            newName = input("Enter name of the person whose data is to be entered: ")

            # Decide whether the user want to take new image or use existing image
            showRequestImageOption()
            shouldNewImage = input("Do you want to use existing image or take a new one?: ")
            if shouldNewImage == "1":
                newImagePath = input(("Enter the path storing the %s's face: " % (newName)))
                saveImageToDatabse(newImagePath, newName)
            elif shouldNewImage == "2":
                takePictureUsingWebcam(newName)
        elif option == "2":
            startRecognition()
    print("Exiting...! Thanks for using the program")