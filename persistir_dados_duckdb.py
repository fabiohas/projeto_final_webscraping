import duckdb
import pandas as pd

def persistir_dados_no_duckdb(csv_file: str, tabela: str, db_file: str = "dados.db"):
    """
    Persiste os dados de um arquivo CSV em uma tabela DuckDB.

    Args:
        csv_file (str): Caminho para o arquivo CSV.
        tabela (str): Nome da tabela onde os dados serão armazenados.
        db_file (str): Caminho para o arquivo DuckDB. Default é "dados.db".
    """
    try:
        # Ler os dados do CSV
        df = pd.read_csv(csv_file)

        # Conectar ao banco de dados DuckDB
        conn = duckdb.connect(db_file)

        # Persistir os dados no banco de dados
        conn.execute(f"CREATE TABLE IF NOT EXISTS {tabela} AS SELECT * FROM df")
        conn.execute(f"INSERT INTO {tabela} SELECT * FROM df")

        print(f"Dados do arquivo '{csv_file}' foram persistidos na tabela '{tabela}' no banco '{db_file}'.")

        # Fechar a conexão
        conn.close()
    except Exception as e:
        print(f"Erro ao persistir os dados: {e}")

if __name__ == "__main__":
    # Exemplo de uso
    persistir_dados_no_duckdb("bbc_israel_gaza_noticias.csv", "noticias_bbc")
    persistir_dados_no_duckdb("precos_brent_2024-01-01_to_2025-12-31.csv", "precos_petroleo")