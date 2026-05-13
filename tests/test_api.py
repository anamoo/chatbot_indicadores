import requests

BASE_URL = "http://localhost:8000/indicadores"

def test_egresados():
    params = {
        "carrera": "sistemas",
        "anio": 2024,
        "semestre": 1
    }

    response = requests.get(f"{BASE_URL}/egresados", params=params)

    assert response.status_code == 200
    data = response.json()

    assert "cantidad_egresados" in data
    assert data["anio"] == 2024
    assert data["semestre"] == 1


def test_titulados():
    params = {
        "carrera": "sistemas",
        "anio": 2024,
        "semestre": 1
    }

    response = requests.get(f"{BASE_URL}/titulados", params=params)

    assert response.status_code == 200
    data = response.json()

    assert "cantidad_titulados" in data


def test_matricula():
    params = {
        "carrera": "sistemas",
        "anio": 2024,
        "semestre": 1
    }

    response = requests.get(f"{BASE_URL}/matricula", params=params)

    assert response.status_code == 200
    data = response.json()

    assert "ni_h" in data
    assert "ni_m" in data
    assert "re_h" in data
    assert "re_m" in data


def test_docentes():
    params = {
        "departamento": "sistemas",
        "anio": 2024,
        "semestre": 1
    }

    response = requests.get(f"{BASE_URL}/docentes", params=params)

    assert response.status_code == 200
    data = response.json()

    assert "total_docentes" in data
    assert "tc" in data
    assert "ct" in data
    assert "mt" in data
    assert "ha" in data