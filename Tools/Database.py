from tinydb import TinyDB, Query

# importing os module  
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Path 
path = os.path.join(dir_path, "..", "userDatabase.json")

db = TinyDB(path)