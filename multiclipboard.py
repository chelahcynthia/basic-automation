# Store multiple clips on your clipboard
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

# create json
def save_items(filepath, data):
   with open(filepath, "w") as f:
      json.dump(data, f)
      
# function to load json file
def load_items(filepath):
   with open(filepath, "r") as f:
      data = json.load(f)
      return data

      
   
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)
    
    if command == "save":
       key = input("Enter a key: ")
       data[key] = clipboard.paste()
       save_items(SAVED_DATA, data)
    elif command == "load":
       print("load")
    elif command == "list":
        print("Unknown command")
else:
    print("Please pass exactly one command")