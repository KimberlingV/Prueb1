
import streamlit as st

# --- Usuarios permitidos ---
USERS = {
    "usuario1": "clave123",
    "usuario2": "segura456"
}

# --- Función de login ---
def login():
    st.title("Login")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if USERS.get(username) == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
        else:
            st.error("Usuario o contraseña incorrectos")

# --- App principal ---
def main_app():
    st.title("Dashboard Interactivo")
    st.success(f"Bienvenido, {st.session_state['username']}!")

    st.sidebar.header("Filtros")
    opcion = st.sidebar.selectbox("Selecciona una opción:", ["Ventas", "Clientes", "Mapa"])

    if opcion == "Ventas":
        st.subheader("Gráfico de ventas")
        st.line_chart([100, 200, 150, 300, 250])

    elif opcion == "Clientes":
        st.subheader("Tabla de clientes")
        st.dataframe({"Nombre": ["Ana", "Luis", "Carla"], "Compras": [5, 2, 7]})

    elif opcion == "Mapa":
        st.subheader("Mapa")
        st.map({
            "lat": [ -1.25, -1.27 ],
            "lon": [ -78.6, -78.65 ]
        })

# --- Control de sesión ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    main_app()
else:
    login()
