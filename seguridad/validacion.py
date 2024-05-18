
nombre = input('Ingrese un nombre\n').capitalize() # formateamos texto de entrada
apellido = input('Ingres su apellido\n').capitalize()

# Para quitar espacios en blanco 
# utilizando strip(), esto quita espacios vacios al inicio y fin de la palabra
# " hola mundo " -> "hola mundo"
nombre = nombre.strip() # quitar espacios al inicio y fin

# utilizando replace(), esto reemplaza caracteres por otro
# " hola mundo " -> "holamundo"
apellido = apellido.replace(" ", "") 

if nombre == '':
    print('Nombre vacio, intente nuevamente')
else:
    print(f'su nombre es {nombre}')
    
password = input('Ingrese un password con 8 caracteres y con mayusculas, minuscula y digitos\n')

#1234Abc
tieneNumeros = False
tieneMayusculas = False
tieneMinusculas = False
tiene8Caracteres = False

for i in password:
    if i.isdigit() == True:
        # tiene numeros
        tieneNumeros = True
    elif i.isupper() == True:
        # Es mayuscula
        tieneMayusculas = True
    elif i.islower() == True:
        # Es minuscula
        tieneMinusculas = True

if len(password) >= 8:
    #tiene 8 o mas caracteres
    tiene8Caracteres = True
    
if tieneNumeros and tieneMayusculas and tieneMinusculas and tiene8Caracteres:
    print("Password cumple condiciones")
else:
    print("Password no cumple condiciones")
    
try:
    numero = int(input('Ingrese un numero entero\n'))
except:
    print('El valor ingresado no es un numero')