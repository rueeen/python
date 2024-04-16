#Funciones

#Las funciones serviran para reutilizar codigo

#Crecion de funcion
#salundado_desde_funcion() Error porque la funcion debe estar creada antes de ser invocada

def saludando_desde_funcion():
    print('Hola mundo desde funcion')
    
def salundado_con_nombre(nombre):
    print(f'Hola {nombre} desde funcion')
    
#Invocar funcion
saludando_desde_funcion()
    
#Invocando funcion con parametros
salundado_con_nombre('Perico') # debe haber 1 argumento

n = input('Ingrese su nombre\n')
salundado_con_nombre(n)

#salundado_con_nombre('Perico', n)Error porque envie 2 argumentos
#salundado_con_nombre()Error porque no envie argumentos
