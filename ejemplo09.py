#Instrucciones IF

edad = int(input('Ingrese su edad:\n'))

#la instruccion if va en minuscula
if edad >= 18:
    print("Usted es mayor de edad")
    print("Esto esta dentro del cuerpo del if")
print("Esto esta fuera del cuerpo del if y siempre se ejecuta")
#    print('esto da error')

#Mejorando con un els
if edad >= 18:
    print("Usted es mayor de edad")
#print()   
else:
    print("Usted es menor de edad")