import glob, os
IMG_PATH = "./data/images"

def img_validation(img):
    """
        Retorna la extensión de la foto dada, si es que es una foto válida.
    """
    parts = img.filename.split('.')
    extension =  parts[-1].lower()
    if extension in ['jpeg', 'jpg', 'bmp', 'png', 'webp']:
        return extension
    return None

def save_image(img, id):
    """
        Agrega la foto dada a la ubicación dada.
    """
    extension = img_validation(img)
    if extension is None:
        return None
    # Eliminar fotos antiguas (si es que existen)
    for file in glob.glob(id + '.*'):
        os.remove(file)
    # Guardar la nueva
    with open(f"{IMG_PATH}/{id}.{extension}", "wb+") as file_object:
        file_object.write(img.file.read())
    return extension
    