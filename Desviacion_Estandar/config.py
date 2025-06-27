# Configuración de la base de datos MySQL
# Modifique los valores según su entorno
DB_USER = 'jeferson'
DB_PASSWORD = 'J3Fers0n3527*'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'desviacion_estandar_db'

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"