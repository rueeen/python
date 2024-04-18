'''
b.	Cree una función en python que reciba una palabra, cuente cuantas 
vocales (a, e, i, o, u) hay dentro de la palabra.
'''

def contarVocales(palabra):
    vocales = 0
    for caracter in palabra:
        if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
            vocales += 1
    print(f'Hay {vocales} vocales(a, e, i, o, u) dentro de {palabra}')
    
dato = input("Ingrese una palabar\n").lower()

contarVocales(dato)