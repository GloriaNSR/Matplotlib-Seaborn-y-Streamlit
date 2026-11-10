import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Dashboard Influencers 2026", layout="wide")

st.title("📊 Análisis de Influencers Globales de Instagram (2026)")
st.write("Comparativa de los 5 gráficos implementados en el cuaderno (Matplotlib, Seaborn y Streamlit).")

# Cargar datos desde el archivo CSV en el repositorio
@st.cache_data
def cargar_datos():
    return pd.read_csv("instagram_global_influencers_2026.csv")

try:
    influ = cargar_datos()
except FileNotFoundError:
    st.error("⚠️ No se encontró 'instagram_global_influencers_2026.csv'. Asegúrate de subirlo a tu repositorio de GitHub.")
    st.stop()

with st.expander("🔍 Ver primeras filas del dataset (influ.head())"):
    st.dataframe(influ.head())

# Selector de modo igual que en la primera versión
modo = st.radio(
    "Elige cómo visualizar los gráficos en la página:",
    [
        "Comparativa lado a lado: Matplotlib vs Seaborn",
        "Gráficos Nativos de Streamlit + Pyplot"
    ],
    horizontal=True
)

st.divider()

# ==============================================================================
# MODO 1: COMPARATIVA LADO A LADO (MATPLOTLIB A LA IZQUIERDA, SEABORN A LA DERECHA)
# ==============================================================================
if modo == "Comparativa lado a lado: Matplotlib vs Seaborn":
    st.info("A la izquierda se muestran los gráficos generados con **Matplotlib** y a la derecha exactamente los mismos generados con **Seaborn**.")

    # Encabezados de las dos columnas
    col_mat_head, col_sns_head = st.columns(2)
    with col_mat_head:
        st.header("🐍 Matplotlib")
    with col_sns_head:
        st.header("🌊 Seaborn")

    # --- GRÁFICO 1: HISTOGRAMA ---
    st.subheader("1. Distribución de Seguidores")
    c1_mat, c1_sns = st.columns(2)
    with c1_mat:
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        ax1.hist(influ['followers'] / 1e6, bins=20, color='skyblue', edgecolor='black')
        ax1.set_title('1. Distribución de Seguidores (Matplotlib)')
        ax1.set_xlabel('Seguidores (en millones)')
        ax1.set_ylabel('Cantidad de Influencers')
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig1)

    with c1_sns:
        fig6, ax6 = plt.subplots(figsize=(8, 5))
        sns.histplot(data=influ, x=influ['followers'] / 1e6, bins=20, color='skyblue', kde=True, ax=ax6)
        ax6.set_title('1. Distribución de Seguidores (Seaborn)')
        ax6.set_xlabel('Seguidores (en millones)')
        ax6.set_ylabel('Cantidad de Influencers')
        st.pyplot(fig6)

    st.divider()

    # --- GRÁFICO 2: DISPERSIÓN (SEGUIDORES VS LIKES) ---
    st.subheader("2. Relación: Seguidores vs Likes Promedio")
    c2_mat, c2_sns = st.columns(2)
    with c2_mat:
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        ax2.scatter(influ['followers'] / 1e6, influ['avg_likes'] / 1e6, color='coral', alpha=0.7, edgecolors='black')
        ax2.set_title('2. Relación: Seguidores vs Likes Promedio (Matplotlib)')
        ax2.set_xlabel('Seguidores (en millones)')
        ax2.set_ylabel('Likes Promedio por Post (en millones)')
        ax2.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig2)

    with c2_sns:
        fig7, ax7 = plt.subplots(figsize=(8, 5))
        sns.scatterplot(data=influ, x=influ['followers'] / 1e6, y=influ['avg_likes'] / 1e6,
                        color='coral', alpha=0.8, edgecolor='black', ax=ax7)
        ax7.set_title('2. Relación: Seguidores vs Likes Promedio (Seaborn)')
        ax7.set_xlabel('Seguidores (en millones)')
        ax7.set_ylabel('Likes Promedio por Post (en millones)')
        st.pyplot(fig7)

    st.divider()

    # --- GRÁFICO 3: BARRAS (TOP 10 PAÍSES) ---
    st.subheader("3. Top 10 Países con más Influencers")
    c3_mat, c3_sns = st.columns(2)
    with c3_mat:
        top_countries = influ['country'].value_counts().head(10)
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        ax3.bar(top_countries.index, top_countries.values, color='lightgreen', edgecolor='black')
        ax3.set_title('3. Top 10 Países con más Influencers (Matplotlib)')
        ax3.set_xlabel('País')
        ax3.set_ylabel('Cantidad de Influencers')
        plt.setp(ax3.get_xticklabels(), rotation=45, ha='right')
        fig3.tight_layout()
        st.pyplot(fig3)

    with c3_sns:
        top_countries_df = influ['country'].value_counts().head(10).reset_index()
        top_countries_df.columns = ['country', 'count']
        fig8, ax8 = plt.subplots(figsize=(8, 5))
        sns.barplot(data=top_countries_df, x='country', y='count', hue='country', palette='viridis', legend=False, ax=ax8)
        ax8.set_title('3. Top 10 Países con más Influencers (Seaborn)')
        ax8.set_xlabel('País')
        ax8.set_ylabel('Cantidad de Influencers')
        plt.setp(ax8.get_xticklabels(), rotation=45, ha='right')
        fig8.tight_layout()
        st.pyplot(fig8)

    st.divider()

    # --- GRÁFICO 4: BOXPLOT (INFLUENCE SCORE) ---
    st.subheader("4. Distribución de Puntuación de Influencia (Boxplot)")
    c4_mat, c4_sns = st.columns(2)
    with c4_mat:
        fig4, ax4 = plt.subplots(figsize=(8, 5))
        ax4.boxplot(influ['influence_score'].dropna(), vert=False, patch_artist=True,
                    boxprops=dict(facecolor='orchid', color='black'),
                    medianprops=dict(color='yellow', linewidth=2))
        ax4.set_title('4. Distribución de Puntuación de Influencia (Matplotlib)')
        ax4.set_xlabel('Influence Score')
        ax4.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(fig4)

    with c4_sns:
        fig9, ax9 = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=influ, x='influence_score', color='orchid', ax=ax9)
        ax9.set_title('4. Distribución de Puntuación de Influencia (Seaborn)')
        ax9.set_xlabel('Influence Score')
        st.pyplot(fig9)

    st.divider()

    # --- GRÁFICO 5: DISPERSIÓN (POSTS VS INFLUENCE SCORE) ---
    st.subheader("5. Relación: Posts Publicados vs Influence Score")
    c5_mat, c5_sns = st.columns(2)
    with c5_mat:
        fig5, ax5 = plt.subplots(figsize=(8, 5))
        ax5.scatter(influ['posts'], influ['influence_score'], color='gold', alpha=0.7, edgecolors='black')
        ax5.set_title('5. Relación: Posts Publicados vs Influence Score (Matplotlib)')
        ax5.set_xlabel('Total de Posts')
        ax5.set_ylabel('Influence Score')
        ax5.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig5)

    with c5_sns:
        fig10, ax10 = plt.subplots(figsize=(8, 5))
        sns.regplot(data=influ, x='posts', y='influence_score', color='gold',
                    scatter_kws={'edgecolor': 'black', 'alpha': 0.7}, ax=ax10)
        ax10.set_title('5. Relación: Posts Publicados vs Influence Score (Seaborn)')
        ax10.set_xlabel('Total de Posts')
        ax10.set_ylabel('Influence Score')
        st.pyplot(fig10)

# ==============================================================================
# MODO 2: GRÁFICOS NATIVOS DE STREAMLIT + PYPLOT
# ==============================================================================
else:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1. Distribución de Seguidores (en millones)")
        fig_st1, ax_st1 = plt.subplots()
        sns.histplot(influ['followers'] / 1e6, bins=20, color='skyblue', kde=True, ax=ax_st1)
        ax_st1.set_xlabel('Seguidores (en millones)')
        ax_st1.set_ylabel('Cantidad de Influencers')
        st.pyplot(fig_st1)

        st.subheader("3. Top 10 Países con más Influencers (Nativo Streamlit)")
        top_countries_st = influ['country'].value_counts().head(10)
        st.bar_chart(top_countries_st)

        st.subheader("5. Posts Publicados vs Influence Score (Nativo Streamlit)")
        st.scatter_chart(influ, x='posts', y='influence_score', color='#FFD700')

    with col2:
        st.subheader("2. Seguidores vs Likes Promedio (Nativo Streamlit)")
        df_scatter = pd.DataFrame({
            'Seguidores (M)': influ['followers'] / 1e6,
            'Likes Promedio (M)': influ['avg_likes'] / 1e6
        })
        st.scatter_chart(df_scatter, x='Seguidores (M)', y='Likes Promedio (M)', color='#FF7F50')

        st.subheader("4. Dist
