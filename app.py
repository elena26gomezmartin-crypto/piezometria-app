import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        # Leer Excel SIN cabecera
        df = pd.read_excel(archivo, header=None)

        st.subheader("🔍 Vista previa del Excel")
        st.dataframe(df.head(10), use_container_width=True)

        # Buscar la fila correcta (donde aparece FECHA o CODIGO)
        fila_header = None

        for i in range(10):
            fila = df.iloc[i].astype(str).str.upper()

            if fila.str.contains("FECHA").any() and fila.str.contains("CODIGO").any():
                fila_header = i
                break

        if fila_header is None:
            st.error("No se pudo detectar la cabecera automáticamente")
        else:
            st.success(f"Cabecera detectada en fila {fila_header}")

            # Leer bien el Excel
            df = pd.read_excel(archivo, header=fila_header)

            # Limpiar columnas
            df.columns = df.columns.astype(str).str.strip()

            st.subheader("📋 TODAS las columnas")
            st.write(df.columns.tolist())

            st.subheader("📊 DATOS COMPLETOS")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
