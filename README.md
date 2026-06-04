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
