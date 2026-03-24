import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        # Leer Excel normal (cabecera en fila 1)
        df = pd.read_excel(archivo)

        # Limpiar nombres de columnas (por si hay espacios)
        df.columns = df.columns.str.strip()

        # 🔥 Columnas EXACTAS que quieres
        columnas_deseadas = [
            "CODIGO",
            "MUNICIPIO",
            "FECHA",
            "NIVEL (m)",
            "SECTOR"
        ]

        # Ver qué columnas existen realmente
        columnas_existentes = [col for col in columnas_deseadas if col in df.columns]

        # Aviso si falta alguna
        if len(columnas_existentes) < len(columnas_deseadas):
            st.warning("Alguna columna no coincide exactamente con el Excel")
            st.write("Columnas disponibles:")
            st.write(df.columns.tolist())

        # Mostrar solo las columnas que existen
        st.dataframe(df[columnas_existentes], use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
