import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="5 Gráficos en Streamlit", layout="wide")

st.title("📊 Visualización de 5 Gráficos con Streamlit")
st.write("Comparativa de los 5 gráficos implementados en el cuaderno (Matplotlib, Seaborn y Nativos de Streamlit).")

# Cargar datos de ejemplo (Puedes cambiarlo por el dataset de tu Colab)
@st.cache_data
def cargar_datos():
    return sns.load_dataset("tips")

df = cargar_datos()

with st.expander("Ver tabla de datos original"):
    st.dataframe(df.head(10))

# Selector para ver la versión nativa de Streamlit o las librerías del cuaderno
modo = st.radio(
    "Elige cómo visualizar los gráficos en la página:",
    ["Nativos de Streamlit + Pyplot", "Comparativa directa: Matplotlib vs Seaborn (con st.pyplot)"],
    horizontal=True
)

st.divider()

if modo == "Nativos de Streamlit + Pyplot":
    col1, col2 = st.columns(2)

    # 1. Gráfico de Barras
    with col1:
        st.subheader("1. Gráfico de Barras (Propina media por día)")
        datos_barras = df.groupby("day", observed=False)["tip"].mean()
        st.bar_chart(datos_barras)

    # 2. Gráfico de Dispersión (Scatter)
    with col2:
        st.subheader("2. Gráfico de Dispersión (Cuenta total vs Propina)")
        st.scatter_chart(df, x="total_bill", y="tip", color="sex")

    col3, col4 = st.columns(2)

    # 3. Gráfico de Líneas
    with col3:
        st.subheader("3. Gráfico de Líneas (Evolución de las primeras 30 cuentas)")
        st.line_chart(df[["total_bill", "tip"]].head(30))

    # 4. Histograma (Renderizado con st.pyplot)
    with col4:
        st.subheader("4. Histograma (Distribución de la cuenta total)")
        fig_hist, ax_hist = plt.subplots()
        sns.histplot(df["total_bill"], kde=True, ax=ax_hist, color="#ff4b4b")
        st.pyplot(fig_hist)

    # 5. Boxplot / Diagrama de Caja (Renderizado con st.pyplot)
    st.subheader("5. Diagrama de Caja / Boxplot (Cuenta total por día)")
    fig_box, ax_box = plt.subplots(figsize=(10, 4))
    sns.boxplot(data=df, x="day", y="total_bill", hue="sex", ax=ax_box)
    st.pyplot(fig_box)

else:
    st.info("En Streamlit, cualquier gráfico de Matplotlib o Seaborn de tu Colab se muestra envolviéndolo en `fig, ax = plt.subplots()` y llamando a `st.pyplot(fig)`.")
    
    col_mat, col_sns = st.columns(2)
    
    with col_mat:
        st.header("🐍 Matplotlib")
        
        # 1. Barras Matplotlib
        st.subheader("1. Barras")
        fig1, ax1 = plt.subplots()
        propinas_dia = df.groupby("day", observed=False)["tip"].mean()
        ax1.bar(propinas_dia.index, propinas_dia.values, color="skyblue")
        ax1.set_title("Propina media por día")
        st.pyplot(fig1)

        # 2. Dispersión Matplotlib
        st.subheader("2. Dispersión")
        fig2, ax2 = plt.subplots()
        ax2.scatter(df["total_bill"], df["tip"], alpha=0.6, color="teal")
        ax2.set_xlabel("Total Cuenta")
        ax2.set_ylabel("Propina")
        st.pyplot(fig2)

        # 3. Líneas Matplotlib
        st.subheader("3. Líneas")
        fig3, ax3 = plt.subplots()
        ax3.plot(df["total_bill"].head(30), label="Total Bill", color="orange")
        ax3.legend()
        st.pyplot(fig3)

        # 4. Histograma Matplotlib
        st.subheader("4. Histograma")
        fig4, ax4 = plt.subplots()
        ax4.hist(df["total_bill"], bins=15, color="purple", edgecolor="black")
        st.pyplot(fig4)

        # 5. Boxplot Matplotlib
        st.subheader("5. Boxplot")
        fig5, ax5 = plt.subplots()
        grupos = [ grupo["total_bill"].values for _, grupo in df.groupby("day", observed=False) ]
        ax5.boxplot(grupos, tick_labels=df["day"].unique())
        st.pyplot(fig5)

    with col_sns:
        st.header("🌊 Seaborn")

        # 1. Barras Seaborn
        st.subheader("1. Barras")
        fig6, ax6 = plt.subplots()
        sns.barplot(data=df, x="day", y="tip", ax=ax6, palette="viridis", errorbar=None)
        ax6.set_title("Propina media por día")
        st.pyplot(fig6)

        # 2. Dispersión Seaborn
        st.subheader("2. Dispersión")
        fig7, ax7 = plt.subplots()
        sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", ax=ax7)
        st.pyplot(fig7)

        # 3. Líneas Seaborn
        st.subheader("3. Líneas")
        fig8, ax8 = plt.subplots()
        sns.lineplot(data=df.head(30), x=df.head(30).index, y="total_bill", ax=ax8, color="orange")
        st.pyplot(fig8)

        # 4. Histograma Seaborn
        st.subheader("4. Histograma")
        fig9, ax9 = plt.subplots()
        sns.histplot(data=df, x="total_bill", bins=15, kde=True, ax=ax9, color="purple")
        st.pyplot(fig9)

        # 5. Boxplot Seaborn
        st.subheader("5. Boxplot")
        fig10, ax10 = plt.subplots()
        sns.boxplot(data=df, x="day", y="total_bill", ax=ax10, palette="Set2")
        st.pyplot(fig10)
