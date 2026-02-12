import os
import platform
import shutil

file_map = {
    "Text_Documents": [".txt", ".md", ".doc", ".docx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mov"],
    "PDF_Documents": [".pdf"],
    "Excel_Sheets": [".xlsx"],
    "Zip_Files": [".zip", ".rar"],
    "Setup_Exe": [".exe"],
    "Projects": [".py"],
    "ISO_files": [".iso"],
}

base_folder = ""

if platform.system() == "Windows":
    base_folder = "c:/users/Student/Downloads"
elif platform.system() == "Linux":
    base_folder = os.path.expanduser("~/Downloads/")

# 2. Moves File
def move_files(full_path, destination):
    try:
        folder_existed = os.path.exists(destination)
        os.makedirs (destination, exist_ok=True)
        
        if not folder_existed:
            print(f"Created new Folder: {destination}")
        
        shutil.move(full_path, destination)
        print(f"✅ Moved {os.path.basename(full_path)} to {destination}/")
    
    except Exception as e:
        print(f"❌ Something went wrong when moving file {e}")


# 3. List and organize files
def organize_files(base_folder):
    all_items = os.listdir(base_folder)
    for item in all_items:
        full_path = os.path.join(base_folder, item)
        check_and_try(full_path, item)


# 4. Checks Type
def check_and_try(full_path, item):
    found_category = False

    if os.path.isfile(full_path):
        print(f"📄 File: {item}")
        name, extension = os.path.splitext(item)
        extension = extension.lower()
        # Check which category this file belongs to

        for category, extensions in file_map.items():
            if extension in extensions:
                destination = os.path.join(base_folder, category)
                move_files(full_path, destination)
                found_category = True
                break
        if not found_category:
            print(f"⚠️ No category for {item} (extension: {extension})")

    elif os.path.isdir(full_path):
        print(f"📁 Organize_Folder: {item}")
    else:
        print("❌ I dont know that Type")

organize_files(base_folder)
