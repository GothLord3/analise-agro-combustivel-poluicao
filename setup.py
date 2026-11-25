import os
import sys
import subprocess
from pathlib import Path

def setup_environment():
    # Usa a pasta do script, mesmo quando ele é chamado de outro diretório.
    project_dir = Path(__file__).resolve().parent
    venv_dir = project_dir / ".venv"

    # 1. Cria o ambiente virtual se ele não existir
    if not venv_dir.exists():
        print("Criando ambiente virtual '.venv'...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
        print("Ambiente .venv criado com sucesso!")
    else:
        print("O ambiente '.venv' já existe.")

    # 2. Define o caminho do Python dentro do venv
    if os.name == "nt":  # Windows
        venv_python = venv_dir / "Scripts" / "python.exe"
    else:  # Linux / Mac
        venv_python = venv_dir / "bin" / "python"

    # 3. Atualiza o pip e instala as dependências
    print("Atualizando o pip e instalando dependências, aguarde...")
    subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    requirements = project_dir / "requirements.txt"
    if requirements.exists():
        subprocess.run([venv_python, "-m", "pip", "install", "-r", str(requirements)], check=True)
        print("Todas as dependências do 'requirements.txt' foram instaladas!")
    else:
        print("'requirements.txt' não encontrado. Nenhuma biblioteca extra foi instalada. Por favor, reveja sua instalação, ou reporte o problema abrindo uma issue no GitHub.")

    print("\nTudo pronto! Abra o VS Code, abra seu .ipynb e selecione o kernel '.venv' para executar localmente.")

if __name__ == "__main__":
    setup_environment()
