import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load

# Ruta al modelo
MODEL_PATH = "./modelo/model.pkl"

# Cargar el modelo
@st.cache_resource
def load_model():
    model = load(MODEL_PATH)
    if not hasattr(model, "predict"):
        raise ValueError("El archivo cargado no es un modelo válido.")
    return model

model = load_model()

# Título de la aplicación
st.title("Predicción de Transacciones Totales Mensuales")
st.subheader("Ingrese los datos para la predicción:")

# Crear columnas
col1, col2 = st.columns([2, 1])  # Proporción de ancho: col1 = 2, col2 = 1

# Entradas del usuario en la columna izquierda
with col1:
    # Mes
    months = {
        "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6,
        "Julio": 7, "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
    }
    selected_month = st.selectbox("Seleccionar mes:", list(months.keys()))
    month = months[selected_month]

    # Año
    year = st.number_input("Año:", min_value=2020, max_value=2030, step=1)

    # Local
    local = st.selectbox(
        "Seleccionar local:",
        ["store_location_hell's kitchen", "store_location_lower manhattan"]
    )

# Imagen del local en la columna derecha
with col2:
    # Agregar contenedor con estilo CSS para centrar la imagen verticalmente
    st.markdown(
        """
        <style>
        .vertical-center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="vertical-center">', unsafe_allow_html=True)
    if local == "store_location_hell's kitchen":
        st.image("./img/hell's kitchen.jpg", caption="Hell's Kitchen", use_container_width=True)
    elif local == "store_location_lower manhattan":
        st.image("./img/lower manhatan.jpg", caption="Lower Manhattan", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Botón de predicción debajo de las columnas
st.markdown("---")  # Línea separadora para estética

if st.button("Predecir"):
    # Convertir el local a formato binario
    local_hells_kitchen = 1 if local == "store_location_hell's kitchen" else 0
    local_lower_manhattan = 1 if local == "store_location_lower manhattan" else 0

    # Crear el DataFrame con los datos de entrada
    input_data = pd.DataFrame(
        [[month, year, local_hells_kitchen, local_lower_manhattan]],
        columns=["month", "year", "store_location_hell's kitchen", "store_location_lower manhattan"]
    )

    # Realizar la predicción
    prediction = model.predict(input_data)[0]

    # Mostrar el resultado con estilo
    st.markdown(f"""
        <div style="text-align: center; padding: 20px; border: 2px solid #4CAF50; border-radius: 10px; background-color: #f9f9f9;">
            <h2>Transacciones Totales Predichas</h2>
            <p style="font-size: 32px; color: #4CAF50;"><strong>{prediction:,.2f}</strong></p>
        </div>
        """, unsafe_allow_html=True)
