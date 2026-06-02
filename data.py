# Encabezados obligatorios para que el servidor entienda que mandamos JSON
headers = {
    "Content-Type": "application/json"
}

# Datos base para registrar un usuario nuevo y poder extraer su authToken
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elms St"
}

# Datos base para la creación de los kits (aquí probaremos las variantes del nombre)
kit_body = {
    "name": "Mi kit de prueba"
}