import os
import shutil

folder = "./Sorting_Test"
file_map = {
    "Text_Documents": [".txt", ".md", ".doc"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mov"]
}

# 1. Create all category file_map
for folder_name in file_map:
    new_folder = os.path.join(folder, folder_name)
    os.makedirs(new_folder, exist_ok=True)
    print(f"Created folder: {new_folder}")

# 2. List and organize files

all_items = os.listdir (folder)  # Change path if needed

for item in all_items:
    full_path = os.path.join(folder, item)
    
    if os.path.isfile(full_path):
        print(f"📄 File: {item}")
        name, extension = os.path.splitext(item)
        extension = extension.lower ()              
         
        # Check which category this file belongs to
        for category, extensions in file_map.items():
            if extension in extensions:
                destination = os.path.join (folder, category)
                shutil.move (item, destination)
                print(f"✅ Moved {item} to {category}/")
                break  # Stop checking once we've moved it
    
    elif os.path.isdir(full_path):
        print(f"📁 Folder: {item}")
