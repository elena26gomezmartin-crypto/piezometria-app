import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        df = pd.read_excel(archivo)

        # Limpiar nombres de columnas
        df.columns = df.columns.astype(str).str.strip()

        # 🔍 Detectar columnas automáticamente
        columnas = [
            "CODIGO",
            "MUNICIPIO",
            "FECHA",
            "NIVEL (m)",
            "SECTOR"
        ]

        # Filtrar solo las que existan (por seguridad)
        columnas = [col for col in columnas if col in df.columns]

        # Quitar None (por si alguna no se detecta)
        columnas = [c for c in columnas if c is not None]

        st.success("Columnas seleccionadas")

        # Mostrar solo esas columnas
        st.dataframe(df[columnas], use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
