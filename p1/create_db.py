from config.db import engine, Base
from models.productos import Producto
from models.users import User

# Crea todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)