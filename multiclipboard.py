# Store multiple clips on your clipboard
import sys
import clipboard
import json


print(sys.argv)

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