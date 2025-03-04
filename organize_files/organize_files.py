import os
import shutil

# Get all files in the current directory (excluding directories)
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Loop through each file
for file in files:
    # Get the file name without extension
    folder_name = os.path.splitext(file)[0]

    # Create a folder with the same name as the file (without extension)
    os.makedirs(folder_name, exist_ok=True)

    # Move the file into the newly created folder
    shutil.move(file, os.path.join(folder_name, file))

print("All files have been moved into their respective folders.")
