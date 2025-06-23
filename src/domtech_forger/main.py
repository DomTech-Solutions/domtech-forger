import os
import re
import subprocess
import argparse

# --- CONFIGURAÇÃO ---
FILE_HEADER_PATTERN = re.compile(r'## Arquivo: (.*?)\n')
COMMIT_HEADER_PATTERN = re.compile(r'## Mensagem de Commit:\n')
# Lista de arquivos e diretórios que não devem ser sobrescritos se já existirem.
PROTECTED_PATHS = ['.env', 'PROMPT_TEMPLATE.md']

def run_git_command(command, target_dir):
    """Executa um comando git dentro de um diretório alvo."""
    try:
        subprocess.run(command, check=True, capture_output=True, text=True, encoding='utf-8', cwd=target_dir)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar o comando git: {' '.join(command)} em '{target_dir}'")
        print(f"   Saída de erro: {e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ Erro: O comando 'git' não foi encontrado. Verifique se o Git está instalado e no seu PATH.")
        return False

def apply_updates(source_file, destination_dir, perform_commit):
    """
    Lê o arquivo de código-fonte consolidado, distribui o conteúdo
    e, opcionalmente, faz o commit das alterações no diretório de destino.
    """
    print(f"⚙️  Iniciando atualização do projeto em '{destination_dir}'...")
    print(f"   Usando o arquivo de origem: '{source_file}'")

    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo de origem '{source_file}' não foi encontrado.")
        print("Por favor, verifique o caminho e tente novamente.")
        return

    blocks = content.split('\n---\n')
    files_created_or_updated = 0
    commit_message = None

    for block in blocks:
        if not block.strip():
            continue

        file_match = FILE_HEADER_PATTERN.search(block)
        commit_match = COMMIT_HEADER_PATTERN.search(block)

        if file_match:
            relative_path = file_match.group(1).strip()
            # Constrói o caminho completo dentro do diretório de destino
            full_path = os.path.join(destination_dir, relative_path)

            code_content = block[file_match.end():].strip()

            # --- LÓGICA DE PROTEÇÃO DE ARQUIVOS ---
            if relative_path in PROTECTED_PATHS:
                if os.path.exists(full_path):
                    print(f"⚠️  Arquivo protegido '{full_path}' já existe. Pulando para manter a versão local.")
                    continue
                else:
                    print(f"✨  Criando arquivo de exemplo para '{full_path}'. Lembre-se de preenchê-lo.")

            try:
                directory = os.path.dirname(full_path)
                if directory:
                    os.makedirs(directory, exist_ok=True)

                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(code_content)

                print(f"✔️ Arquivo '{full_path}' criado/atualizado com sucesso.")
                files_created_or_updated += 1
            except IOError as e:
                print(f"❌ Erro ao escrever o arquivo '{full_path}': {e}")

        elif commit_match:
            commit_message = block[commit_match.end():].strip()
            print("✔️ Mensagem de commit encontrada.")

    print(f"\n🎉 Processo de arquivos concluído! {files_created_or_updated} arquivos foram atualizados.")

    if perform_commit and commit_message:
        print(f"\n🚀 Iniciando processo de versionamento em '{destination_dir}'...")
        print("   Adicionando todos os arquivos ao stage...")
        if run_git_command(['git', 'add', '.'], destination_dir):
            print(f"   Fazendo commit com a mensagem:\n---INÍCIO---\n{commit_message}\n---FIM---")
            if run_git_command(['git', 'commit', '-m', commit_message], destination_dir):
                print("✅ Commit realizado com sucesso!")
    elif perform_commit and not commit_message:
        print("\n⚠️ O commit foi solicitado, mas nenhuma mensagem de commit foi encontrada no arquivo de origem.")
    else:
        print("\nℹ️  O commit automático não foi solicitado. Processo finalizado.")

def main():
    """Função principal para analisar os argumentos e iniciar o script."""
    parser = argparse.ArgumentParser(description="Atualiza arquivos de um projeto alvo a partir de um arquivo de origem e opcionalmente faz o commit.")

    parser.add_argument(
        'source_file',
        type=str,
        help="Caminho para o arquivo de texto com as atualizações."
    )

    parser.add_argument(
        '--destination',
        type=str,
        default='.', # Padrão: diretório atual
        help="Caminho para o diretório do projeto alvo onde as atualizações serão aplicadas. Padrão: diretório atual."
    )

    parser.add_argument(
        '--commit',
        type=str,
        choices=['true', 'false'],
        default='true',
        help="Define se o script deve fazer o commit das alterações. Padrão: true"
    )

    args = parser.parse_args()

    apply_updates(
        source_file=args.source_file,
        destination_dir=args.destination,
        perform_commit=(args.commit == 'true')
    )

if __name__ == "__main__":
    main()