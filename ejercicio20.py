#CRUD listas
#CRUD => Create Read Update Delete

#Lista creada fuera para que no se reinicie en cada ciclo
lst = ['perico', 'maria', 'pedro']
#indces   0         1        2

#Crearemos un menu de acciones
while True:
    print("1. Agregar")
    print("2. Leer")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Mostrar lista completa")
    print("0. Salir")

    opcion = input('Ingrese su opcion\n')
    
    if opcion == '1':
        #Agregando elementos a mi lista
        #La lista contendra nombres de personas
        nombre = input('Ingrese un nuevo nombre para agregar a lista\n')
        #para agregar utilizamos metodo .append
        #primero llamamos a nuestra lista
        #luego agregamos un .
        lst.append(nombre)
        print('Se agrego un nuevo nombre a la lista')
        
    elif opcion == '2':
        print(lst)
        indice = int(input('Ingrese indice de elemento a mostrar\n'))
        #Podemos imprimir el dato especifico de la lista con su INDICE
        #Los indices van desde 0 hata 1 menos el tamaño de la lista
        print(lst[indice])
    elif opcion == '3':
        #Modificando elemento de lista
        print(lst)
        #Para modificar necesito 2 cosas
        #1. el indice del elemento a modificar
        #2. El nuevo valor
        indice = int(input("Ingrese indice de elemento a modificar\n"))
        valor = input("Ingrese nuevo valor\n")
        #Esto cambia el valor del indice indicado
        lst[indice] = valor
        print(lst)
    elif opcion == '4':
        #Eliminar elemento de una lista
        #Se necesita el indice
        indice = int(input('Ingrese indice de elemento a eliminar\n'))
        #Eliminamos
        del lst[indice]
        #del lst esto elimina toda la lista
        
    elif opcion == '5':
        #Recorrer y mostrar TODA la lista
        
        #forma 1 por indice
        # range ( 3 ) => 0, 1, 2
        for i in range(len(lst)):
            print(f"i es el indice y vale {i} y su valor es {lst[i]}")
            print("----------------------------------------------------")
        
        #forma 2 por valor
        for v in lst:
            print(f'Aca solo podemos imprimir el valor, en este caso {v}')
            print('-------------------------------------------------------')
        
    elif opcion == '0':
        print('Saliendo de programa')
        break
    else:
        print("Opcion ingresada no valida")