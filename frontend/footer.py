# Import streamlit
import streamlit as st
# Importar base64
import base64

# Crear una funcion para el footer
def Footer():
    with open("public/footerlogo.gif", "rb") as file:
        img = file.read()
        b64_img = base64.b64encode(img).decode()

        footer = f"""
        <div style='text-align: center;'>
            <hr>
            <p><strong>Redes sociales</strong></p>
            <a href='https://github.com'><img src='https://img.shields.io/badge/Github-100000?style=for-the-badge&logo=github&logoColor=white'></a>
            <a href='https://facebook.com'><img src='https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white'></a>
            <hr>
            <img src='data:image/gif;base64,{b64_img}' alt='logo'>
            <hr>
            <p>Desarrollado por <a href='https://www.youtube.com/watch?v=mCdA4bJAGGk'>JUGUETERIAJJJ</a></p>
        </div>
        """
        # Imprimir el footer
        st.markdown(footer, unsafe_allow_html=True)

# Crear una funcion para el footer
def InterfaceFooter():
    # Call the function Footer
    Footer()

