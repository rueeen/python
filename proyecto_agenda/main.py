'''
Proyecto Agenda
Requerimientos:
1. Agregar nuevos contactos. El sistema debe agregar nuevos contactos con su nombre, apellido y numero
2. Buscar un contacto y modificarlo. El sistema debe buscar un contacto en la lista por nombre y apellido, puede 
modificar su nombre, apellido o numero
3. Eliminar un contacto. El sistema debe buscar un contacto por nombre y apellido, si existe eliminarlo.
4. Listar todos los contactos. El sistema debe listar todos los contactos de la lista
0. Salir
'''
#Importamos siempre al inicio
import os #modulo para interactuar con sistema operativo

#Funcion con retorno
def buscarConctacto(nombre, apellido, lista):
    for c in lista:
        if c['nombre'] == nombre and c['apellido'] == apellido:
            return c
    return None

def buscarApellido(apellido, lista):
    nueva_lista = []
    for c in lista:
        if c['apellido'] == apellido:
            nueva_lista.append(c)
    return nueva_lista
    

#Nuestro contenedor sera una lista vacia
agenda = []
while True:
    #aca limpiamos menu
    os.system('cls')
    print('''
==== Menu de opciones ====
1. Agregar contacto
2. Modificar contacto
3. Eliminar contacto
4. Listar contactos
5. Listar por apellido
0. salir
            ''')

    op = input('Ingrese su opcion\n')
    #aca limpiamos menu
    os.system('cls')
    if op == '1':
        print('==== Agregar contacto ====')
        nombre = input('Ingrese el nombre\n').capitalize().strip() # peRicO => Perico
        apellido = input('Ingrese apellido\n').capitalize().strip() # __perico__ => Perico
        codigo_region = input('Ingrese codigo region\n')
        try:
            numero = int(input('Ingrese numero\n'))
            
            if nombre == '' and apellido == '':
                print('Nombre y apellido no pueden ser vacios')
            
            elif len(str(numero)) != 8:
                print('El numero debe tener 8 digitos')
                
            else:
                contacto = {'nombre':nombre, 'apellido': apellido, 'numero':codigo_region+' '+str(numero)}
                #Agregando contacto a agenda
                agenda.append(contacto)
                print('Contacto agregado')
        except:
            print('Error: Numero ingresado no corresponde')
        
    elif op == '2':
        print('==== Modificar contacto ====')
        nombre = input('Ingrese nombre para buscar\n').capitalize()
        apellido = input('Ingrese apellido a modificar\n').capitalize()
        
        respuesta = buscarConctacto(nombre, apellido, agenda)
        
        nuevo_numero = int(input('Ingrese nuevo numero\n'))
        
        respuesta['numero'] = nuevo_numero
        
    elif op == '3':
        print('==== Eliminar contacto ====')
        nombre = input('Ingrese nombre a eliminar\n').capitalize()
        apellido = input('Ingrese apellido a eliminar\n').capitalize()
        
        respuesta = buscarConctacto(nombre, apellido, agenda)
        
        if respuesta is not None:
            agenda.remove(respuesta)
            print('Se elimino contacto')
        else:
            print('No se encontro contacto')
    
    elif op == '4':
        print('==== Listar Contactos ====')
        if len(agenda) == 0:
            print('Aun no ha agregado contactos')
        else:
            for c in agenda:
                # c => {'nombre':nombre, 'apellido':apellido, 'numero':numero}
                print(f'Nombre: {c["nombre"]}')
                print(f'Apellido: {c["apellido"]}')
                print(f'Numero: {c["numero"]}')
                print('----------------------------------------')
    
    elif op == '5':
        print('==== Listar Contactos por Apellido====')
        apellido = input('Ingrese apellido a buscar\n').capitalize().strip()
        resultado = buscarApellido(apellido, agenda)
        if len(resultado) == 0:
            print('Aun no ha agregado contactos')
        else:
            for c in resultado:
                # c => {'nombre':nombre, 'apellido':apellido, 'numero':numero}
                print(f'Nombre: {c["nombre"]}')
                print(f'Apellido: {c["apellido"]}')
                print(f'Numero: {c["numero"]}')
                print('----------------------------------------')
                
    elif op == '0':
        print('Saliendo de sistema...')
        break
                
    input('Presione enter para continuar...')