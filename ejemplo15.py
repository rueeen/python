# Argumentos posicionales
def resta(a, b):
    print(a - b)
    
resta(5, 3) #2
resta(3, 5) #-2

# Argumento por palabra clave 
resta(b=3, a=5) #2

def operaciones(a, b, c, d):
    print(a+c-b*d)
    
operaciones(1, 2, 3, 4) #-4
operaciones(d=1, b=2, c=3, a=4) #5
operaciones(1, 2, d=3, c=4) #-1
#operaciones(a=1, b=2, 3, 4) #Error debo utilizar siempre un argumento con palabra clave a la derecha de uno declarado
operaciones(1, b=2, d=3, c=4)

'''
print = 'hola'
print('Hola mundo')
input = 'chao'
input('hola')
'''


