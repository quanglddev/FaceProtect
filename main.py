'''
Handles all input/output
'''
import face_recognition

from Tools.ClearTool import clear
# ! For testing only, delete upon production
from time import sleep

from Tools.SaveImageTool import saveImageToDatabse
from Tools.RecognizerTool import startRecognition
from Tools.TakePictureTool import takePictureUsingWebcam
from Tools.Database import DatabaseManager

from Models.Face import Face

# * DatabaseManager handles all database issues related
db_man = DatabaseManager()
 
'''
# ! This is cool (Better Comments extension (try))
# TODO: Save encodings to database everytime user adds a new face
'''

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
            # try:
            showHeader()
            newName = input("Enter name of the person whose data is to be entered: ")

            # Decide whether the user want to take new image or use existing image
            showRequestImageOption()
            shouldNewImage = input("Do you want to use existing image or take a new one?: ")
            __saveImagePath = None
            if shouldNewImage == "1":
                newImagePath = input(("Enter the path storing %s's face: " % (newName)))
                __saveImagePath = saveImageToDatabse(newImagePath, newName)
            elif shouldNewImage == "2":
                __saveImagePath = takePictureUsingWebcam(newName)

            print(__saveImagePath)

            someone_image = face_recognition.load_image_file(__saveImagePath)
            someone_face_encoding = face_recognition.face_encodings(someone_image)[0]
            
            __newFace = Face(__saveImagePath, newName, someone_face_encoding)
            print("Learned", someone_face_encoding)
            db_man.addNewFace(__newFace)
            print("Run")
            sleep(10)
            # except:
            #     # ! In case face is not detected
            #     pass
        elif option == "2":
            sleep(2)
            print(db_man.getAllFaces())
            # startRecognition()
    print("Exiting...! Thanks for using the program")