import os
import shutil

# Folder to organize
folder_path = "Test_Folder"

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"],
    "Excel Files": [".xls", ".xlsx"],
    "Python Files": [".py"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar"]
}


def organize_files():
    print("=" * 45)
    print("        FILE ORGANIZER")
    print("=" * 45)

    if not os.path.exists(folder_path):
        print(f"\nFolder '{folder_path}' does not exist.")
        return

    files = os.listdir(folder_path)

    moved_files = 0

    for file in files:

        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        filename, extension = os.path.splitext(file)

        extension = extension.lower()

        moved = False

        for folder_name, extensions in file_types.items():

            if extension in extensions:

                destination_folder = os.path.join(folder_path, folder_name)

                os.makedirs(destination_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, file)
                )

                print(f"Moved: {file}  --->  {folder_name}")

                moved = True
                moved_files += 1
                break

        if not moved:

            other_folder = os.path.join(folder_path, "Others")

            os.makedirs(other_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(other_folder, file)
            )

            print(f"Moved: {file}  --->  Others")

            moved_files += 1

    print("\n--------------------------------")
    print(f"Total files organized: {moved_files}")
    print("Organization Completed Successfully!")
    print("--------------------------------")


organize_files()