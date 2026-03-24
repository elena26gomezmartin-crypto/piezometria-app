import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        # 🔥 Leer Excel SIN asumir encabezado
        df_raw = pd.read_excel(archivo, header=None)

        st.subheader("🔍 Vista previa del Excel (para detectar cabecera)")
        st.dataframe(df_raw.head(10), use_container_width=True)

        # 🔎 Buscar la fila donde empieza el encabezado (donde está CODIGO)
        fila_header = None
        for i in range(10):
            fila = df_raw.iloc[i].astype(str).str.upper()
            if fila.str.contains("CODIGO").any():
                fila_header = i
                break

        if fila_header is None:
            st.error("No se encontró la fila de cabecera")
        else:
            st.success(f"Cabecera detectada en fila {fila_header}")

            # 🔥 Leer de nuevo usando la cabecera correcta
            df = pd.read_excel(archivo, header=fila_header)

            # Limpiar nombres
            df.columns = df.columns.astype(str).str.strip()

            st.subheader("📋 TODAS las columnas detectadas")
            st.write(df.columns.tolist())

            st.subheader("📊 DATOS COMPLETOS")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
