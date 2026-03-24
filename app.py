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
        col_codigo = next((c for c in df.columns if "codigo" in c.lower()), None)
        col_municipio = next((c for c in df.columns if "municipio" in c.lower()), None)
        col_fecha = next((c for c in df.columns if "fecha" in c.lower()), None)
        col_nivel = next((c for c in df.columns if "nivel" in c.lower()), None)
        col_sector = next((c for c in df.columns if "sector" in c.lower()), None)

        columnas = [col_codigo, col_municipio, col_fecha, col_nivel, col_sector]

        # Quitar None (por si alguna no se detecta)
        columnas = [c for c in columnas if c is not None]

        st.success("Columnas seleccionadas")

        # Mostrar solo esas columnas
        st.dataframe(df[columnas], use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
