import os
import shutil

# path where raw images are downloaded in MY COMPUTER
# USE CORRECT SOURCE DIRECTORY HERE
SOURCE_DIR = os.path.join(os.path.expanduser("~"), "Downloads", "archive", "FGNET", "images")
# path where organized images are
DEST_DIR = os.path.join("data", "raw_data", "fgnet")

def organize_fgnet():
    for filename in os.listdir(SOURCE_DIR):
        if not filename.lower().endswith(".jpg"):
            continue
        
        name = filename.split(".")[0]

        person_id = name[:3]
        age = name.split("A")[1]

        person_folder = f"person_{person_id}"
        person_path = os.path.join(DEST_DIR, person_folder)

        os.makedirs(person_path, exist_ok=True)

        new_filename = f"age_{age}.jpg"

        src_path = os.path.join(SOURCE_DIR, filename)
        dst_path = os.path.join(person_path, new_filename)

        shutil.copy(src_path, dst_path)

if __name__ == "__main__":
    organize_fgnet()