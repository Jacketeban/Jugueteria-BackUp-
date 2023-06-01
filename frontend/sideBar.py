# Import streamlit
import streamlit as st
# Importar toysJJJ
import frontend.toysStore as InterfaceHome
# Importar admin
import frontend.admin as InterfaceAdmin

# Crear una funcion para el side bar
def SideBar():
    # Cargar el archivo del gif 
    file = open("public/logosiderbard.gif", "rb")
    # Cargar una gif en el side bar
    st.sidebar.image(file.read(), width=300)

    # Cargar el archivo del md
    file = open("public/logolado.jpg", "rb")
    # Cargar una imagen en el side bar
    st.sidebar.image(file.read(), width=300)

    # Crear un subtitulo para el side bar
    st.sidebar.subheader('Menú')

    # Agregar opciones al sidebar
    option = st.sidebar.selectbox(
        'Seleccione una opción:',
        ('Jugueteria', 'Administrador')
    )

    # Si la opción seleccionada es 'Jugueteria'
    if option == 'Jugueteria':
        # Call the function InterfaceHome
        InterfaceHome.InterfaceHome()

    # Si la opción seleccionada es 'Administrador'
    elif option == 'Administrador':
        # Call the function InterfaceAdmin
        InterfaceAdmin.InterfaceAdmin()