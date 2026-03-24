import streamlit as st
import pandas as pd

st.set_page_config(page_title="Control piezométrico", layout="wide")

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    df = pd.read_excel(archivo)

    # Limpiar nombres de columnas
    df.columns = df.columns.str.strip()

    # Mostrar columnas
    st.write("Columnas detectadas:", df.columns)

    # Detectar columna de fecha
    col_fecha = [col for col in df.columns if "fecha" in col.lower()][0]

    df[col_fecha] = pd.to_datetime(df[col_fecha])

    # FILTROS
    st.sidebar.header("Filtros")

    provincia = st.sidebar.selectbox("Provincia", df["Provincia"].unique())
    df = df[df["Provincia"] == provincia]

    piezometro = st.sidebar.selectbox("Piezómetro", df["Codigo"].unique())
    df_filtrado = df[df["Codigo"] == piezometro]

    df_filtrado = df_filtrado.sort_values(col_fecha)

    # MÉTRICAS
    col1, col2 = st.columns(2)
    col1.metric("Nivel medio", round(df_filtrado["Nivel"].mean(), 2))
    col2.metric("Nivel mínimo", round(df_filtrado["Nivel"].min(), 2))

    # GRÁFICA
    st.subheader("📈 Evolución del nivel")
    st.line_chart(df_filtrado.set_index(col_fecha)["Nivel"])

    # TABLA
    st.subheader("📋 Datos")
    st.dataframe(df_filtrado)
