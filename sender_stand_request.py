import configuration
import data
import requests


# 1. Función para crear un nuevo usuario
def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )


# 2. Función para crear un kit de productos
def post_new_client_kit(kit_body, auth_token):
    # Copiamos los encabezados base y añadimos el token de autorización dinámica
    current_headers = data.headers.copy()
    current_headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=current_headers
    )