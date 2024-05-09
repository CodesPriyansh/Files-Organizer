#File Organizer: Write a script that organizes files in a directory based on their extensions.

#importing os and shutil
import os
import shutil 

#directory where files exists
directory_path = r"C:\TryFolder"

#listing all the files in the directory
files = os.listdir(directory_path)

#creating a loop to iterate each file in dir and creating a sub dir for it move in, by it's file type
for file in files:
    
    base_name, extension = os.path.splitext(file)
    
    if extension == '.pdf':
        destination_directory = r"C:\TryFolder\documents"
    elif extension == '.mkv':
        destination_directory = r"C:\TryFolder\videos"
    elif extension == '.png':
        destination_directory = r"C:\TryFolder\images"
    else:
        destination_directory = r"C:\TryFolder\exe"
    
    #creating the directory for files, if it doesn't exist.
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    #moving the files         
    source_path = os.path.join(directory_path, file)
    destination_path = os.path.join(destination_directory, file)
    shutil.move(source_path, destination_path) 










