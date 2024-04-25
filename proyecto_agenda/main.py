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
#Funcion con retorno
def buscarConctacto(nombre, apellido, lista):
    for c in lista:
        if c['nombre'] == nombre and c['apellido'] == apellido:
            return c
    return None

#Nuestro contenedor sera una lista vacia
agenda = []
while True:
    print('''
    ==== Menu de opciones ====
    1. Agregar contacto
    2. Modificar contacto
    3. Eliminar contacto
    4. Listar contactos
    0. salir
            ''')

    op = input('Ingrese su opcion\n')
    
    if op == '1':
        print('==== Agregar contacto ====')
        nombre = input('Ingrese el nombre\n').capitalize() # peRicO => Perico
        apellido = input('Ingrese apellido\n').capitalize()
        numero = int(input('Ingrese numero\n'))
        contacto = {'nombre':nombre, 'apellido': apellido, 'numero':numero}
        #Agregando contacto a agenda
        agenda.append(contacto)
        print('Contacto agregado')
        
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