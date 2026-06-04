# Flask CSV Stats
API REST que recebe o upload de um arquivo CSV e retorna estatísticas descritivas das colunas numéricas em JSON.

## Como executar
```bash
git clone https://github.com/edu76666/flask-csv-stats
cd flask-csv-stats
pip install -r requirements.txt
python main.py
```

## Endpoints

### POST /stats

Recebe um arquivo CSV via form-data e retorna estatísticas descritivas das colunas numéricas.

**Request**
- Campo: `file` (form-data)
- Formato: `.csv`

**Exemplo com curl**
```bash
curl -X POST http://localhost:5000/stats \
  -F "file=@dados.csv"
```

**Resposta de sucesso (200)**
```json
{
  "idade": {
    "media": 28.5,
    "mediana": 27.0,
    "desvio_padrao": 4.2,
    "minimo": 22.0,
    "maximo": 35.0
  }
}
```

**Erros possíveis**
| Status | Mensagem |
|--------|----------|
| 400 | Nenhum arquivo enviado |
| 400 | Arquivo inválido ou corrompido |
| 400 | O arquivo não contém dados |
| 400 | Nenhuma coluna numérica encontrada |

## Testes
```bash
pytest tests/
```

## Tecnologias
- Python 3.14
- Flask
- Pandas

## Autor
Eduardo Cruz Junior — LinkedIn · GitHub
