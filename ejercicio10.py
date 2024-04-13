# Ejemplo while

# ciclo while funciona con una CONDICION

contador = 0

while contador > 10:
    print('NO se imprime')
    #Esto es el cuerpo del ciclo
print('Fuera del ciclo')

while contador < 10:
    print('Se ejecuta', contador)
    #Dentro del cuerpo debe existir algo que cambie la condicion a False
    contador += 1 # contador = contador + 1
    
respuesta = input('Desea continuar? Si/No\n').lower()

while respuesta == "si":
    print("Continuando...")
    respuesta = input('Desea continuar? Si/No\n').lower()

print("Fuera del ciclo")