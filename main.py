from flask import Flask, request, jsonify
import pandas as pd
import io

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "ok"})

@app.route("/stats", methods=["POST"])
def stats():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    try:
        df = pd.read_csv(io.StringIO(file.stream.read().decode("utf-8")))
    except Exception:
        return jsonify({"error": "Arquivo inválido ou corrompido"}), 400

    if df.empty:
        return jsonify({"error": "O arquivo não contém dados"}), 400

    numericas = df.select_dtypes(include="number")
    if numericas.empty:
        return jsonify({"error": "Nenhuma coluna numérica encontrada"}), 400

    resultado = {}
    for coluna in numericas.columns:
        resultado[coluna] = {
            "media": round(numericas[coluna].mean(), 2),
            "mediana": round(numericas[coluna].median(), 2),
            "desvio_padrao": round(numericas[coluna].std(), 2),
            "minimo": round(numericas[coluna].min(), 2),
            "maximo": round(numericas[coluna].max(), 2)
        }

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)