import re

def sanitize_input(user_input):
    sanitized_input = re.sub(r'[^a-zA-Z0-9\s]', '', user_input)
    return sanitized_input


texto = input('Ingrese un texto con expresiones no regulares\n')

texto_sanitizado = sanitize_input(texto)

print(texto_sanitizado)