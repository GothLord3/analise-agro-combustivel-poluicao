# Analise da correlação entre agronegócio, combustivel fóssil e poluicao
Análise correlacional entre agronegócio, energia de combustível fóssil e poluição, por meio de um modelo preditivo

Essa pesquisa, tem como objetivo, a criação de um modelo preditivo de analise supervisionada, que seja capaz de investigar a correlação entre:

- Produção e consumo das culturas agrícolas.
 - Produção, consumo, importação e exportação de combustíveis fósseis.
 - Produção de CO₂ provenientes de alteração do solo, e combustíveis fósseis.

Referente a matéria de '*Programação para Ciência de Dados I*', ministrada por '*Ronaldo Rodrigues Martins*', perante o curso '*Ciência de Dados para o Agronegócio*' da 'Faculdade de Tecnologia (FATEC) de Catanduva'.

 ---
### Atual Estado da análise:

Em meio a data de 10/11/26, essa pesquisa se encontra tendo em seu foco, as seguintes fontes:

- Produção da *cultura agricola milho* em *toneladas* **(t)**.
- Produçaõ da *cultura agricola trigo* em *toneladas* **(t)**.
- Produção da *cultura agricola arroz* em *toneladas* **(t)**.
- Oferta de consumo média em *quilocalorias por pessoa diariamente* **(kcal/pessoa/dia)**.
- Consumo médio de combustiveis fósseis *(sendo eles: carvão, gás e petróleo)* em *terawatts por hora* **(twh)**.
- Emissão média de *CO₂* na atmosfera *(sendo dividido em: emissão por fontes de combustivel fóssil, e emissão por desmatamento / alteração de solo)* em toneladas **(t)**.

Sendo todas organizadas e agregados no formato '**país/ano**', no período de **1961** á **2023**.

---
### Replicação dos resultados:

Para a replicação dos resultados obtidos por meio desta analise, efetue os seguintes passos:

---

### Para o ambiente colab:

Abra o arquivo .ipynb principal ([main.ipynb](main.ipynb)) no [Google Colab](https://colab.research.google.com/).
Salve a pasta [Datasets/](Datasets/) em "/content/" dentro da sua instância do Google Colab.
Agora você pode prosseguir com as instruções presentes no notebook.

---

### Para rodar localmente:

Execute o arquivo [setup.py](setup.py) diretamente no seu terminal ou em uma IDE

Em Windows:
``` python caminho/setup.py ```

Linux/Mac OS:
``` python3 caminho/setup.py ```

Ele irá criar o ambiente .venv, e instalar os requirementos e dependências em [requirements.txt](requirements.txt).
Depois, basta escolher o .venv como interpretador de Python no VSCode.
Agora você pode executar o [main.ipynb](main.ipynb) livremente.

---
### Inventário

Atualemnte, a pasta [Datasets/](Datasets/) contém 239 datasets, baixados diretamente do [Our World in Data](https://ourworldindata.org/). 
<!-- Para uma visão mais detalhada de todos esses datasets, utilize o resumo presente em [resumo-datasets.md](resumo-datasets.md). -->

---
### Dados utilizados

Todos os datasets utilizados para essa análise, foram adquiridos de 3 principais char no [Our World in Data](https://ourworldindata.org/), sendo eles:

- [Agricultural Production](https://ourworldindata.org/agricultural-production) - Hannah Ritchie, Pablo Rosado e Max Roser (Our World in Data, 2023).
- [Fossil fuels](https://ourworldindata.org/grapher/fossil-fuels) - Hannah Ritchie, Pablo Rosado e Max Roser (Our World in Data, 2023 - dados de: Energy Institute, EIA, Etemad & Luciani, e Smil).
- [CO₂ emissions](https://ourworldindata.org/co2-emissions) - Hannah Ritchie e Max Roser (Our World in Data, 2020).