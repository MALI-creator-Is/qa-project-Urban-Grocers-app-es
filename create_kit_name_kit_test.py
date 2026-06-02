import sender_stand_request
import data


# Función auxiliar para obtener el authToken de un usuario nuevo
def get_new_user_token():
    user_body = data.user_body.copy()
    response = sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]


# FUNCIÓN DE ASERCIÓN POSITIVA (Espera un código 201)
def positive_assert(kit_name):
    auth_token = get_new_user_token()
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name

    response = sender_stand_request.post_new_client_kit(current_kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_name


# FUNCIÓN DE ASERCIÓN NEGATIVA (Espera un código 400 por error de validación)
def negative_assert_code_400(kit_name):
    auth_token = get_new_user_token()
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name

    response = sender_stand_request.post_new_client_kit(current_kit_body, auth_token)

    assert response.status_code == 400


# -------------------------------------------------------------------------
# CASOS DE PRUEBA (CHECKLIST)
# -------------------------------------------------------------------------

# Caso 1: El número mínimo de caracteres permitido (1 carácter)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Caso 2: El número máximo de caracteres permitido (511 caracteres)
def test_create_kit_511_letter_in_name_get_success_response():
    string_511 = "A" * 511
    positive_assert(string_511)


# Caso 3: Cantidad menor que el límite inferior (0 caracteres / vacío)
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400("")


# Caso 4: Cantidad mayor que el límite superior (512 caracteres)
def test_create_kit_512_letter_in_name_get_error_response():
    string_512 = "A" * 512
    negative_assert_code_400(string_512)


# Caso 5: Se permiten caracteres especiales
def test_create_kit_special_character_in_name_get_success_response():
    positive_assert('"№%@",')


# Caso 6: Se permiten espacios
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert("A A A")


# Caso 7: Se permiten números
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")


# Caso 8: Error si falta el parámetro 'name' en la solicitud
def test_create_kit_no_name_in_body_get_error_response():
    auth_token = get_new_user_token()
    # Enviamos un cuerpo completamente vacío sin la clave "name"
    response = sender_stand_request.post_new_client_kit({}, auth_token)
    assert response.status_code == 400


# Caso 9: Error si se pasa un tipo de datos diferente (ej. un número en vez de string)
def test_create_kit_int_type_name_get_error_response():
    negative_assert_code_400(123)