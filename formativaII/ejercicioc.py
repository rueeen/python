def contarCaracteres(p):
    contar = 0
    for c in p:
        if c != " ":
            contar += 1
    return contar

palabra1 = input('Ingrese una palabra\n')
palabra2 = input('Ingrese otra palabra\n')

if contarCaracteres(palabra1) > contarCaracteres(palabra2):
    print('Palabra 1 es mayor')
elif contarCaracteres(palabra2) > contarCaracteres(palabra1):
    print("Palabra 2 es mayor")
else:
    print("Son iguales")