# DomTech Forger

**DomTech Forger** é uma ferramenta de linha de comando em Python projetada para automatizar a criação e atualização de projetos de software. Ele lê um único arquivo de texto contendo o código-fonte de múltiplos arquivos e os distribui na estrutura de diretórios correta, além de, opcionalmente, fazer o commit das alterações no Git.

Este projeto nasceu para acelerar o desenvolvimento iterativo, especialmente ao colaborar com Large Language Models (LLMs).

## Funcionalidades

* Cria automaticamente a estrutura de diretórios necessária.
* Distribui o código-fonte para os arquivos corretos a partir de um único arquivo de origem.
* Protege arquivos sensíveis como `.env` de serem sobrescritos.
* Opcionalmente, faz o `git commit` das alterações com uma mensagem de commit extraída do próprio arquivo de origem.

## Instalação e Uso

1.  **Clone o repositório:**
    ```sh
    git clone https://github.com/DomTechSolutions/domtech-forger.git
    cd domtech-forger
    ```

2.  **Crie um arquivo de atualização** (ex: `meu_projeto_update.txt`) seguindo o formato especificado em `PROMPT_TEMPLATE.md`.

3.  **Execute o script:**
    O script deve ser executado como um módulo a partir da pasta raiz do repositório.

    * **Para atualizar e fazer o commit (padrão):**
        ```sh
        python -m src.domtech_forger.main meu_projeto_update.txt
        ```

    * **Para apenas atualizar os arquivos, sem fazer o commit:**
        ```sh
        python -m src.domtech_forger.main meu_projeto_update.txt --commit=false
        ```

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
