import io
import pytest
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_sem_arquivo(client):
    response = client.post("/stats")
    assert response.status_code == 400
    assert response.get_json()["error"] == "Nenhum arquivo enviado"

def test_csv_valido(client):
    csv = b"nome,idade,salario\nAna,28,3000\nBruno,35,5000"
    data = {"file": (io.BytesIO(csv), "dados.csv")}
    response = client.post("/stats", data=data, content_type="multipart/form-data")
    assert response.status_code == 200
    json = response.get_json()
    assert "idade" in json
    assert "salario" in json
    assert json["idade"]["media"] == 31.5