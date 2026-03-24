import streamlit as st
import pandas as pd

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    df = pd.read_excel(archivo)

    df["Fecha"] = pd.to_datetime(df["Fecha"])

    st.subheader("Vista de datos")
    st.dataframe(df)

    provincia = st.selectbox("Provincia", df["Provincia"].unique())
    df = df[df["Provincia"] == provincia]

    piezometro = st.selectbox("Piezómetro", df["Codigo"].unique())
    df_filtrado = df[df["Codigo"] == piezometro]

    df_filtrado = df_filtrado.sort_values("Fecha")

    st.subheader("Evolución del nivel")
    st.line_chart(df_filtrado.set_index("Fecha")["Nivel"])

    st.write("Nivel medio:", round(df_filtrado["Nivel"].mean(), 2))
