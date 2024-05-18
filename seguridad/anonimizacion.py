def anonymize_data(data):
    # Sustituir cada carácter por 'X' para anonimizar los datos
    anonymized_data = 'X' * (len(data)-3)+str(data[-1:-4:-1])
    return anonymized_data

numero_tarjeta_credito = input('Ingrese numero tarjeta de credito\n')

anonimizacion = anonymize_data(numero_tarjeta_credito)

print(anonimizacion)