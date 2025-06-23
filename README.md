# DomTech Forger

**DomTech Forger** é uma ferramenta de linha de comando em Python projetada para automatizar a criação e atualização de projetos de software. Ele lê um único arquivo de texto contendo o código-fonte de múltiplos arquivos e os distribui na estrutura de diretórios correta, além de, opcionalmente, fazer o commit das alterações no Git.

Este projeto nasceu para acelerar o desenvolvimento iterativo, especialmente ao colaborar com Large Language Models (LLMs). É uma ferramenta da **Dom Tech Solutions**.

## Funcionalidades

* Cria automaticamente a estrutura de diretórios em um diretório de destino especificado.
* Distribui o código-fonte para os arquivos corretos a partir de um único arquivo de origem.
* Protege arquivos sensíveis como `.env` de serem sobrescritos.
* Opcionalmente, faz o `git commit` das alterações no repositório de destino com uma mensagem extraída do próprio arquivo de origem.

## Instalação e Uso

1.  **Clone o repositório do DomTech Forger:**
    ```sh
    git clone [https://github.com/DomTechSolutions/domtech-forger.git](https://github.com/DomTechSolutions/domtech-forger.git)
    ```

2.  **Crie um arquivo de atualização** (ex: `politicamente_update.txt`) em qualquer lugar, seguindo o formato especificado em `PROMPT_TEMPLATE.md`.

3.  **Execute o script:**
    Navegue até a pasta do seu projeto **alvo** (ex: `politicamente-api`) e execute o script `DomTech Forger` a partir de lá, especificando o caminho para o arquivo de atualização.

    * **Para atualizar e fazer o commit (padrão):**
        ```sh
        python /caminho/para/domtech-forger/src/domtech_forger/main.py /caminho/para/politicamente_update.txt
        ```

    * **Para apenas atualizar os arquivos, sem fazer o commit:**
        ```sh
        python /caminho/para/domtech-forger/src/domtech_forger/main.py /caminho/para/politicamente_update.txt --commit=false
        ```
    *Obs: Uma forma mais avançada seria adicionar a pasta do `domtech-forger` ao seu `PATH` do sistema para poder chamá-lo de qualquer lugar.*

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
