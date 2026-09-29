# Datathon — Passos Mágicos

## Análise de Indicadores Educacionais e Previsão de Risco de Defasagem

Projeto desenvolvido para o Datathon da Passos Mágicos, com análise dos
dados educacionais disponibilizados para os anos de 2022, 2023 e 2024.

O trabalho combina análise exploratória, acompanhamento longitudinal dos
estudantes e Machine Learning para investigar padrões nos indicadores
educacionais e apoiar a identificação antecipada de estudantes com risco
futuro de defasagem.

## Objetivos

A análise busca compreender a evolução dos indicadores educacionais ao longo
do período, investigar relações entre as diferentes dimensões avaliadas e
identificar padrões relevantes para o acompanhamento dos estudantes.

Além das análises descritivas e longitudinais, foi desenvolvido um modelo
preditivo exploratório para estimar a probabilidade de estudantes inicialmente
sem defasagem entrarem em situação de defasagem no período seguinte.

## Metodologia

O projeto contempla:

- preparação, limpeza e consolidação das bases de 2022, 2023 e 2024;
- análise exploratória dos indicadores educacionais;
- padronização de variáveis para permitir comparações entre os anos;
- análises por fase e classificação Pedra;
- investigação de correlações entre indicadores;
- análise longitudinal da trajetória dos estudantes;
- construção de variável-alvo para entrada futura em defasagem;
- separação temporal entre treino e teste;
- comparação entre baseline, Regressão Logística e Random Forest;
- avaliação por acurácia, precisão, recall, F1-score e ROC-AUC;
- geração de probabilidades individuais estimadas de entrada em risco.

## Machine Learning

A modelagem foi estruturada de forma temporal.

Os dados de 2022 foram utilizados para construir o conjunto de treinamento,
considerando a situação dos estudantes em 2023. Os dados de 2023 foram
utilizados no conjunto de teste, considerando a situação observada em 2024.

Entre os modelos avaliados, a Regressão Logística apresentou maior capacidade
de identificação da classe de interesse:

| Modelo | Acurácia | Precisão | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Baseline | 0,764 | 0,000 | 0,000 | 0,000 | — |
| Regressão Logística | 0,510 | 0,265 | 0,608 | 0,369 | 0,614 |
| Random Forest | 0,716 | 0,300 | 0,152 | 0,202 | 0,569 |

A Regressão Logística identificou 48 dos 79 estudantes que efetivamente
entraram em risco no conjunto de teste.

Os resultados indicam capacidade preditiva limitada e, portanto, o modelo
deve ser interpretado como ferramenta exploratória de apoio à priorização
do acompanhamento, e não como mecanismo automático de decisão.

## Insight longitudinal

A análise dos mesmos estudantes entre 2022 e 2024 identificou 441 casos
comparáveis.

- 242 estudantes (54,88%) aumentaram o INDE;
- 199 estudantes (45,12%) reduziram o INDE;
- o INDE médio passou de 7,39 em 2022 para 7,38 em 2024;
- a variação individual média foi de -0,01.

Apesar da estabilidade do indicador agregado, as trajetórias individuais
mostram movimentos relevantes de melhora e deterioração.

Esse resultado sugere que o acompanhamento educacional pode se beneficiar
da combinação entre o nível atual dos indicadores, sua evolução longitudinal
e a probabilidade estimada de risco futuro.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab
- Streamlit

## Estrutura do projeto

```text
datathon-passos-magicos/
│
├── Datathon_Passos_Magicos_FINAL.ipynb
├── README.md
├── app.py                 # aplicação Streamlit
├── requirements.txt       # dependências da aplicação
└── arquivos do modelo     # adicionados na etapa de deploy
