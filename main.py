import streamlit as st
import pandas as pd
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
st.title("Predicción de Transacciones Mensuales")

# Entradas del usuario
st.subheader("Ingrese los datos para la predicción:")

month = st.number_input("Mes (1-12):", min_value=1, max_value=12, step=1)
year = st.number_input("Año:", min_value=2020, max_value=2030, step=1)
local = st.selectbox(
    "Seleccionar local:",
    ["store_location_hell's kitchen", "store_location_lower manhattan"]
)

# Convertir el local a formato binario
local_hells_kitchen = 1 if local == "store_location_hell's kitchen" else 0
local_lower_manhattan = 1 if local == "store_location_lower manhattan" else 0

if st.button("Predecir"):
    input_data = pd.DataFrame(
        [[month, year, local_hells_kitchen, local_lower_manhattan]],
        columns=["month", "year", "store_location_hell's kitchen", "store_location_lower manhattan"]
    )

    # Realizar la predicción
    prediction = model.predict(input_data)

    # Mostrar el resultado
    st.write(f"Predicción de la suma de transacciones: {prediction[0]:,.2f}")
