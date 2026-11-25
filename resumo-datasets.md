# Dados utilizados na análise

O acervo original contém 239 CSVs do Our World in Data. A pesquisa usa as seis séries abaixo, integradas por `Code` e `Year`, entre 1965 e 2023.

| Indicador | Arquivo em `Datasets/Our World in Data` | Unidade |
|---|---|---|
| Milho | `Agricultural production/ap-maize-corn_production-tonnes_total.csv` | Toneladas |
| Trigo | `Agricultural production/ap-wheat_production-tonnes_total.csv` | Toneladas |
| Arroz | `Agricultural production/ap-rice_production-tonnes_total.csv` | Toneladas |
| Oferta alimentar | `Agricultural production/ap-all_kcal-capita-day_total.csv` | kcal/pessoa/dia |
| Consumo de combustíveis fósseis | `Fossil fuels/ff-all_energy-consumption-TWh_total.csv` | TWh |
| Emissões de CO₂ | `ce_co2-production_fossil-and-land.csv` | Toneladas de CO₂ |

Na fonte de CO₂, selecionamos a coluna `Total (fossil fuels and land-use change)`. A série de energia é o consumo total de carvão, petróleo e gás; não são utilizados valores de importação, exportação ou reservas no modelo.

Os arquivos tratados são recriados pela execução de `main.ipynb`:

- `agricultura.csv`: culturas, soma das três produções e oferta alimentar.
- `combustiveis.csv`: consumo de energia fóssil por país/ano.
- `co2.csv`: emissões de CO₂ por país/ano.
- `painel_pais_ano.csv`: integração das seis séries, ainda com ausências.
- `base_classificacao.csv`: exemplos completos, atributos, valores para auditar o alvo e identificação de treino/teste.

Os sete atributos do modelo são as seis séries do ano de referência e o crescimento agrícola mais recente. `agro_anterior_t`, `agro_seguinte_t` e `crescimento_seguinte_pct` ajudam a conferir os cálculos. O valor do ano seguinte e a classe **não podem ser usados como entradas**.

As classes são `1 = crescimento > 5%` e `0 = crescimento ≤ 5%` da soma de milho, trigo e arroz no ano seguinte. As linhas incompletas são retiradas da base de classificação, sem preencher ausência com zero. O detalhamento da seleção e suas limitações está no notebook.
