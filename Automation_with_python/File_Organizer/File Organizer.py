import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


# Get the current path where the script is located
current_path = os.getcwd()


def organize_files():
    # Get the list of files in the current path
    files = os.listdir(current_path)

    for file in files:
        # Check if it is a file and it is not the Python file itself
        if os.path.isfile(file) and file != os.path.basename(__file__):
            # Get file extension
            extension = os.path.splitext(file)[1].lower()

            # Create a folder if it does not exist according to the file extension
            if extension:
                if extension in [
                    ".doc",
                    ".docx",
                    ".txt",
                    ".pdf",
                    ".rtf",
                    ".odt",
                    ".xls",
                    ".xlsx",
                    ".csv",
                    ".ppt",
                    ".pptx",
                    ".odp",
                ]:
                    destination_folder = os.path.join(current_path, "documents")
                elif extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
                    destination_folder = os.path.join(current_path, "images")
                elif extension in [".zip", ".rar", ".7z", ".tar", ".gz"]:
                    destination_folder = os.path.join(current_path, "compressed")
                elif extension in [".mp3", ".wav", ".flac", ".aac", ".ogg"]:
                    folder_destina = os.path.join(current_path, "music")
                elif extension in [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"]:
                    destination_folder = os.path.join(current_path, "movies")
                elif extension in [".exe", ".msi"]:
                    destination_folder = os.path.join(current_path, "app")
                elif extension in [".py"]:
                    destination_folder = os.path.join(current_path, "python")
                elif extension in [".java"]:
                    destination_folder = os.path.join(current_path, "java")
                elif extension in [".cpp"]:
                    destination_folder = os.path.join(current_path, "cpp")
                elif extension in [".c"]:
                    destination_folder = os.path.join(current_path, "c")
                elif extension in [".cs"]:
                    destination_folder = os.path.join(current_path, "csharp")
                elif extension in [".php"]:
                    destination_folder = os.path.join(current_path, "php")
                elif extension in [".html"]:
                    destination_folder = os.path.join(current_path, "html")
                elif extension in [".css"]:
                    destination_folder = os.path.join(current_path, "css")
                elif extension in [".js"]:
                    destination_folder = os.path.join(current_path, "javascript")
                elif extension in [".rb"]:
                    destination_folder = os.path.join(current_path, "ruby")
                elif extension in [".pl"]:
                    destination_folder = os.path.join(current_path, "perl")
                elif extension in [".swift"]:
                    destination_folder = os.path.join(current_path, "swift")
                elif extension in [".go"]:
                    destination_folder = os.path.join(current_path, "go")
                elif extension in [".ts"]:
                    destination_folder = os.path.join(current_path, "typescript")
                elif extension in [".lua"]:
                    destination_folder = os.path.join(current_path, "lua")
                elif extension in [".r"]:
                    destination_folder = os.path.join(current_path, "r")
                elif extension in [".scala"]:
                    destination_folder = os.path.join(current_path, "scala")
                elif extension in [".vb"]:
                    destination_folder = os.path.join(current_path, "visualbasic")
                elif extension in [".asm"]:
                    destination_folder = os.path.join(current_path, "ensamblador")
                else:
                    destination_folder = os.path.join(current_path, extension[1:])

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                try:
                    # Move the file to the corresponding folder
                    shutil.move(file, destination_folder)
                except shutil.Error:
                    print(
                        "The file {0} is already copied into the folder {1}".format(
                            file, destination_folder
                        )
                    )

    print("File organization completed.")


def delete_empty_folder(route):
    for folder in os.listdir(route):
        route_folder = os.path.join(route, folder)
        if os.path.isdir(route_folder):
            if not os.listdir(route_folder):
                os.rmdir(route_folder)
                print(f"Folder is empty {folder} and has been removed.")
            else:
                delete_empty_folder(route_folder)


def get_creation_date_image(file):
    try:
        imagen = Image.open(file)
        # Get the file modification date
        date_modification = datetime.fromtimestamp(os.path.getmtime(file)).date()
        return str(date_modification.year)

    except (IOError, AttributeError):
        pass

    return None


def organize_images():
    # Get the current route where the script is located
    current_path = os.getcwd()

    # Obtain the path to the "images" folder
    image_folder = os.path.join(current_path, "images")

    # Get the list of image files in the folder "images".
    image_files = os.listdir(image_folder)

    for image_file in image_files:
        path_image = os.path.join(image_folder, image_file)

        # Obtener el año de creación de la imagen
        creation_date = get_creation_date_image(path_image)

        if creation_date:
            destination_folder = os.path.join(image_folder, creation_date)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the imagen to the corresponding folder according to the creation year
            shutil.move(path_image, destination_folder)
            print(
                f"Imagen {image_file} move to the folder {os.path.basename(destination_folder)}."
            )


if __name__ == "__main__":
    try:
        organize_images()
    except:
        None
    delete_empty_folder(current_path)
    organize_files()

    input("Press enter for continue")
