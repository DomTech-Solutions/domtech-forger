# PoliticaMente API

Este é o repositório do backend para a plataforma **PoliticaMente**. Construído com FastAPI e Python, este serviço é responsável por toda a lógica de negócio, segurança e gestão de dados da aplicação.

## Filosofia

O PoliticaMente nasceu como um projeto **open source** com foco total em **segurança, privacidade e transparência**. Acreditamos que, ao lidar com dados sensíveis, a melhor abordagem é permitir que a comunidade audite e contribua para a robustez da plataforma.

## Começando

Siga estas instruções para ter uma cópia do projeto funcionando na sua máquina local para desenvolvimento e testes (ambiente WSL/Linux recomendado).

### Pré-requisitos

* Python 3.9+ (instalado no WSL)
* `pip` e `venv` (instalados no WSL com `sudo apt install python3-pip python3-venv`)

### Instalação

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/politicamente-app/politicamente-api.git](https://github.com/politicamente-app/politicamente-api.git)
    cd politicamente-api
    ```

2.  **Crie e ative um ambiente virtual:**
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```sh
    # Dependências da Aplicação
    pip install fastapi "uvicorn[standard]" "pydantic[email]" "passlib[bcrypt]" sqlalchemy psycopg2-binary python-dotenv pydantic-settings "python-jose[cryptography]" python-multipart

    # Dependências de Teste
    pip install pytest httpx
    ```
4.  **Crie o arquivo `.env`:**
    * Crie um arquivo chamado `.env` na pasta raiz do projeto.
    * Dentro dele, adicione sua string de conexão do Supabase e as configurações de segurança:
        ```
        DATABASE_URL="postgresql://postgres.[SEU_ID]:[SUA_SENHA]@[aws-0-sa-east-1.pooler.supabase.com:5432/postgres](https://aws-0-sa-east-1.pooler.supabase.com:5432/postgres)"

        # Execute `openssl rand -hex 32` no terminal para gerar uma chave segura
        SECRET_KEY="sua_chave_secreta_aqui"
        ALGORITHM="HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES=60
        ```

### Executar a Aplicação

1.  Com seu ambiente virtual ativado, execute o servidor de desenvolvimento Uvicorn a partir da pasta raiz (`politicamente-api/`):
    ```sh
    uvicorn app.main:app --reload
    ```
    A flag `--reload` faz com que o servidor reinicie automaticamente após cada alteração no código.

2.  Abra seu navegador e acesse [http://127.0.0.1:8000](http://127.0.0.1:8000). Você deverá ver a mensagem: `{"message":"Bem-vindo à API do PoliticaMente"}`.

### Executar os Testes

1.  Com seu ambiente virtual ativado, execute o Pytest a partir da pasta raiz (`politicamente-api/`):
    ```sh
    pytest
    ```
    O Pytest irá descobrir e executar automaticamente todos os testes dentro da pasta `tests/`.