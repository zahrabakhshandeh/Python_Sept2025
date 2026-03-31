import os 
import shutil

def find_files(path):
    files_name = []
    for root, dirs, files in os.walk(path):
        for f in files:
            full_path = os.path.join(root, f)
            files_name.append(full_path)
    return files_name       

#folder_py
#folder_txt
def find_file_ext(files):
    exts = set()
    for f in files:
        ext = f.split(".")
        exts.add(ext[-1])
    return exts


def create_dir(main_path, folders):
    for folder_name in folders.keys():
        new_path = os.path.join(main_path, folder_name)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            print(f"{folder_name} created!")


def organize_files(main_path, files, folders):
    for file_path in files:
        ext = file_path.split(".")[-1]
        folder_name = "Other_Files"
        ext = "." + ext
        for folder, exts in folders.items():
            if ext in exts:
                folder_name = folder 
                break
        file_name = os.path.basename(file_path)
        new_path = os.path.join(main_path, folder_name)
        new_path = os.path.join(new_path, file_name)
        shutil.move(file_path, new_path)


MEDICAL_CATEGORIES = {
    "Articles_and_Books": ['.pdf'],
    "Presentations": ['.pptx', '.ppt'],
    "Medical_Images": ['.jpg', '.jpeg', '.png'],
    "Educational_Videos": ['.mp4', '.avi', '.mkv', '.mov'],
    "Notes": ['.docx', '.doc', '.txt', '.odt'],
    "Lab_Data": ['.xlsx', '.xls', '.csv'],
    "Compressed_Files": ['.zip', '.rar', '.7z'],
    "Other_Files": []  
}

# step1
main_path = "/home/zahra/Desktop/Example"

# step2
if not os.path.exists(main_path):
    print("path not found!")
else:
    print("Starting...")
    all_files = find_files(main_path)
    #find_file_ext(all_files)
    create_dir(main_path, MEDICAL_CATEGORIES)

    organize_files(main_path, all_files, MEDICAL_CATEGORIES)


    