# Datathon — Passos Mágicos

## Análise de Indicadores Educacionais e Previsão de Risco de Defasagem

Projeto desenvolvido para o Datathon da Passos Mágicos, com análise dos dados
educacionais disponibilizados para os anos de 2022, 2023 e 2024.

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

Embora o baseline apresente maior acurácia, ele não identifica nenhum estudante
da classe de risco. Por isso, a análise dos modelos considerou especialmente
métricas relacionadas à identificação dessa classe, como recall, F1-score e
ROC-AUC.

Os resultados indicam capacidade preditiva limitada e, portanto, o modelo deve
ser interpretado como ferramenta exploratória de apoio à priorização do
acompanhamento, e não como mecanismo automático de decisão.

## Insight longitudinal

A análise dos mesmos estudantes entre 2022 e 2024 identificou 441 casos
comparáveis.

- 242 estudantes (54,88%) aumentaram o INDE;
- 199 estudantes (45,12%) reduziram o INDE;
- o INDE médio passou de 7,39 em 2022 para 7,38 em 2024;
- a variação individual média foi de -0,01.

Apesar da estabilidade do indicador agregado, as trajetórias individuais
mostram movimentos relevantes de melhora e redução do INDE.

Esse resultado sugere que o acompanhamento educacional pode se beneficiar
da combinação entre o nível atual dos indicadores, sua evolução longitudinal
e a probabilidade estimada de risco futuro.

## Aplicação interativa

Foi desenvolvida uma aplicação em Streamlit que permite informar os indicadores
IAA, IEG, IPS e IDA de um estudante e obter a probabilidade estimada pelo modelo
de entrada futura em situação de defasagem.

🔗 **[Acessar aplicação Streamlit](https://datathonpaappsmagicos-v7reatsgrejy6kkfkcrybt.streamlit.app/)**

A aplicação utiliza a Regressão Logística desenvolvida no projeto e adota
50% como limiar de referência para sinalização.

> **Importante:** a probabilidade apresentada é uma estimativa estatística
> exploratória. O resultado não representa diagnóstico e não deve ser utilizado
> isoladamente para decisões sobre estudantes.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Google Colab
- Streamlit
- GitHub

## Estrutura do projeto

```text
datathon-passos-magicos/
│
├── Datathon_Passos_Magicos_FINAL.ipynb
├── README.md
├── app.py
├── modelo_risco_defasagem.pkl
└── requirements.txt
```

### Arquivos principais

- `Datathon_Passos_Magicos_FINAL.ipynb`: análise exploratória, longitudinal e modelagem.
- `app.py`: aplicação interativa desenvolvida em Streamlit.
- `modelo_risco_defasagem.pkl`: pipeline treinado utilizado pela aplicação.
- `requirements.txt`: dependências necessárias para execução da aplicação.

## Limitações

O conjunto utilizado para treinamento continha apenas 19 casos positivos de
entrada futura em risco. Também foram observadas mudanças na distribuição dos
indicadores entre os períodos analisados.

Dessa forma, os resultados da modelagem devem ser considerados exploratórios e
necessitam de validação com uma série histórica maior antes de eventual
utilização operacional.

## Considerações finais

A análise evidencia a importância de combinar indicadores agregados com o
acompanhamento longitudinal das trajetórias individuais.

A estabilidade das médias gerais pode coexistir com mudanças relevantes na
trajetória de estudantes específicos. Nesse contexto, análises longitudinais
e modelos preditivos podem funcionar como instrumentos complementares para
apoiar a identificação de casos que mereçam acompanhamento mais próximo.
