import glob, os

from requests import Session
from schemas import Item
import models

IMG_PATH = "./data/images"

def img_validation(img) -> str | None:
    """
        Retorna la extensión de la foto dada, si es que es una foto válida.
    """
    parts = img.filename.split('.')
    extension =  parts[-1].lower()
    if extension in ['jpeg', 'jpg', 'bmp', 'png', 'webp']:
        return extension
    return None

def save_image(img, id, extension):
    """
        Agrega la foto dada a la ubicación dada.
    """
    # Eliminar fotos antiguas (si es que existen)
    for file in glob.glob(str(id) + '.*'):
        os.remove(file)
    # Guardar la foto
    with open(f"{IMG_PATH}/{id}.{extension}", "wb+") as file_object:
        file_object.write(img.file.read())

def read_image(id, extension):
    """
        Lee la foto con el id dado.
    """
    with open(f"{IMG_PATH}/{id}.{extension}", "rb") as file_object:
        return file_object.read()

def create_item(db: Session, item: Item):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
    