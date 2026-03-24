import streamlit as st
import pandas as pd

st.set_page_config(page_title="Control piezométrico", layout="wide")

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    df = pd.read_excel(archivo)

    # Limpiar columnas
    df.columns = df.columns.str.strip()

    # Nombres reales
    col_fecha = "FECHA"
    col_nivel = "NIVEL (m)"
    col_codigo = "CODIGO"
    col_provincia = "PROVINCIA"

    # Convertir fecha
    df[col_fecha] = pd.to_datetime(df[col_fecha], errors="coerce")

    # Quitar filas sin fecha
    df = df.dropna(subset=[col_fecha])

    # FILTROS
    st.sidebar.header("Filtros")

    provincia = st.sidebar.selectbox("Provincia", df[col_provincia].dropna().unique())
    df = df[df[col_provincia] == provincia]

    piezometro = st.sidebar.selectbox("Piezómetro", df[col_codigo].dropna().unique())
    df_filtrado = df[df[col_codigo] == piezometro]

    df_filtrado = df_filtrado.sort_values(col_fecha)

    # MÉTRICAS
    col1, col2 = st.columns(2)
    col1.metric("Nivel medio", round(df_filtrado[col_nivel].mean(), 2))
    col2.metric("Nivel mínimo", round(df_filtrado[col_nivel].min(), 2))

    # GRÁFICA
    st.subheader("📈 Evolución del nivel")
    st.line_chart(df_filtrado.set_index(col_fecha)[col_nivel])

    # TABLA
    st.subheader("📋 Datos")
    st.dataframe(df_filtrado)
