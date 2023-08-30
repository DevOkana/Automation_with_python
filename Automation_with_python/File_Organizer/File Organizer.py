import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


# Obtener la ruta actual donde se encuentra el script
ruta_actual = os.getcwd()


def organizar_archivos():
    # Obtener la lista de archivos en la ruta actual
    archivos = os.listdir(ruta_actual)

    for archivo in archivos:
        # Comprobar si es un archivo y no es el archivo Python en sí mismo
        if os.path.isfile(archivo) and archivo != os.path.basename(__file__):
            # Obtener la extensión del archivo
            extension = os.path.splitext(archivo)[1].lower()

            # Crear una carpeta si no existe según la extensión del archivo
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
                    carpeta_destino = os.path.join(ruta_actual, "documentos")
                elif extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
                    carpeta_destino = os.path.join(ruta_actual, "imagenes")
                elif extension in [".zip", ".rar", ".7z", ".tar", ".gz"]:
                    carpeta_destino = os.path.join(ruta_actual, "comprimido")
                elif extension in [".mp3", ".wav", ".flac", ".aac", ".ogg"]:
                    carpeta_destina = os.path.join(ruta_actual, "musica")
                elif extension in [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"]:
                    carpeta_destino = os.path.join(ruta_actual, "videos")
                elif extension in [".exe", ".msi"]:
                    carpeta_destino = os.path.join(ruta_actual, "aplicaciones")
                elif extension in [".py"]:
                    carpeta_destino = os.path.join(ruta_actual, "python")
                elif extension in [".java"]:
                    carpeta_destino = os.path.join(ruta_actual, "java")
                elif extension in [".cpp"]:
                    carpeta_destino = os.path.join(ruta_actual, "cpp")
                elif extension in [".c"]:
                    carpeta_destino = os.path.join(ruta_actual, "c")
                elif extension in [".cs"]:
                    carpeta_destino = os.path.join(ruta_actual, "csharp")
                elif extension in [".php"]:
                    carpeta_destino = os.path.join(ruta_actual, "php")
                elif extension in [".html"]:
                    carpeta_destino = os.path.join(ruta_actual, "html")
                elif extension in [".css"]:
                    carpeta_destino = os.path.join(ruta_actual, "css")
                elif extension in [".js"]:
                    carpeta_destino = os.path.join(ruta_actual, "javascript")
                elif extension in [".rb"]:
                    carpeta_destino = os.path.join(ruta_actual, "ruby")
                elif extension in [".pl"]:
                    carpeta_destino = os.path.join(ruta_actual, "perl")
                elif extension in [".swift"]:
                    carpeta_destino = os.path.join(ruta_actual, "swift")
                elif extension in [".go"]:
                    carpeta_destino = os.path.join(ruta_actual, "go")
                elif extension in [".ts"]:
                    carpeta_destino = os.path.join(ruta_actual, "typescript")
                elif extension in [".lua"]:
                    carpeta_destino = os.path.join(ruta_actual, "lua")
                elif extension in [".r"]:
                    carpeta_destino = os.path.join(ruta_actual, "r")
                elif extension in [".scala"]:
                    carpeta_destino = os.path.join(ruta_actual, "scala")
                elif extension in [".vb"]:
                    carpeta_destino = os.path.join(ruta_actual, "visualbasic")
                elif extension in [".asm"]:
                    carpeta_destino = os.path.join(ruta_actual, "ensamblador")
                else:
                    carpeta_destino = os.path.join(ruta_actual, extension[1:])

                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)

                try:
                    # Mover el archivo a la carpeta correspondiente
                    shutil.move(archivo, carpeta_destino)
                except shutil.Error:
                    print(
                        "El archivo {0} ya esta copiado dentro de la carpeta {1}".format(
                            archivo, carpeta_destino
                        )
                    )

    print("Organización de archivos completada.")


def eliminar_carpetas_vacias(ruta):
    for carpeta in os.listdir(ruta):
        ruta_carpeta = os.path.join(ruta, carpeta)
        if os.path.isdir(ruta_carpeta):
            if not os.listdir(ruta_carpeta):
                os.rmdir(ruta_carpeta)
                print(f"Carpeta vacía {carpeta} eliminada.")
            else:
                eliminar_carpetas_vacias(ruta_carpeta)


def obtener_fecha_creacion_imagen(archivo):
    try:
        imagen = Image.open(archivo)
        # Obtener la fecha de modificación del archivo
        fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(archivo)).date()
        return str(fecha_modificacion.year)

    except (IOError, AttributeError):
        pass

    return None


def organizar_imagenes():
    # Obtener la ruta actual donde se encuentra el script
    ruta_actual = os.getcwd()

    # Obtener la ruta de la carpeta "imagenes"
    carpeta_imagenes = os.path.join(ruta_actual, "imagenes")

    # Obtener la lista de archivos de imagen en la carpeta "imagenes"
    archivos_imagenes = os.listdir(carpeta_imagenes)

    for archivo_imagen in archivos_imagenes:
        ruta_imagen = os.path.join(carpeta_imagenes, archivo_imagen)

        # Obtener el año de creación de la imagen
        fecha_creacion = obtener_fecha_creacion_imagen(ruta_imagen)

        if fecha_creacion:
            carpeta_destino = os.path.join(carpeta_imagenes, fecha_creacion)

            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            # Mover la imagen a la carpeta correspondiente según el año de creación
            shutil.move(ruta_imagen, carpeta_destino)
            print(
                f"Imagen {archivo_imagen} movida a la carpeta {os.path.basename(carpeta_destino)}."
            )

if __name__ == '__main__':
    try: 
        # Ejemplo de uso
        organizar_imagenes()
    except: 
        None
    # Ejemplo de uso
    eliminar_carpetas_vacias(ruta_actual)
    organizar_archivos()

    input("Presiona Enter para continuar...")
