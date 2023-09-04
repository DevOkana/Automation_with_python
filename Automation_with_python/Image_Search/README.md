# Image Organization Script

This Python script searches for image files in a folder and its subfolders, then copies them to a specific destination folder. The script is designed to work with images having extensions such as .jpg, .jpeg, .png, .gif and .bmp.

## Operation

The script performs the following actions:

1. it imports the `os` and `shutil` modules for file and directory handling operations.
2. Defines the `process_folder(current_folder, target_folder)` function to process files and subfolders.
   - Searches for image files in the `current_folder` and its subfolders using a `for` loop and `os.walk`.
   - Copies image files found in the `target_folder` using `shutil.copy2`.
   - Handles errors in case of problems during the copy.
   - Processes subfolders recursively.
3. Sets the `home_folder` to be processed (can be changed to an absolute path).
4. Defines the `destination_folder` where the organized images will be copied to.
5. Create the `destination_folder` if it does not exist.
6. Execute the `process_folder` function with the start folder and destination folder paths.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository or download the script file.
3. Modify the `start_folder` variable with the path of the folder you want to process.
4. Optionally, adjust the `destination_folder` variable if you want to change the destination folder.
5. Run the script in your terminal using `python script_de_organizacion.py`.

## Notes

- Make sure you have read and write permissions on the folders involved.
- The script will only copy image files with .jpg, .jpeg, .png, .gif and .bmp extensions.

---

This script makes it easy to organize your images by copying them into a neat folder structure! If you have suggestions for improvement, feel free to contribute.
