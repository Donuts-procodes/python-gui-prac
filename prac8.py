import os 

if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("deleted")
else:
    print("file does not exist")