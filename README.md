# Real Estate Price Prediction

Projeto de Machine Learning desenvolvido em Python para prever preços de imóveis com base em sua área em metros quadrados, utilizando o algoritmo de **Regressão Linear (Linear Regression)**.

## Objetivo

Desenvolver um modelo preditivo capaz de estimar o preço de um imóvel a partir de sua área, aplicando conceitos fundamentais de Machine Learning, preparação de dados, treinamento e avaliação de modelos.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Estrutura do projeto

```text
real-estate-price-prediction/
│
├── imoveis.py
├── imoveis.csv
└── README.md
```

## Metodologia

O desenvolvimento do projeto foi dividido nas seguintes etapas:

1. **Preparação dos dados:** leitura e organização da base de dados utilizando Pandas.
2. **Análise dos dados:** exploração da relação entre a área dos imóveis e seus respectivos preços.
3. **Separação dos dados:** divisão entre conjuntos de treinamento e teste, utilizando `train_test_split`.
4. **Treinamento:** aplicação do algoritmo de Regressão Linear por meio do Scikit-learn.
5. **Avaliação:** utilização da métrica MAE (Mean Absolute Error) para avaliar a diferença média entre os preços previstos e os valores reais.
6. **Visualização:** criação de gráficos para observar a relação entre a área dos imóveis e os preços estimados pelo modelo.

## Resultados

O modelo foi treinado utilizando uma base de dados de 16 registros, com divisão de 80% para treinamento e 20% para teste.

**Métrica de avaliação:**

- MAE (Erro Absoluto Médio): aproximadamente R$ 3.716,05.

O resultado representa o erro absoluto médio das previsões no conjunto de teste.

## Como executar o projeto

**1. Clone o repositório:**

```bash
git clone https://github.com/tavin27/real-estate-price-prediction.git
```

**2. Entre na pasta do projeto:**

```bash
cd real-estate-price-prediction
```

**3. Instale as dependências:**

```bash
pip install pandas numpy matplotlib scikit-learn
```

**4. Execute o projeto:**

```bash
python imoveis.py
```

## Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conceitos importantes de Machine Learning:

- Fundamentos de aprendizado supervisionado.
- Regressão Linear.
- Preparação e exploração de dados.
- Separação entre dados de treinamento e teste.
- Avaliação de modelos utilizando MAE.
- Visualização e interpretação de resultados.

## Próximos passos

- Ampliar a base de dados utilizada no treinamento.
- Explorar novas variáveis que possam influenciar os preços dos imóveis.
- Comparar diferentes algoritmos de regressão.
- Aprimorar a avaliação e a capacidade preditiva do modelo.

---

**Desenvolvido por Otávio Augusto Silva**

Estudante de Sistemas de Informação | Python | Machine Learning | Análise de Dados
