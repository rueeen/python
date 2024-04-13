# Ejemplo break

# break es una instruccion para ciclos
contador = 0
while True:
    print('Esto es infinito')
    contador += 1
    if contador == 5:
        print(contador)
        break
        print("Esto no se ejecuta")
    print('Esto si')
print('Fuera del ciclo')