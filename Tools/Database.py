from tinydb import TinyDB, Query

# importing os module
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Path
path = os.path.join(dir_path, "..", "userDatabase.json")

class DatabaseManager:
    def __init__(self):
        self.db = TinyDB(path)
        self.allFaces = []

    def addNewFace(self, newFace):
        self.db.insert({
            'imagePath': newFace.imagePath, 
            'full_name': newFace.full_name,
            'encoding': newFace.encoding
        })
    
    def getAllFaces(self):
        return self.db.all()
