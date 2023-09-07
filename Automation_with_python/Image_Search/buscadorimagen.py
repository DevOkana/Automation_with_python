import os
import shutil


def process_folder(current_folder, destination_folder):
    # Recursively searches all subfolders of the current folder
    for dirpath, dirnames, filenames in os.walk(current_folder):
        for filename in filenames:
            if filename.endswith(".jpg", ".jpeg", ".png", ".gif", ".bmp"):
                # Copy the file to the destination folder
                path_origin = os.path.join(dirpath, filename)
                path_new = os.path.join(destination_folder, filename)

                try:
                    shutil.copy2(path_origin, path_new)
                except Exception as e:
                    print(f"Unable to copy file  {path_origin}: {str(e)}")

    # Processes the subfolders recursively
    for subdir in dirnames:
        new_current_folder = os.path.join(current_folder, subdir)
        new_destination_folder = os.path.join(destination_folder, subdir)
        process_folder(new_current_folder, new_destination_folder)


# Start folder to process
folder_initial = (
    "."  # You can replace '.' with the absolute path of the initial folder.
)

# Destination folder to store images
destination_folder = "images_organized"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

#  Process the initial folder
process_folder(folder_initial, destination_folder)
