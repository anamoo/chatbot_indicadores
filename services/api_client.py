import requests

from config.settings import BASE_URL, TIMEOUT
from config.endpoints import ENDPOINTS


def llamar_backend(intent, entities):

    if intent not in ENDPOINTS:
        print("Intent no tiene endpoint:", intent)
        return None

    url = BASE_URL + ENDPOINTS[intent]

    try:

        response = requests.get(
            url,
            params=entities,
            timeout=TIMEOUT
        )

        print("URL:", url)
        print("PARAMS:", entities)
        print("STATUS:", response.status_code)

        if response.status_code != 200:
            print("ERROR BACKEND:", response.text)
            return None

        return response.json()

    except requests.exceptions.ConnectionError:
        print("No se pudo conectar al backend")
        return None

    except requests.exceptions.Timeout:
        print("Tiempo de espera agotado")
        return None