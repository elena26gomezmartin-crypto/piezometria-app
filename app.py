import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        # Leer Excel directamente
        df = pd.read_excel(archivo)

        # Limpiar nombres de columnas
        df.columns = df.columns.astype(str).str.strip()

        st.success("Excel cargado correctamente")

        # Mostrar TODAS las columnas
        st.write("Columnas del Excel:")
        st.write(df.columns.tolist())

        # Mostrar datos completos
        st.write("Datos:")
        st.dataframe(df)

    except Exception as e:
        st.error(f"Error al leer el Excel: {e}")
