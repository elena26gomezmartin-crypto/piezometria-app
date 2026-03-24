import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    df = pd.read_excel(archivo)

    # Limpiar nombres de columnas
df.columns = df.columns.str.strip()

# Mostrar columnas para ver nombres reales
st.write("Columnas:", df.columns)

# Buscar columna de fecha
col_fecha = [col for col in df.columns if "fecha" in col.lower()][0]

df[col_fecha] = pd.to_datetime(df[col_fecha])
    st.subheader("Vista de datos")
    st.dataframe(df)

    provincia = st.selectbox("Provincia", df["Provincia"].unique())
    df = df[df["Provincia"] == provincia]

    piezometro = st.selectbox("Piezómetro", df["Codigo"].unique())
    df_filtrado = df[df["Codigo"] == piezometro]

    df_filtrado = df_filtrado.sort_values("Fecha")

    st.subheader("Evolución del nivel")
    st.line_chart(df_filtrado.set_index(col_fecha)["Nivel"])

    st.write("Nivel medio:", round(df_filtrado["Nivel"].mean(), 2))
