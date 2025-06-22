# Prompt Template para Geração de Código Compatível com o DomTech Forger

Use o seguinte template ao instruir um Large Language Model (LLM) para gerar o código-fonte de um projeto completo em um único bloco de texto. Isso garantirá que a saída seja compatível com a ferramenta de automação `DomTech Forger`.

## Template do Prompt

"Por favor, gere a estrutura completa de arquivos para o projeto [NOME DO PROJETO]. A saída deve ser um único bloco de código. Cada arquivo deve ser precedido por um cabeçalho no formato `## Arquivo: caminho/completo/do/arquivo.ext` e o conteúdo de cada arquivo deve ser separado por uma linha contendo apenas `---`.

Se houver uma mensagem de commit sugerida, ela deve estar em seu próprio bloco, precedida por `## Mensagem de Commit:` e separada por `---`."

**Exemplo de Estrutura:**

```
## Arquivo: src/main.py

print("Olá, Mundo!")

---
## Arquivo: README.md

# Meu Projeto

Este é um projeto de exemplo.

---
## Mensagem de Commit:

feat: cria estrutura inicial do projeto

Adiciona os arquivos `main.py` e `README.md` para a configuração inicial do projeto.
```
