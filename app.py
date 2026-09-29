import streamlit as st
import pandas as pd
import joblib

# Configuração da página
st.set_page_config(
    page_title="Risco de Defasagem | Passos Mágicos",
    page_icon="📊",
    layout="centered"
)

# Carregamento do modelo
@st.cache_resource
def carregar_modelo():
    return joblib.load("modelo_risco_defasagem.pkl")


modelo = carregar_modelo()

# Título
st.title("Previsão de Risco de Defasagem")

st.write(
    """
    Aplicação exploratória desenvolvida a partir dos dados do
    Datathon Passos Mágicos.

    Informe os indicadores do estudante para obter uma estimativa
    da probabilidade de entrada futura em situação de defasagem.
    """
)

st.divider()

# Entradas
st.subheader("Indicadores do estudante")

iaa = st.number_input(
    "IAA — Indicador de Autoavaliação",
    min_value=0.0,
    max_value=10.0,
    value=8.0,
    step=0.1
)

ieg = st.number_input(
    "IEG — Indicador de Engajamento",
    min_value=0.0,
    max_value=10.0,
    value=8.0,
    step=0.1
)

ips = st.number_input(
    "IPS — Indicador Psicossocial",
    min_value=0.0,
    max_value=10.0,
    value=6.0,
    step=0.1
)

ida = st.number_input(
    "IDA — Indicador de Aprendizagem",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

st.divider()

if st.button(
    "Calcular probabilidade de risco",
    type="primary",
    use_container_width=True
):

    entrada = pd.DataFrame(
        [[iaa, ieg, ips, ida]],
        columns=["IAA", "IEG", "IPS", "IDA"]
    )

    probabilidade = modelo.predict_proba(entrada)[0, 1]

    st.subheader("Resultado")

    st.metric(
        "Probabilidade estimada de entrada em risco",
        f"{probabilidade * 100:.1f}%"
    )

    if probabilidade >= 0.50:
        st.warning(
            "O modelo sinalizou probabilidade igual ou superior "
            "ao limiar de referência de 50%."
        )
    else:
        st.success(
            "O modelo estimou probabilidade inferior ao "
            "limiar de referência de 50%."
        )

    st.caption(
        "O resultado representa uma estimativa estatística do modelo "
        "e não deve ser interpretado como diagnóstico ou decisão "
        "automática sobre o estudante."
    )

st.divider()

st.subheader("Sobre o modelo")

st.write(
    """
    O modelo utilizado é uma Regressão Logística treinada com
    indicadores educacionais de 2022 para prever a entrada em
    defasagem em 2023 e avaliada temporalmente com dados de 2023
    para prever a situação observada em 2024.

    No conjunto de teste, o modelo apresentou recall de 60,8%,
    precisão de 26,5% e ROC-AUC de 61,4%.

    Os resultados devem ser considerados exploratórios e utilizados
    como apoio à análise educacional, sempre em conjunto com outras
    informações e com a avaliação dos profissionais responsáveis.
    """
)
