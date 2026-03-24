import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        # Leer Excel
        df = pd.read_excel(archivo)

        # Limpiar nombres de columnas (quita espacios raros)
        df.columns = df.columns.astype(str).str.strip()

        # Diccionario para guardar columnas detectadas
        columnas = {}

        for col in df.columns:
            col_lower = col.lower()

            if "codigo" in col_lower:
                columnas["codigo"] = col
            elif "municipio" in col_lower:
                columnas["municipio"] = col
            elif "fecha" in col_lower:
                columnas["fecha"] = col
            elif "nivel" in col_lower:
                columnas["nivel"] = col
            elif "sector" in col_lower:
                columnas["sector"] = col

        # Ver qué se ha detectado
        st.write("Columnas detectadas:", columnas)

        # Crear lista final
        columnas_finales = [columnas.get(k) for k in ["codigo","municipio","fecha","nivel","sector"]]
        columnas_finales = [c for c in columnas_finales if c is not None]

        # Mostrar tabla
        st.dataframe(df[columnas_finales], use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
