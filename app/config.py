import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class config:

    """Configuracion de la aplicacion"""

    #Dejamos el debug activado por defecto porque solo vamos a tener un entorno
    DEBUG = True

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB
    ALLOWED_EXTENSIONS = {"pdf"}