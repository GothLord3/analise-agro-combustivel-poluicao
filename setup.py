import os
import sys
import subprocess

def setup_environment():

    # 1. Cria o ambiente virtual se ele não existir
    if not os.path.exists(".venv"):
        print("Criando ambiente virtual '.venv'...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        print("Ambiente .venv criado com sucesso!")
    else:
        print("O ambiente '.venv' já existe.")

    # 2. Define o caminho do Python dentro do venv
    if os.name == "nt":  # Windows
        venv_python = os.path.join(".venv", "Scripts", "python.exe")
    else:  # Linux / Mac
        venv_python = os.path.join(".venv", "bin", "python")

    # 3. Atualiza o pip e instala as dependências
    print("Atualizando o pip e instalando dependências, aguarde...")
    subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([venv_python, "-m", "pip", "install", "ipykernel"], check=True)

    if os.path.exists("requirements.txt"):
        subprocess.run([venv_python, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Todas as dependências do 'requirements.txt' foram instaladas!")
    else:
        print("'requirements.txt' não encontrado. Nenhuma biblioteca extra foi instalada. Por favor, reveja sua instalação, ou reporte o problema abrindo uma issue no GitHub.")

    print("\nTudo pronto! Abra o VS Code, abra seu .ipynb e selecione o kernel '.venv' para executar localmente.")

if __name__ == "__main__":
    setup_environment()
