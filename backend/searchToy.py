# Importar la conexion a la base de datos
import config.db as db

# Crear una funcion para buscar juguetes en la base de datos por categoria
def searchToyCategoria(categoria):
    # Crear una lista vacia para guardar los juguetes
    toys = []

    # Buscar los juguetes en la base de datos
    toys_db = db.db["juguetes"].find({"categoria": categoria})

    # Recorrer los juguetes
    for toy in toys_db:
        # Agregar el juguete a la lista
        toys.append(toy)
    
    # Retornar la lista de juguetes
    return toys

# Crear una funcion para buscar juguetes en la base de datos por nombre
def searchToyName(name):
    # Crear una lista vacia para guardar los juguetes
    toys = []

    # Buscar los juguetes en la base de datos
    toys_db = db.db["juguetes"].find({"nombre": name})

    # Recorrer los juguetes
    for toy in toys_db:
        # Agregar el juguete a la lista
        toys.append(toy)
    
    # Retornar la lista de juguetes
    return toys