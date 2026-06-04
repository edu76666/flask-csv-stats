# Flask CSV Stats

API REST que recebe o upload de um arquivo CSV e retorna
estatísticas descritivas das colunas numéricas em JSON.

## Como executar

git clone https://github.com/edu76666/flask-csv-stats
cd flask-csv-stats
pip install -r requirements.txt
python main.py

## Endpoints

POST /stats
- Recebe: arquivo CSV via form-data (campo "file")
- Retorna: JSON com média, mediana, desvio padrão, mínimo e máximo

## Tecnologias

- Python 3.14
- Flask
- Pandas

## Autor

Eduardo Cruz Junior — LinkedIn · GitHub
