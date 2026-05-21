# Laboratório API IBGE + PySpark

Este laboratório busca dados da API do IBGE, salva em CSV organizado por data e lê os dados usando PySpark.

## Estrutura

- `labs/ibge_population_lab/` → código Python do laboratório.
- `data/YYYY-MM-DD/` → pasta criada automaticamente com CSV.
- `requirements.txt` → dependências do laboratório.
- `.gitignore` → ignora dados e cache Python.

## Como rodar

1. Instale dependências:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt