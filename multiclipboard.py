# Store multiple clips on your clipboard
import sys
import clipboard
import json

# create json
def save_items(filepath, data):
   with open(filepath, "w") as f:
      json.dump(data, f)
      
# function to read json file
def load_json(filepath):
   with open(filepath, "r") as f:
      data = json.load(f)

      
   
if len(sys.argv) == 2:
    command = sys.argv[1]
    
    if command == "save":
       print("save")
    elif command == "load":
       print("load")
    elif command == "list":
        print("Unknown command")
else:
    print("Please pass exactly one command")