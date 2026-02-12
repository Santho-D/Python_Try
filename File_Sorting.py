import os
import shutil
base_folder = "c:/users/Student/Downloads"
# base_folder = "./Sorting_Test" # Change path if needed
file_map = {
    "Text_Documents": [".txt", ".md", ".doc", ".docx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mov"],
    "PDF_Documents": [".pdf"],
    "Excel_Sheets": [".xlsx"],
    "Zip_Files" : [".zip",".rar"],
    "Setup_Exe" : [".exe"]
}
# 1. Create all category file_map
def create_Folders(base_folder, file_map):
    for Organize_Folder_name in file_map:
        new_Organize_Folder = os.path.join(base_folder, Organize_Folder_name)
        os.makedirs(new_Organize_Folder, exist_ok=True)
        print(f"Created Organize_Folder: {new_Organize_Folder}")

# 2. Moves File
def move_files(full_path, destination):
    try:   
            shutil.move (full_path, destination)
            print(f"✅ Moved {os.path.basename(full_path)} to {destination}/")
    except Exception as e:
            print (f"❌ Something went wrong when moving file {e}")

# 3. List and organize files
def organize_files(base_folder):
    all_items = os.listdir (base_folder)  

    for item in all_items:
        stripped_item = item.strip ()
        full_path = os.path.join(base_folder, stripped_item)
        check_and_try(full_path, stripped_item)
   
# 4. Checks Type
def check_and_try (full_path, item):
    found_category = False
    
    if os.path.isfile(full_path):
        print(f"📄 File: {item}")
        name, extension = os.path.splitext(item)
        extension = extension.lower ()              
        # Check which category this file belongs to
            
        for category, extensions in file_map.items():
            if extension in extensions: 
                destination = os.path.join (base_folder, category)
                move_files(full_path, destination)
                found_category = True
                break
        if not found_category:
             print (f"⚠️ No category for {item} (extension: {extension})")
                     
    elif os.path.isdir(full_path):
            print(f"📁 Organize_Folder: {item}")
    else:
            print("❌ I dont know that Type")
    


        

create_Folders (base_folder,file_map)
organize_files (base_folder)
