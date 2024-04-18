'''
a.	Cree una función en python que reciba 2 números, imprima un mensaje con el mayor de ellos.
'''
#creando funcion
def mostrarMayorOIgual(n, m):
    if n > m:
        print(f'El mayor es {n}')
    elif n < m:
        print(f'El mayor es {m}')
    else:
        print('Son iguales')
        
n1 = float(input('Ingrese un numero\n'))
n2 = float(input('Ingrese otro numero\n'))

#Invocacion
mostrarMayorOIgual(n1, n2)