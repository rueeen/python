# Ejemplo for

for i in "hola mundo":
    #cuerpo del for
    print(i, end = '\n')
    
palabra = 'abecedario'
#No imprimir caracter "a"
for caracter in palabra:
    if caracter != 'a':
        print(caracter)
        
#range() tiene 3 sobrecargas
#range(5) -> 0, 1, 2, 3, 4

for numero in range(5):
    print(numero)
    
#range(2, 5)  -> 2, 3, 4
# primer numero es el inicio
# segundo numero es el fin - 1

for numero in range(2, 5):
    print(numero)
    
#range(2, 5, 2) -> 2, 4
# primero es el inicio
# segundo el fin - 1 
# tercero incremento
print()
for numero in range(2, 5, 2):
    print(numero)
    
# si quiero ir al reves con range

# range (5, 2) -> 
# range (5, 2, -1) -> 5, 4, 3
print("Aca comienza el for al reves")
for numero in range(10, 0, -1):
    print(numero)