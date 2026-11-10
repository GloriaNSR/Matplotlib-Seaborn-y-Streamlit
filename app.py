import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Dashboard Influencers 2026", layout="wide")

st.title("📊 Análisis de Influencers Globales de Instagram (2026)")
st.write("Visualización de los 5 gráficos del cuaderno de Colab implementados en Streamlit.")

# Cargar el CSV (asegúrate de subir instagram_global_influencers_2026.csv a tu GitHub)
@st.cache_data
def cargar_datos():
    return pd.read_csv("instagram_global_influencers_2026.csv")

try:
    influ = cargar_datos()
except FileNotFoundError:
    st.error("⚠️ No se encontró el archivo 'instagram_global_influencers_2026.csv'. Súbelo a la misma carpeta de tu repositorio de GitHub.")
    st.stop()

with st.expander("🔍 Ver primeras filas del dataset (influ.head())"):
    st.dataframe(influ.head())

# Pestañas para ver los gráficos con componentes nativos de Streamlit o los exactos de tu Colab
tab_st, tab_mat, tab_sns = st.tabs([
    "🚀 Gráficos Nativos Streamlit",
    "🐍 Tus 5 Gráficos en Matplotlib",
    "🌊 Tus 5 Gráficos en Seaborn"
])

# ==========================================
# PESTAÑA 1: GRÁFICOS CON STREAMLIT
# ==========================================
with tab_st:
    st.header("Visualización con Streamlit")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1. Distribución de Seguidores (en millones)")
        fig_st1, ax_st1 = plt.subplots()
        sns.histplot(influ['followers'] / 1e6, bins=20, color='skyblue', kde=True, ax=ax_st1)
        ax_st1.set_xlabel('Seguidores (en millones)')
        ax_st1.set_ylabel('Cantidad de Influencers')
        st.pyplot(fig_st1)

        st.subheader("3. Top 10 Países con más Influencers")
        top_countries_st = influ['country'].value_counts().head(10)
        st.bar_chart(top_countries_st)

        st.subheader("5. Relación: Posts Publicados vs Influence Score")
        st.scatter_chart(influ, x='posts', y='influence_score', color='#FFD700')

    with col2:
        st.subheader("2. Relación: Seguidores vs Likes Promedio (en millones)")
        df_scatter = pd.DataFrame({
            'Seguidores (M)': influ['followers'] / 1e6,
            'Likes Promedio (M)': influ['avg_likes'] / 1e6
        })
        st.scatter_chart(df_scatter, x='Seguidores (M)', y='Likes Promedio (M)', color='#FF7F50')

        st.subheader("4. Distribución de Puntuación de Influencia (Boxplot)")
        fig_st4, ax_st4 = plt.subplots(figsize=(8, 4))
        sns.boxplot(data=influ, x='influence_score', color='orchid', ax=ax_st4)
        ax_st4.set_xlabel('Influence Score')
        st.pyplot(fig_st4)

# ==========================================
# PESTAÑA 2: TUS 5 GRÁFICOS DE MATPLOTLIB
# ==========================================
with tab_mat:
    st.header("5 Gráficos con Matplotlib (Idénticos al Colab)")
    col_m1, col_m2 = st.columns(2)

    with col_m1:
        # 1. Histograma: Distribución de Seguidores
        fig1, ax1 = plt.subplots()
        ax1.hist(influ['followers'] / 1e6, bins=20, color='skyblue', edgecolor='black')
        ax1.set_title('1. Distribución de Seguidores (Matplotlib)')
        ax1.set_xlabel('Seguidores (en millones)')
        ax1.set_ylabel('Cantidad de Influencers')
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig1)

        # 3. Barras: Top 10 Países
        top_countries = influ['country'].value_counts().head(10)
        fig3, ax3 = plt.subplots()
        ax3.bar(top_countries.index, top_countries.values, color='lightgreen', edgecolor='black')
        ax3.set_title('3. Top 10 Países con más Influencers (Matplotlib)')
        ax3.set_xlabel('País')
        ax3.set_ylabel('Cantidad de Influencers')
        plt.setp(ax3.get_xticklabels(), rotation=45, ha='right')
        fig3.tight_layout()
        st.pyplot(fig3)

        # 5. Dispersión: Posts vs Influence Score
        fig5, ax5 = plt.subplots()
        ax5.scatter(influ['posts'], influ['influence_score'], color='gold', alpha=0.7, edgecolors='black')
        ax5.set_title('5. Relación: Posts Publicados vs Influence Score (Matplotlib)')
        ax5.set_xlabel('Total de Posts')
        ax5.set_ylabel('Influence Score')
        ax5.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig5)

    with col_m2:
        # 2. Dispersión: Seguidores vs Likes Promedio
        fig2, ax2 = plt.subplots()
        ax2.scatter(influ['followers'] / 1e6, influ['avg_likes'] / 1e6, color='coral', alpha=0.7, edgecolors='black')
        ax2.set_title('2. Relación: Seguidores vs Likes Promedio (Matplotlib)')
        ax2.set_xlabel('Seguidores (en millones)')
        ax2.set_ylabel('Likes Promedio por Post (en millones)')
        ax2.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig2)

        # 4. Boxplot: Distribución de Influence Score
        fig4, ax4 = plt.subplots()
        ax4.boxplot(influ['influence_score'].dropna(), vert=False, patch_artist=True,
                    boxprops=dict(facecolor='orchid', color='black'),
                    medianprops=dict(color='yellow', linewidth=2))
        ax4.set_title('4. Distribución de Puntuación de Influencia (Matplotlib)')
        ax4.set_xlabel('Influence Score')
        ax4.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(fig4)

# ==========================================
# PESTAÑA 3: TUS 5 GRÁFICOS DE SEABORN
# ==========================================
with tab_sns:
    st.header("5 Gráficos con Seaborn (Idénticos al Colab)")
    col_s1, col_s2 = st.columns(2)

    with col_s1:
        # 1. Histograma: Distribución de Seguidores con KDE
        fig6, ax6 = plt.subplots(figsize=(10, 6))
        sns.histplot(data=influ, x=influ['followers'] / 1e6, bins=20, color='skyblue', kde=True, ax=ax6)
        ax6.set_title('1. Distribución de Seguidores (Seaborn)')
        ax6.set_xlabel('Seguidores (en millones)')
        ax6.set_ylabel('Cantidad de Influencers')
        st.pyplot(fig6)

        # 3. Barras: Top 10 Países
        top_countries_df = influ['country'].value_counts().head(10).reset_index()
        top_countries_df.columns = ['country', 'count']
        fig8, ax8 = plt.subplots(figsize=(10, 6))
        sns.barplot(data=top_countries_df, x='country', y='count', hue='country', palette='viridis', legend=False, ax=ax8)
        ax8.set_title('3. Top 10 Países con más Influencers (Seaborn)')
        ax8.set_xlabel('País')
        ax8.set_ylabel('Cantidad de Influencers')
        plt.setp(ax8.get_xticklabels(), rotation=45, ha='right')
        fig8.tight_layout()
        st.pyplot(fig8)

        # 5. Dispersión: Posts vs Influence Score con línea de tendencia
        fig10, ax10 = plt.subplots(figsize=(10, 6))
        sns.regplot(data=influ, x='posts', y='influence_score', color='gold',
                    scatter_kws={'edgecolor': 'black', 'alpha': 0.7}, ax=ax10)
        ax10.set_title('5. Relación: Posts Publicados vs Influence Score (Seaborn)')
        ax10.set_xlabel('Total de Posts')
        ax10.set_ylabel('Influence Score')
        st.pyplot(fig10)

    with col_s2:
        # 2. Dispersión: Seguidores vs Likes Promedio
        fig7, ax7 = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=influ, x=influ['followers'] / 1e6, y=influ['avg_likes'] / 1e6,
                        color='coral', alpha=0.8, edgecolor='black', ax=ax7)
        ax7.set_title('2. Relación: Seguidores vs Likes Promedio (Seaborn)')
        ax7.set_xlabel('Seguidores (en millones)')
        ax7.set_ylabel('Likes Promedio por Post (en millones)')
        st.pyplot(fig7)

        # 4. Boxplot: Distribución de Influence Score
        fig9, ax9 = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=influ, x='influence_score', color='orchid', ax=ax9)
        ax9.set_title('4. Distribución de Puntuación de Influencia (Seaborn)')
        ax9.set_xlabel('Influence Score')
        st.pyplot(fig9)
