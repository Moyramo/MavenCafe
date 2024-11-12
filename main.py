import streamlit as st

# Título de la aplicación
st.title("Aplicación Sencilla de Streamlit")

# Sección de entrada de datos
st.header("Introduce tus datos")
nombre = st.text_input("Nombre:")
edad = st.number_input("Edad:", min_value=0)

# Botón para mostrar el mensaje
if st.button("Mostrar mensaje"):
    if nombre:
        st.success(f"¡Hola, {nombre}! Tienes {edad} años.")
    else:
        st.warning("Por favor, introduce tu nombre.")
