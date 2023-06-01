# Importar la conexion a la base de datos
import config.db as db

# Importar streamlit
import streamlit as st

# Importar time 
import time

# Crear la funcion para insertar juguetes a la base de datos con pymongo
def insertToy(name, edad_recomendada, descripcion, imagen, precio, stock, marca, categoria):
    # Crear el diccionario con los datos del juguete
    toy = {
        "nombre": name,
        "edad_recomendada": edad_recomendada,
        "descripcion": descripcion,
        "imagen": imagen,
        "precio": precio,
        "stock": stock,
        "marca": marca,
        "categoria": categoria
    }

    # Insertar el juguete en la base de datos
    db.db["juguetes"].insert_one(toy)

    # Mostrar mensaje de exito
    st.success('El juguete se ha agregado con exito')

# Crear una funcion para insertar juguetes
def InterfaceInsert():
    # Titulo
    st.title('Agregar juguetes')

    try:
        # Crear un input para nombre y edad recomendada del juguete en una misma linea
        name, edad_recomendada = st.columns(2)
        name = name.text_input('Nombre', key='input_name', type='default')
        edad_recomendada = edad_recomendada.text_input('Edad recomendada', key='input_edad_recomendada', type='default')

        # Crear un input para la descripcion y la imagen del juguete
        descripcion = st.text_area('Descripcion', key='input_descripcion')
        imagen = st.text_input('Imagen', key='input_imagen', type='default')

        # Crear un input para el precio, stock y marca del juguete en una misma linea
        precio, stock, marca = st.columns(3)
        precio = precio.text_input('Precio', key='input_precio', type='default')
        stock = stock.text_input('Stock', key='input_stock', type='default')
        marca = marca.text_input('Marca', key='input_marca', type='default')

        # Crear un select para la categoria
        categoria = st.selectbox('Categoria', ['Niñas', 'Niños', 'Didacticos'])

    except:
        st.error("Todos los campos deben estar llenos")

    # Crear un boton para agregar el juguete
    button = st.button('Agregar')

    # Si el boton es presionado
    if button:
        # Texto
        st.text('Agregando juguete...')
        # Texto de carga
        with st.spinner('Actualizando datos del juguete...'):
            time.sleep(1)
        # Si edad recomendada, precio o stock no son numeros
        if not edad_recomendada.isnumeric():
            # Mostrar mensaje de error
            st.error('La edad recomendada debe ser un numero')
        elif not precio.isnumeric():
                st.error('El precio debe ser un numero')
        elif not stock.isnumeric():
                st.error('El stock debe ser un numero')
        # Si no validar que todos los campos esten llenos
        elif name == '' or edad_recomendada == '' or descripcion == '' or imagen == '' or precio == '' or stock == '' or marca == '':
            # Mostrar mensaje de error
            st.error('Todos los campos son requeridos')
        # Si todos los campos estan llenos
        else:
            # Insertar el juguete en la base de datos
            insertToy(name, edad_recomendada, descripcion, imagen, precio, stock, marca, categoria)
            # Texto de exito
            st.success(f'Juguete agregado con exito:{name}')