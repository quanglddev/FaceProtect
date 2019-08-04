'''
Handles all input/output
'''

from Tools.ClearTool import clear
from Tools.SaveImageTool import saveImageToDatabse
from Tools.RecognizerTool import startRecognition

def showMenu():
    clear()
    print("==============================================")
    print("======== Welcome to [______] program =========")
    print("==============================================")
    print("1. Add data")
    print("2. Start Face Recognition")
    print("3. Exit")
    print()

option = None
if __name__ == "__main__":
    while option != "3":
        showMenu()
        option = input("What you wanna do?: ")
        if option == "1":
            newName = input("Enter name of the person whose data is to be entered: ")
            newImagePath = input(("Enter the path storing the %s's face: " % (newName)))
            saveImageToDatabse(newImagePath)
        elif option == "2":
            startRecognition()
            break
    print("Exiting...! Thanks for using the program")