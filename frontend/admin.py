# Import streamlit
import streamlit as st

# Importar insertToy de backend/insertToy.py
from backend.insertToy import InterfaceInsert

# Importar viewToy de backend/viewToy.py
from backend.viewToy import InterfaceView


# Importar InterfaceDelete de backend/deleteToy.py
from backend.deleteToy import InterfaceDelete

# Importar InterfaceEdit de backend/updateToy.py
from backend.updateToy import InterfaceEdit

# Crear una funcion para el admin
def InterfaceAdmin():
    # Titulo
    st.title('Administrador')
    
    # Subtitulo
    st.subheader('Controlar la jugueteria JJJ')

    # Crear tabs
    tab1, tab2, tab3, tab4 = st.tabs(['Agregar juguetes', 'Eliminar juguetes', 'Actualizar juguetes', 'Ver juguetes'])

    # Si el tab seleccionado es 'Agregar juguetes'
    with tab1:
        # Insertar juguetes
        InterfaceInsert()
    
    # Si el tab seleccionado es 'Eliminar juguetes'
    with tab2:
       #Eliminar Juguete
        InterfaceDelete()
    with tab3:
        # Editar Datos Juguetes
        InterfaceEdit()

    # Si el tab seleccionado es 'Ver juguetes'
    with tab4:
        # Ver juguetes
        InterfaceView()

