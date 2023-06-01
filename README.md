###
```
Deploy página web: https://hacksjuandavid-jugueteriajjj-app-kscgsj.streamlit.app

```
#[Deploy página JugueteriaJJJ](https://hacksjuandavid-jugueteriajjj-app-kscgsj.streamlit.app)

###
###
Instalar streamlit
```
pip install streamlit
```
Instalar virtualenv
```
pip install virtualenv
```
Instalar pymongo
```
pip install pymongo
```
###
Crear un entorno virtual solo sino existe
```
virtualenv env
```
###

Activar el entorno virtual
```
source env/bin/activate
```
###

Desactivar el entorno virtual
```
deactivate
```
###
Instalar las librerias
```
pip install -r requirements.txt
```
###
Crear un archivo requirements.txt
```
pip freeze > requirements.txt
```
###
Ejecutar el programa
```
streamlit run app.py
```
```
JugueteriaJJJ/
├── .streamlit/
│   ├── config.toml
├── backend/
│   ├── deleteToy.py
│   ├── insertToy.py
│   ├── searchToy.py
│   ├── updateToy.py
│   └── viewToy.py
├── frontend/
│   ├── admin.py
│   ├── footer.py
│   ├── header.py
│   ├── sideBar.py
│   └── toysStore.py
├── config/
│   ├── db.py
├── public/
│   ├── images/
|   |  ├── logo.png
|   |  ├── logo2.png
|   |  ├── logo3.png
|   |  ├── logo4.png
├── .gitignore
├── app.py
├── commands.md
├── README.md
└── requirements.txt
```
###
