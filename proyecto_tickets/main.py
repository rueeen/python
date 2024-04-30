'''
TICKETS
'''

#Creacion de listas
tickets_abiertos = [] #LISTA VACIA 
tickets_cerrados = [] #LISTA VACIA

while True:
    print('==== Menu de opciones ====')
    print('1. Crear ticket')
    print('2. Cerrar ticket')
    print('3. Listar tickets cerrados')
    print('4. Listar tickets abiertos')
    print('5. Eliminar cerrados')
    print('0. salir')
    
    opcion = input('Ingrese su opcion\n')
    
    if opcion == '1':
        print('==== Crear ticket ====')
        codigo = input('Ingrese codigo de ticket\n').upper()
        #len() funcion que devuelve tamanio de algo
        #len("hola") -> 4
        #len([1,2,3,4,5]) -> 5
        if len(codigo) > 4:
            print('Error, codigo no debe superar los 4 caracteres')
        else:
            nombre = input('Ingrese nombre de ticket\n')
            #Creamos ticket dentro de else para seguir la secuencia logica de acciones
            ticket = {'codigo':codigo, 'nombre':nombre}
            tickets_abiertos.append(ticket)
            print('Se creo ticket con exito')
            
    elif opcion == '4':
        print('==== Tickets abiertos ====')
        if len(tickets_abiertos) == 0:
            print('No hay tickets abiertos')
        else:
            for t in tickets_abiertos:
                print(f'Codigo: {t["codigo"]}') 
                print(f'Nombre: {t["nombre"]}') 
                print('---------------------------------')
                
    elif opcion == '3':
        print('==== Tickets cerrados ====')
        if len(tickets_cerrados) == 0:
            print('No hay tickets cerrados')
        else:
            for t in tickets_cerrados:
                print(f'Codigo: {t["codigo"]}') 
                print(f'Nombre: {t["nombre"]}') 
                print(f'Comentario: {t["comentario"]}') 
                print('---------------------------------')
                
    elif opcion == '2':
        print('==== Cerrar ticket ====')
        codigo = input('Ingrese codigo ticket\n').upper()
        
        for t in tickets_abiertos:
            if codigo == t['codigo']:
                #Encontramos tickets
                comentario = input('Ingrese un comentario\n')
                t['comentario'] = comentario
                tickets_cerrados.append(t)
                tickets_abiertos.remove(t)
                print(f'Se ha cerrado ticket {t["nombre"]}')
                
    elif opcion == '5':
        print('==== Borrar cerrados ====')
        respuesta = input('Esta seguro que desea eliminar la lista cerrados?\n').lower()
        
        if respuesta == 'si':
            tickets_cerrados.clear()
            print('Lista vaciada')
        else:
            print('Se mantiene lista')
                
        
        