# Importar streamlit
import pandas as pd
import streamlit as st
# Importar la conexion a la base de datos
import config.db as db

# Crear una funcion para traer los juguetes de la base de datos
def getToys():
    # Crear una lista vacia para guardar los juguetes
    toys = []

    # Buscar los juguetes en la base de datos
    toys_db = db.db["juguetes"].find()

    # Recorrer los juguetes
    for toy in toys_db:
        # Agregar el juguete a la lista
        toys.append(toy)
    
    # Retornar la lista de juguetes
    return toys

# Crear una funcion para traer los juguetes
def InterfaceView():
    # Titulo
    st.title('Ver juguetes')

    # Crear un dataframe con los juguetes
    toys = getToys()
    df = pd.DataFrame(toys)

    # Mostrar el dataframe
    st.dataframe(df)

