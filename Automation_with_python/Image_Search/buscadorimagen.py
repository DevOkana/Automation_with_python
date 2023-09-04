import os
import shutil

def procesar_carpeta(carpeta_actual, carpeta_destino):
    # Busca recursivamente en todas las subcarpetas de la carpeta actual
    for dirpath, dirnames, filenames in os.walk(carpeta_actual):
        for filename in filenames:
            if filename.endswith('.jpg', '.jpeg', '.png', '.gif', '.bmp'):
                # Copia el archivo a la carpeta de destino
                ruta_original = os.path.join(dirpath, filename)
                ruta_nueva = os.path.join(carpeta_destino, filename)
                
                try:
                    shutil.copy2(ruta_original, ruta_nueva)
                except Exception as e:
                    print(f"No se pudo copiar el archivo {ruta_original}: {str(e)}")

    # Procesa las subcarpetas de manera recursiva
    for subdir in dirnames:
        nueva_carpeta_actual = os.path.join(carpeta_actual, subdir)
        nueva_carpeta_destino = os.path.join(carpeta_destino, subdir)
        procesar_carpeta(nueva_carpeta_actual, nueva_carpeta_destino)

# Carpeta inicial a procesar
carpeta_inicial = '.'  # Puedes reemplazar '.' con la ruta absoluta de la carpeta inicial

# Carpeta de destino para almacenar las imágenes
carpeta_destino = 'imagenes_organizadas'
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Procesa la carpeta inicial
procesar_carpeta(carpeta_inicial, carpeta_destino)
