import os

dir_path = os.path.abspath(os.getcwd())

def fileMode(submode):
    
    
    pass
    

def folderMode(submode):
    
    try:

        with open(".grepignore", "r") as ignorefile:
            
            ignorelist = ignorefile.read().split("\n")
            
    except FileNotFoundError:
        
        ignorelist = []

    files = []

    for (dir_path, dir_names, file_names) in os.walk("."):
        
        for file in file_names:
            
            filepath = f"{dir_path}/{file}"
            
            truename = filepath[2::]
            
            if ignorelist.count(truename):
                
                continue
            
            files.append(filepath)
            
            
    print(files)
    
    
def rootMode(submode):
    
    pass

    

print(f"Current Path: {dir_path}")
print()
print("MODES")
print("1. File")
print("2. Folder")
print("3. Root")

mode = input("Enter a mode: ")

print()
print("SUBMODES")


print("1. Find in file")
print("2. Replace in file")

if mode != "1":
    
    print("3. Find in file name")
    

submode = input("Enter a submode: ")


if mode == "1":
    
    fileMode(submode)
    

if mode == "2":
    
    folderMode(submode)
    
    
if mode == "3":
    
    rootMode(submode)
    
