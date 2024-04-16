#scope de python
#shadowing

nombre = "Perico"

def cambiarNombre():
    nombre = "Maria"
    print(nombre)#maria

cambiarNombre()

print(nombre) #perico

def una_funcion(a, b):
    print(a-b)
    
b = int(input('Ingrese un numero\n')) #3
a = int(input('Ingrese un numero\n')) #9

una_funcion(b, a) #-6
una_funcion(b=a, a=b) #-6