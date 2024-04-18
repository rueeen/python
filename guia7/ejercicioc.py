'''
c.	Cree una función en python que reciba un número, escriba si el número es par o impar
'''

def par_impar(num):
    if num % 2 == 0 :
        print('Par')
    else:
        print('Impar')
        
n = int(input('Ingrese un numero'))

par_impar(n)