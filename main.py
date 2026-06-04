from flask import Flask, request
import pandas as pd
import io

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "ok"}

@app.route("/stats", methods=["POST"])
def stats():
    file = request.files.get("file")
    if not file:
        return {"error": "Nenhum arquivo enviado"}, 400

    df = pd.read_csv(io.StringIO(file.stream.read().decode("utf-8")))
    
    numericas = df.select_dtypes(include="number")
    if numericas.empty:
        return {"error": "Nenhuma coluna numérica encontrada"}, 400

    resultado = {}
    for coluna in numericas.columns:
        resultado[coluna] = {
            "media": round(numericas[coluna].mean(), 2),
            "mediana": round(numericas[coluna].median(), 2),
            "desvio_padrao": round(numericas[coluna].std(), 2),
            "minimo": round(numericas[coluna].min(), 2),
            "maximo": round(numericas[coluna].max(), 2)
        }

    return resultado

if __name__ == "__main__":
    app.run(debug=True)