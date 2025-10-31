# Projeto de Web Scraping e Extração de Dados de Preços do Petróleo

## Descrição Geral

Este projeto foi desenvolvido para realizar duas tarefas principais:

1. **Web Scraping de Notícias da BBC**: Um notebook foi criado para extrair notícias relacionadas ao tópico "Israel e Gaza" diretamente do site da BBC. As notícias são coletadas com informações como título, URL, resumo e timestamp de coleta.
2. **Extração de Dados de Preços do Petróleo**: Um script Python foi desenvolvido para obter os preços diários do petróleo (WTI e Brent) em um intervalo de datas especificado, utilizando a biblioteca `yfinance`.
3. **Geração Automática de Requirements**: Um script Python foi criado para gerar automaticamente um arquivo `requirements.txt` com todas as dependências instaladas no ambiente.
4. **Persistência de Dados em DuckDB**: Um script Python foi desenvolvido para salvar os dados gerados pelo notebook e pelo script Python em um banco de dados DuckDB.

---

## Detalhes do Notebook: `scrapping_noticias_bbc.ipynb`

### Funcionalidades:

- **Aceitação Automática de Cookies**: O notebook utiliza a biblioteca `playwright` para navegar no site da BBC e aceitar automaticamente os cookies.
- **Extração de Notícias**: As notícias são extraídas com base em sua posição visual na página, garantindo que apenas os links relevantes sejam coletados.
- **Salvamento em CSV**: As notícias coletadas são salvas em um arquivo CSV com as seguintes colunas:
  - `titulo`: O título da notícia.
  - `url`: O link para a notícia.
  - `mini_resumo`: Um breve resumo da notícia.
  - `timestamp_coleta`: O horário em que a notícia foi coletada.

### Tecnologias Utilizadas:

- `playwright`: Para automação de navegação na web.
- `asyncio`: Para lidar com operações assíncronas.
- `csv`: Para salvar os dados extraídos em um arquivo.

---

## Detalhes do Script Python: `extrair_dados_petroleo.py`

### Funcionalidades:

- **Extração de Dados do Yahoo Finance**: O script utiliza a biblioteca `yfinance` para baixar os preços diários do petróleo (WTI e Brent).
- **Parâmetros Personalizáveis**: O usuário pode especificar:
  - A série desejada (`wti` ou `brent`).
  - A data inicial e final para a extração.
- **Retorno em DataFrame**: Os dados extraídos são retornados como um `DataFrame` do pandas, com as seguintes colunas:
  - `ds`: Datas dos preços.
  - `price`: Preço do petróleo no dia correspondente.
- **Salvamento Opcional**: Os dados podem ser salvos em um arquivo CSV.

### Tecnologias Utilizadas:

- `yfinance`: Para acessar os dados financeiros do Yahoo Finance.
- `pandas`: Para manipulação e análise dos dados extraídos.

---

## Detalhes do Script Python: `gerar_requirements.py`

### Funcionalidades:

- **Geração Automática de Requirements**: O script executa o comando `pip freeze` para listar todas as dependências instaladas no ambiente atual e salva essas informações em um arquivo `requirements.txt`.

### Como Utilizar:

1. Execute o script:
   ```bash
   python gerar_requirements.py
   ```
2. O arquivo `requirements.txt` será gerado no diretório atual.

---

## Detalhes do Script Python: `persistir_dados_duckdb.py`

### Funcionalidades:

- **Persistência de Dados**: O script lê os dados de arquivos CSV e os salva em tabelas de um banco de dados DuckDB.
- **Parâmetros Personalizáveis**:
  - `csv_file`: Caminho para o arquivo CSV.
  - `tabela`: Nome da tabela onde os dados serão armazenados.
  - `db_file`: Caminho para o arquivo DuckDB (padrão: `dados.db`).

### Como Utilizar:

1. Execute o script diretamente para persistir os dados de exemplo:
   ```bash
   python persistir_dados_duckdb.py
   ```
2. O banco de dados DuckDB será atualizado com as tabelas especificadas.

---

## Como Utilizar

### Notebook de Web Scraping

1. Certifique-se de ter o `playwright` instalado:
   ```bash
   pip install playwright
   playwright install
   ```
2. Abra o notebook `scrapping_noticias_bbc.ipynb` e execute as células para coletar as notícias.
3. O arquivo CSV será salvo no diretório especificado.

### Script de Extração de Dados do Petróleo

1. Certifique-se de ter o `yfinance` instalado:
   ```bash
   pip install yfinance
   ```
2. Importe a função `extrair_dados_petroleo` no seu código ou notebook:
   ```python
   from extrair_dados_petroleo import extrair_dados_petroleo
   ```
3. Chame a função com os parâmetros desejados:
   ```python
   dados = extrair_dados_petroleo("brent", "2024-01-01", "2024-12-31")
   ```
4. Salve os dados em um arquivo CSV, se necessário:
   ```python
   dados.to_csv("precos_brent_2024.csv", index=False)
   ```

### Script de Persistência de Dados

1. Certifique-se de ter o `duckdb` instalado:
   ```bash
   pip install duckdb
   ```
2. Execute o script `persistir_dados_duckdb.py` para salvar os dados no banco DuckDB.

---

## Requisitos

- Python 3.8 ou superior.
- Bibliotecas necessárias:
  - `playwright`
  - `yfinance`
  - `pandas`
  - `duckdb`

---

## Estrutura do Projeto

```
projeto_final/
├── scrapping_noticias_bbc.ipynb  # Notebook para web scraping de notícias.
├── extrair_dados_petroleo.py     # Script para extração de preços do petróleo.
├── gerar_requirements.py         # Script para gerar o arquivo requirements.txt.
├── persistir_dados_duckdb.py     # Script para persistir dados em DuckDB.
├── README.md                     # Documentação do projeto.
├── bbc_israel_gaza_noticias.csv  # Arquivo CSV gerado pelo notebook.
├── precos_brent_2024-01-01_to_2025-12-31.csv  # Exemplo de saída do script.
├── dados.db                      # Banco de dados DuckDB gerado.
```
