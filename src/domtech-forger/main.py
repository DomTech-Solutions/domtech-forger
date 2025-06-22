import os
import re
import subprocess
import argparse

# --- CONFIGURAÇÃO ---
FILE_HEADER_PATTERN = re.compile(r'## Arquivo: (.*?)\n')
COMMIT_HEADER_PATTERN = re.compile(r'## Mensagem de Commit:\n')

def run_git_command(command):
    """Executa um comando git e verifica se foi bem-sucedido."""
    try:
        subprocess.run(command, check=True, capture_output=True, text=True, encoding='utf-8')
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar o comando git: {' '.join(command)}")
        print(f"   Saída de erro: {e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ Erro: O comando 'git' não foi encontrado. Verifique se o Git está instalado e no seu PATH.")
        return False

def apply_updates(source_file, perform_commit):
    """
    Lê o arquivo de código-fonte consolidado, distribui o conteúdo
    e, opcionalmente, faz o commit das alterações.
    """
    print(f"⚙️  Iniciando a atualização do projeto a partir do arquivo '{source_file}'...")

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
            filepath = file_match.group(1).strip()
            code_content = block[file_match.end():].strip()

            if filepath == '.env':
                if os.path.exists(filepath):
                    print(f"⚠️  Arquivo '{filepath}' já existe. Pulando para proteger seus segredos.")
                    continue
                else:
                    print(f"✨  Criando arquivo de exemplo '{filepath}'. Lembre-se de preenchê-lo.")

            try:
                directory = os.path.dirname(filepath)
                if directory:
                    os.makedirs(directory, exist_ok=True)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(code_content)

                print(f"✔️ Arquivo '{filepath}' criado/atualizado com sucesso.")
                files_created_or_updated += 1
            except IOError as e:
                print(f"❌ Erro ao escrever o arquivo '{filepath}': {e}")

        elif commit_match:
            commit_message = block[commit_match.end():].strip()
            print("✔️ Mensagem de commit encontrada.")

    print(f"\n🎉 Processo de arquivos concluído! {files_created_or_updated} arquivos foram atualizados.")

    if perform_commit and commit_message:
        print("\n🚀 Iniciando processo de versionamento com Git...")
        print("   Adicionando todos os arquivos ao stage...")
        if run_git_command(['git', 'add', '.']):
            print(f"   Fazendo commit com a mensagem:\n---INÍCIO---\n{commit_message}\n---FIM---")
            if run_git_command(['git', 'commit', '-m', commit_message]):
                print("✅ Commit realizado com sucesso!")
    elif perform_commit and not commit_message:
        print("\n⚠️ O commit foi solicitado, mas nenhuma mensagem de commit foi encontrada no arquivo de origem.")
    else:
        print("\nℹ️  O commit automático não foi solicitado. Processo finalizado.")


def main():
    """Função principal para analisar os argumentos e iniciar o script."""
    parser = argparse.ArgumentParser(description="Atualiza os arquivos do projeto a partir de um arquivo de origem e opcionalmente faz o commit.")

    parser.add_argument(
        'source_file',
        type=str,
        default='update_source.txt',
        nargs='?',
        help="Caminho para o arquivo de texto com as atualizações. Padrão: 'update_source.txt'"
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
        perform_commit=(args.commit == 'true')
    )

if __name__ == "__main__":
    main()
