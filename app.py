import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        df = pd.read_excel(archivo)

        # Limpiar nombres
        df.columns = df.columns.astype(str).str.strip()

        st.success("Excel cargado correctamente")

        # 🔍 MOSTRAR TODAS LAS COLUMNAS (CLAVE)
        st.subheader("Selecciona las columnas que quieres usar")

        col_codigo = st.selectbox("Código", df.columns)
        col_municipio = st.selectbox("Municipio", df.columns)
        col_fecha = st.selectbox("Fecha", df.columns)
        col_nivel = st.selectbox("Nivel", df.columns)
        col_sector = st.selectbox("Sector", df.columns)

        # Mostrar resultado
        columnas = [col_codigo, col_municipio, col_fecha, col_nivel, col_sector]

        st.subheader("📊 Datos filtrados")
        st.dataframe(df[columnas], use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
