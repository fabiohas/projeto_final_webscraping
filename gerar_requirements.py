import pkgutil
import subprocess
import sys


def gerar_requirements(output_file="requirements.txt"):
    """
    Gera um arquivo requirements.txt com todos os pacotes instalados no ambiente atual
    (neste caso no ambiente que o projeto foi desenvolvido).

    Args:
        output_file (str): Nome do arquivo de saída. Default é "requirements.txt".
    """
    try:
        # Executa o comando pip freeze para listar os pacotes instalados
        result = subprocess.run(
            [sys.executable, "-m", "pip", "freeze"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )

        # Salva a saída no arquivo especificado
        with open(output_file, "w") as f:
            f.write(result.stdout)

        print(f"Arquivo '{output_file}' gerado com sucesso!")
    except subprocess.CalledProcessError as e:
        print("Erro ao gerar o arquivo requirements.txt:", e.stderr)


if __name__ == "__main__":
    gerar_requirements()