import streamlit as st
import pandas as pd

st.set_page_config(page_title="Control piezométrico", layout="wide")

st.title("📊 Control piezométrico")

archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

if archivo:
    # Leer Excel probando varias opciones de encabezado
    df = None
    for i in range(5):  # prueba primeras 5 filas como cabecera
        try:
            df_temp = pd.read_excel(archivo, header=i)
            if df_temp.shape[1] > 5:  # si tiene bastantes columnas, es correcto
                df = df_temp
                break
        except:
            continue

    if df is None:
        st.error("No se pudo leer correctamente el Excel")
    else:
        # Limpiar nombres de columnas
        df.columns = df.columns.astype(str).str.strip()

        st.success("Excel cargado correctamente")

        # 🔍 MOSTRAR TODAS LAS COLUMNAS
        st.subheader("📋 Todas las columnas del Excel")
        st.write(list(df.columns))

        # 📊 MOSTRAR DATOS COMPLETOS
        st.subheader("📊 Vista completa de datos")
        st.dataframe(df, use_container_width=True)

        # 🧠 Intentar detectar columnas clave automáticamente
        col_fecha = next((c for c in df.columns if "fecha" in c.lower()), None)
        col_nivel = next((c for c in df.columns if "nivel" in c.lower()), None)
        col_codigo = next((c for c in df.columns if "codigo" in c.lower()), None)
        col_provincia = next((c for c in df.columns if "provincia" in c.lower()), None)

        # 📌 Si existen, activar filtros y gráfica
        if col_fecha and col_nivel and col_codigo:
            try:
                df[col_fecha] = pd.to_datetime(df[col_fecha], errors="coerce")
                df = df.dropna(subset=[col_fecha])

                st.sidebar.header("Filtros")

                if col_provincia:
                    provincia = st.sidebar.selectbox(
                        "Provincia", df[col_provincia].dropna().unique()
                    )
                    df = df[df[col_provincia] == provincia]

                piezometro = st.sidebar.selectbox(
                    "Piezómetro", df[col_codigo].dropna().unique()
                )
                df_filtrado = df[df[col_codigo] == piezometro]

                df_filtrado = df_filtrado.sort_values(col_fecha)

                # MÉTRICAS
                col1, col2 = st.columns(2)
                col1.metric("Nivel medio", round(df_filtrado[col_nivel].mean(), 2))
                col2.metric("Nivel mínimo", round(df_filtrado[col_nivel].min(), 2))

                # GRÁFICA
                st.subheader("📈 Evolución del nivel")
                st.line_chart(df_filtrado.set_index(col_fecha)[col_nivel])

            except Exception as e:
                st.warning("No se pudo generar la gráfica automáticamente")

        else:
            st.info("No se detectaron automáticamente columnas de fecha/nivel/código")
