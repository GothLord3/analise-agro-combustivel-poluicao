# Análise da correlação entre agronegócio, combustíveis fósseis e poluição

Trabalho de Programação para Ciência de Dados I, ministrada por Ronaldo Rodrigues Martins, no curso Ciência de Dados para o Agronegócio da FATEC de Catanduva.

**Integrantes:** Clara D. Gonzaga, Gabriel G. Lima, Mateus e Rodrigo S. Bertolini.

**Turma:** CDA - Ciência de Dados, 1º ano (curso anual).

Essa pesquisa reúne dados de produção agrícola, consumo de energia fóssil e emissões de CO₂ do Our World in Data. Na etapa supervisionada, comparamos quatro classificadores para responder:

**A partir dos indicadores de um país e do crescimento agrícola mais recente, é possível prever se a produção conjunta de milho, trigo e arroz crescerá mais de 5% no ano seguinte?**

---

### O que foi analisado

- Produção de milho, trigo e arroz, em toneladas.
- Oferta de energia alimentar, em kcal/pessoa/dia.
- Consumo total de carvão, petróleo e gás, em TWh.
- Emissões de CO₂ de combustíveis fósseis e mudança no uso da terra, em toneladas.

Os dados são integrados por país/território e ano, no período de **1965 a 2023**. A soma das três culturas representa somente esse recorte do agro. Energia e emissões são totais nacionais de vários setores.

O alvo tem duas classes: **1 = crescimento > 5%** e **0 = crescimento ≤ 5%**, incluindo estabilidade e queda. Usamos sete atributos: os seis indicadores do ano de referência e o crescimento agrícola do ano anterior para o de referência. Os valores do ano seguinte servem apenas para obter a classe real.

### Notebook

A pesquisa está documentada em [main.ipynb](main.ipynb), com os dados, gráficos, implementação dos classificadores e discussão dos resultados. O roteiro de estudo do grupo fica separado em `ROTEIRO_APRESENTACAO.txt`.

### Resultados desta execução

A base final contém **3.382 exemplos de 91 países/territórios**. Os anos-alvo até 2013 ficaram no treino (2.596 exemplos), e de 2014 a 2023 no teste (786 exemplos). A normalização foi ajustada somente no treino.

| Classificador | Acurácia no teste | Precisão da classe 1 | Recall da classe 1 |
|---|---:|---:|---:|
| Árvore de Decisão | 66,79% | 62,50% | 22,65% |
| Random Forest | 63,36% | 49,79% | 41,81% |
| KNN | 58,40% | 43,33% | 45,30% |
| Naive Bayes | 40,84% | 36,95% | 87,80% |

A referência que sempre prevê a classe mais comum do treino obteve **63,49%** de acurácia. A Árvore de Decisão foi a melhor dos quatro por acurácia e permitiu visualizar regras simples, mas deixou de identificar muitos crescimentos superiores a 5%. O notebook discute esse limite, os erros dos demais modelos e o sobreajuste observado na Random Forest. Os resultados não demonstram causalidade nem garantem previsão de safras futuras.

As tabelas completas e as matrizes de confusão ficam em [Resultados/](Resultados/).

---

### Para rodar localmente

Com Python 3.12 disponível, execute o [setup.py](setup.py):

```powershell
python setup.py
```

O script cria o ambiente `.venv` na pasta do projeto e instala as dependências de [requirements.txt](requirements.txt). No VS Code, abra a pasta do projeto, escolha o Python de `.venv` como kernel e execute o notebook de cima para baixo.

Para abrir pelo JupyterLab no Windows:

```powershell
.\.venv\Scripts\python.exe -m jupyterlab main.ipynb
```

No Linux ou macOS:

```bash
python3 setup.py
.venv/bin/python -m jupyterlab main.ipynb
```

As versões usadas estão fixadas em `requirements.txt` e registradas em [Resultados/versoes.csv](Resultados/versoes.csv). O notebook não precisa de chave de API nem de arquivo `.env`.

### Para o ambiente Colab

Abra `main.ipynb` no [Google Colab](https://colab.research.google.com/), coloque a pasta `Datasets` em `/content/Datasets` e execute de cima para baixo. Se necessário, use a célula comentada de instalação ou instale as versões de `requirements.txt`. As versões do ambiente podem influenciar os resultados.

### Arquivos de dados

O acervo contém **239 CSVs originais**, baixados pelo grupo. Somente os seis arquivos especificados no notebook entram nesta análise. O [resumo dos datasets](resumo-datasets.md) identifica essa seleção.

A execução recria os arquivos de `Datasets/Tratados` no recorte de 1965 a 2023, incluindo `base_classificacao.csv`, e os resultados em `Resultados`. Os CSVs originais são preservados.

### Fontes e metodologia

- [Agricultural Production](https://ourworldindata.org/agricultural-production), Our World in Data.
- [Fossil fuels](https://ourworldindata.org/grapher/fossil-fuels), Our World in Data.
- [CO₂ emissions](https://ourworldindata.org/co2-emissions), Our World in Data.
- Materiais das Unidades 2 a 4 de Princípios de Ciência de Dados, professor Ronaldo Rodrigues Martins: correlação, árvores, KNN, Naive Bayes, ensembles e avaliação de classificadores. As aulas usadas estão identificadas no notebook.

Foram utilizados os arquivos já presentes no repositório. As páginas das fontes podem disponibilizar versões atualizadas dos dados.
