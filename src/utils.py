import cv2
from pyzbar.pyzbar import decode

from src.database_mysql import get_all_users


def get_barcode(path) -> str:
    _code = 'NO LEGIBLE'
    img = decode(cv2.imread(path))
    for obj in img:
        _code = f'{obj.data}'
    return _code.replace("b", "").replace("'", "")


def actualization_message(bot):
    users = get_all_users()
    for chat_id in users:
        bot.sendMessage(
            chat_id=chat_id,
            text="¡Hola! ¡¡Este bot ha sido actualizado!! Por favor presiona en /start para obtener los cambios,"
                 " se ha añadido: "
                 "\n - Un Menu de acciones"
                 "\n - Lector de codigos de barras por fotos")