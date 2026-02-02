import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

st.sidebar.header("⚙️ Configurações")

if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

if st.session_state.theme == 'light':
    theme_button_label = "🌙 Modo Escuro"
else:
    theme_button_label = "☀️ Modo Claro"

if st.sidebar.button(theme_button_label):
    if st.session_state.theme == 'light':
        st.session_state.theme = 'dark'
    else:
        st.session_state.theme = 'light'
    st.rerun()

if st.session_state.theme == 'dark':
    pio.templates.default = "plotly_dark"
    st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    .css-1d391kg, .css-12ttj6m {
        background-color: #262730;
    }
    .st-bb, .st-at, .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj, .st-ak, .st-al, .st-am, .st-an, .st-ao, .st-ap, .st-aq, .st-ar, .st-as {
        background-color: #262730;
    }
    h1, h2, h3, h4, h5, h6, p, span, div {
        color: #fafafa !important;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    pio.templates.default = "plotly_white"
    st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        color: #31333f;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown(f"**Tema atual:** {'🌙 Escuro' if st.session_state.theme == 'dark' else '☀️ Claro'}")

df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

st.sidebar.header("🔍 Filtros")

anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, "N/A"

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''},
            color_discrete_sequence=['#1f77b4'] if st.session_state.theme == 'light' else ['#00cc96']
        )
        grafico_cargos.update_layout(
            title_x=0.1, 
            yaxis={'categoryorder':'total ascending'},
            plot_bgcolor='rgba(0,0,0,0)' if st.session_state.theme == 'light' else 'rgba(255,255,255,0.05)',
            paper_bgcolor='rgba(0,0,0,0)' if st.session_state.theme == 'light' else 'rgba(0,0,0,0)'
        )
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ''},
            color_discrete_sequence=['#1f77b4'] if st.session_state.theme == 'light' else ['#00cc96']
        )
        grafico_hist.update_layout(
            title_x=0.1,
            plot_bgcolor='rgba(0,0,0,0)' if st.session_state.theme == 'light' else 'rgba(255,255,255,0.05)',
            paper_bgcolor='rgba(0,0,0,0)' if st.session_state.theme == 'light' else 'rgba(0,0,0,0)'
        )
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5,
            color_discrete_sequence=px.colors.sequential.RdBu if st.session_state.theme == 'light' else px.colors.sequential.Plasma
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(
            title_x=0.1,
            plot_bgcolor='rgba(0,0,0,0)' if st.session_state.theme == 'light' else 'rgba(255,255,255,0.05)',
            paper_bgcolor='rgba(0,0,0,0)' if st.session_state.theme == 'light' else 'rgba(0,0,0,0)'
        )
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        if not df_ds.empty:
            media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
            grafico_paises = px.choropleth(
                media_ds_pais,
                locations='residencia_iso3',
                color='usd',
                color_continuous_scale='RdYlGn' if st.session_state.theme == 'light' else 'Plasma',
                title='Salário médio de Cientista de Dados por país',
                labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
            )
            grafico_paises.update_layout(
                title_x=0.1,
                geo=dict(
                    bgcolor='rgba(0,0,0,0)',
                    lakecolor='rgba(255,255,255,0)'
                ),
                plot_bgcolor='rgba(0,0,0,0)' if st.session_state.theme == 'light' else 'rgba(255,255,255,0.05)',
                paper_bgcolor='rgba(0,0,0,0)' if st.session_state.theme == 'light' else 'rgba(0,0,0,0)'
            )
            st.plotly_chart(grafico_paises, use_container_width=True)
        else:
            st.warning("Nenhum dado de Data Scientist para exibir no mapa.")
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)