# File Organizer

This Python script allows you to keep your files in order and well organized in your working directory. You can use it to sort files by extension type into specific folders and also to group images into subfolders according to their creation dates.

## Requirements

Make sure you have the following Python libraries installed:

- `os`: To interact with the operating system and manage paths and files.
- `shutil`: To move files to the corresponding folders.
- PIL` (Python Imaging Library): To obtain image information, such as creation dates.
- `datetime`: To manipulate dates and times.

## How to use

1. Download the file `files_organizer.py` in the directory you want to organize.
2. Open a terminal and navigate to the directory where the file is located.
3. Run the script with Python using the following command:
4. The files will be automatically organized into folders according to their extension and the images will be grouped into subfolders according to their creation dates.

## Main Functions

### `organize_files()`.

This function examines all files in the current directory (except the script itself) and moves them to corresponding folders according to their extension. You can customize the destination folders for each extension in the script. For example, files `.docx`, `.pdf`, `.txt`, etc., will be moved to the "documents" folder.

### `delete_empty_folder(route)`.

This function searches for and removes empty folders in the provided path. It is useful for cleaning up the directory after organizing files.

### `organize_images()`.

This function organizes images into subfolders according to their creation date. Images will be grouped by years of creation in the `images` folder.

## Version History

- 1.0.0
  - The first version itself

## Notes

- Make sure the `files_organizer.py` script is in the same directory as the files you want to organize.

Enjoy a more organized working directory with this script! It is always advisable to review the code and adapt it to your specific needs before running it.
