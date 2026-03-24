import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    try:
        # Leer Excel
        df = pd.read_excel(archivo)

        # Limpiar columnas (muy importante)
        df.columns = df.columns.astype(str).str.strip()

        # Mostrar columnas reales (para comprobar)
        st.write("Columnas reales:")
        st.write(df.columns.tolist())

        # 🔥 SELECCIÓN DIRECTA (SIN AUTOMÁTICOS)
        columnas = []

        for col in df.columns:
            nombre = col.upper().replace(" ", "")

            if nombre == "CODIGO":
                columnas.append(col)

            elif nombre == "MUNICIPIO":
                columnas.append(col)

            elif "FECHA" in nombre:
                columnas.append(col)

            elif "NIVEL" in nombre:
                columnas.append(col)

            elif "SECTOR" in nombre:
                columnas.append(col)

        # Mostrar resultado
        st.subheader("📊 Datos filtrados")
        st.dataframe(df[columnas], use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
