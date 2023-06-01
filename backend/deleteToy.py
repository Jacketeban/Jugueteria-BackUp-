import config.db as db
import streamlit as st

# Crear la función para eliminar juguetes de la base de datos con PyMongo


def deleteToy(name):
    # Eliminar el juguete de la base de datos
    result = db.db["juguetes"].delete_one({"nombre": name})

    # Mostrar mensaje de éxito o error
    if result.deleted_count == 1:
        st.success('El juguete se ha eliminado con éxito')
    else:
        st.error('Error al eliminar el juguete')

# Crear una función para eliminar juguetes


def InterfaceDelete():

    st.title('Eliminar juguetes')

    # Crear un input para el nombre del juguete a eliminar
    toy_name = st.text_input(
        'Nombre del juguete a eliminar', key='input_nameToy', type='default')

    # Crear un boton para eliminar el juguete
    button = st.button('Eliminar')

    if button:

        st.text('Eliminando juguete...')

        st.success(f'Juguete eliminado: {toy_name}')

        # Eliminar el juguete de la base de datos
        deleteToy(toy_name)
