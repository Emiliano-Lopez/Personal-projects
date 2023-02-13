import os
import shutil


current_dir = os.getcwd()

folders= {
        "documents":[".txt", ".doc", ".docx", ".pdf", ".xlm", ".csv", ".xls", ".xlsx", ".ppt", 
            ".pptx",".oxps", ".epub", ".pages", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", 
            ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd"],
        "images":[".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
            ".heif", ".psd"],
        "audio":[".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
            ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
        "videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
            ".qt", ".mpg", ".mpeg", ".3gp"],
        "rar":[".zip",".rar",".7z"],
        "PYTHON": [".py","ipynb"],
        "school":["school"],
        "trash":["trash"],

}

def create_folder():

    if os.path.exists("others") == True:
        pass
    else:
        os.mkdir("others")

    for name in folders.keys():
        if os.path.exists(name) == True:
            pass
        else:
            os.mkdir(name)


def move_file(current_dir):
    for file in os.listdir(current_dir):
        filename, file_ext = os.path.splitext(file)

        try:
            
            if not file_ext or filename =="organize_files" :
                pass

            elif "trash" in filename :
                    shutil.move(
                        os.path.join(current_dir, f"{filename}{file_ext}"),
                        os.path.join(current_dir, "trash",f"{filename}{file_ext}")
                )
            elif "school" in filename :
                    shutil.move(
                        os.path.join(current_dir, f"{filename}{file_ext}"),
                        os.path.join(current_dir, "school",f"{filename}{file_ext}")
                )
            
            for key in folders.keys():                
                if file_ext in folders[key]:
                    shutil.move(
                        os.path.join(current_dir, f"{filename}{file_ext}"),
                        os.path.join(current_dir, key,f"{filename}{file_ext}")
                    )

        except (FileNotFoundError,PermissionError):
            pass
            


def move_other(current_dir):
    for file in os.listdir(current_dir):
        filename, file_ext = os.path.splitext(file)
        try:
            if not file_ext :
                pass
            elif filename=="organize_files":
                pass
            else:
                shutil.move(
                        os.path.join(current_dir, f"{filename}{file_ext}"),
                        os.path.join(current_dir, "others",f"{filename}{file_ext}")
                )
        except (FileNotFoundError,PermissionError):
            pass

create_folder()
move_file(current_dir)
move_other(current_dir)