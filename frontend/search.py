# Importamos streamlit
import streamlit as st

# Importar buscar juguetes de backend/searchToy.py
from backend.searchToy import searchToyName

# Crear una funcion para presentar el juguete
def CardToy(juguete):
    row = st.columns([1, 1, 1, 1, 1])
    row[0].image(juguete['imagen'], width=200)
    st.write(f"<h1 style='color: #9B0707'>{juguete['nombre']}</h1>", unsafe_allow_html=True)
    st.write(f"<h3>Edad recomendada: {juguete['edad_recomendada']}</h3>", unsafe_allow_html=True)
    st.write(f"<p>{juguete['descripcion']}</p>", unsafe_allow_html=True)
    st.write(f"Precio: {juguete['precio']}")
    st.write(f"Stock: {juguete['stock']}")
    st.write(f"Marca: {juguete['marca']}")
    st.write(f"Categoria: {juguete['categoria']}")
    st.divider()


# Creamos una funcion para buscar juguete por nombre y presentarlo
def searchToyNameCard(name):
    # Buscar el juguete en la base de datos
    toy = searchToyName(name)

    # Si no se encontro el juguete
    if toy == None:
        # Texto
        st.text('No se encontro el juguete')
    # Si se encontro el juguete
    else:
        # Mostar el juguete en una carta
        for juguete in toy:
            CardToy(juguete)


# Creamos una funcion para buscar juguetes
def InterfaceSearch():
    # Crear un input para buscar juguetes
    search = st.text_input(' ',placeholder='Buscar por nombre juguete', label_visibility='hidden', key='input_search', type='default')

    # Boton para buscar juguetes
    button = st.button('Buscar')

    # Si el boton es presionado
    if button:
        # Texto
        st.text('Buscando juguetes...')
        # Texto
        st.success(f'Buscando juguetes: {search}')

        # Buscar juguetes por nombre y presentarlos
        searchToyNameCard(search)
  
