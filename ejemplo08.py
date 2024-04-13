'''
Muestre el nombre y la edad en 10 años mas de una persona
'''

nombre = input('Ingrese su nombre\n')
edad = int(input('Ingrese su edad\n'))

nueva_edad = edad + 10

print('Hola', nombre, 'su edad en 10 años mas sera', nueva_edad)
#Esto da error porque no puedo sumar int con str
print('Hola '+ nombre + ' su edad en 10 años mas sera '+ nueva_edad)

print('Cualquier cosa')