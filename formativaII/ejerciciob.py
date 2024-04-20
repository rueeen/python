# dato entrada -> 5
# dato salida  -> 55555
#                 4444
#                 333
#                 22
#                 1


numero = int(input('Ingrese un numero\n'))

if numero > 0:
    for i in range(numero, 0, -1):
        print(i*str(i))
else:
    print("Numero no valido")
  
print("Se termino ciclo")  
    
for j in range(5, 0, -1):
    for o in range(j):
        print(j, end="")
    print()

print("Se termino ciclo")