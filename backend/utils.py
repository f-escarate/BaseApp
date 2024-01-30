import glob, os

from requests import Session
from schemas import Item
import models

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

def save_image(img, id) -> str:
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

def create_item(db: Session, item: Item):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
    