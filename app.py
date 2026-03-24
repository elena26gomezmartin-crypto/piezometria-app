import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        # 🔥 IMPORTANTE: usar header=1 (fila correcta)
        df = pd.read_excel(archivo, header=1)

        # Limpiar nombres
        df.columns = df.columns.astype(str).str.strip()

        st.success("Excel cargado correctamente")

        # Ver TODAS las columnas
        st.write("Columnas:")
        st.write(df.columns.tolist())

        # Mostrar datos completos
        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
