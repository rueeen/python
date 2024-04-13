'''
Para recibir datos de entrada utilizamos la funcion
input(), esta funcion retorna por lo que SIEMPRE se acompaña de
una variable
'''
print('Ingrese un nombre de persona')
input() #aca no guardo lo que recibo desde consola
nombre = input() #aca guardo en la variable nombre lo que recibo desde consola

print('Su nombre es', nombre)

# input() tiene otra forma
saludo = input('Ingrese un saludo: ')
print(saludo)

saludo = input('Ingrese un saludo:\n')
print(saludo)