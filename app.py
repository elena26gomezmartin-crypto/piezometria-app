import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        # 🔥 Leer TODAS las columnas sin limitaciones
        df = pd.read_excel(archivo, engine="openpyxl")

        # Limpiar nombres
        df.columns = [str(c).strip() for c in df.columns]

        st.success(f"Columnas detectadas: {len(df.columns)}")

        # 🔍 MOSTRAR TODAS LAS COLUMNAS CLARAMENTE
        st.subheader("📋 Todas las columnas del Excel")
        st.write(df.columns.tolist())

        # 👇 SELECTORES (ahora deberían salir TODAS)
        col_codigo = st.selectbox("Código", df.columns.tolist())
        col_municipio = st.selectbox("Municipio", df.columns.tolist())
        col_fecha = st.selectbox("Fecha", df.columns.tolist())
        col_nivel = st.selectbox("Nivel", df.columns.tolist())
        col_sector = st.selectbox("Sector", df.columns.tolist())

        # Mostrar datos
        columnas = [col_codigo, col_municipio, col_fecha, col_nivel, col_sector]

        st.subheader("📊 Datos filtrados")
        st.dataframe(df[columnas], use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
