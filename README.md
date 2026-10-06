# Catálogo de Séries

API simples para cadastrar e consultar séries, feita com FastAPI e Pydantic.

## Tecnologias

- Python
- FastAPI
- Pydantic
- JSON para armazenar e listar séries
- SQLite usado pela busca por título

## Como executar

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Crie um arquivo `series.json` na pasta do projeto com o conteúdo inicial:

   ```json
   []
   ```

3. Inicie a API:

   ```bash
   uvicorn main:app --reload
   ```

4. Acesse `http://127.0.0.1:8000/docs` para testar as rotas pela documentação interativa do FastAPI.

## Rotas disponíveis

| Método | Caminho | Descrição |
|---|---|---|
| GET | `/` | Mensagem inicial da API |
| POST | `/series` | Cadastra uma série e grava a lista em `series.json` |
| GET | `/series` | Lista as séries do arquivo `series.json` |
| GET | `/series/{titulo}` | Busca uma série pelo título no banco `series.db` |

O corpo enviado para `POST /series` deve ser um JSON com este formato:

```json
{
  "titulo": "Nome da série",
  "genero": "Drama",
  "ano_lancamento": 2021,
  "temporadas": 3
}
```

O modelo valida que o ano de lançamento seja maior que 1900 e que o número de temporadas seja positivo.

> **Observação:** a busca por título consulta a tabela `catalogo` no arquivo `series.db`. Essa tabela precisa existir e estar configurada no SQLite; o projeto ainda não cria nem preenche essa tabela automaticamente.
