import os

#Creando funcion para buscar producto
def buscarProducto(nombre, lista):
    for p in lista:
        if p['nombre'] == nombre:
            return p #p es un diccionario con keys 'nombre' y 'precio'
    return None #Si no retornamos p, retornamos None

#creando listas vacias
tienda = []
ventas = []

while True:
    os.system('cls')
    print('==== Menu de opciones ====')
    print('1. Agregar producto')
    print('2. Modificar producto')
    print('3. Eliminar producto')
    print('4. Listar productos')
    print('5. Vender productos')
    print('6. Total ventas')
    print('0. Salir')
    
    op = input('Ingrese su opcion\n')
    os.system('cls')
    if op == '1':
        print('==== Agregar producto ====')
        nombre = input('Ingrese nombre producto\n').capitalize()
        precio = int(input('Ingrese precio producto\n'))
        #validar que nombre sea unico!
        r = buscarProducto(nombre, tienda)
        if r is None:
            #creamos diccionario producto
            producto = {'nombre':nombre, 'precio':precio}
            #agregar produco a lista
            tienda.append(producto)
            print('Producto agregado')
        else:
            print('Producto ya existe')
            
    elif op == '2':
        print('==== Modificar Producto ====')
        nombre = input('Ingrese nombre a modificar\n').capitalize()
        r = buscarProducto(nombre, tienda)
        if r is not None:
            #r es un diccionario con keys 'nombre' y 'precio'
            try:
                nuevo_precio = int(input('Ingrese nuevo precio\n'))
                r['precio'] = nuevo_precio
                print('Se ha modificado')
            except:
                print('Debe ingresar un valor numerico')
        else:
            print('Producto no encontrado')
            
    elif op == '3':
        print('==== Eliminar Producto ====')
        nombre = input('Ingrese nombre a modificar\n').capitalize()
        r = buscarProducto(nombre, tienda)
        if r is not None:
            tienda.remove(r)
            print('Se ha eliminado')
        else:
            print('Producto no encontrado')
        
    elif op == '4':
        print('==== Listar Productos ====')
        if len(tienda) == 0:
            print('No hay productos')
        else:
            for p in tienda:
                print(f'{p["nombre"]}............{p["precio"]}')
            
        
    elif op == '5':
        print('==== Vender Producto ====')
        nombre = input('Ingrese nombre producto a vender\n').capitalize()
        r = buscarProducto(nombre, tienda)
        
        if r is not None:
            #podemos vender
            ventas.append(r)
            print('Producto agregado a ventas')
        else:
            print('Producto no encontrado')
            
    elif op == '6':
        print('==== Total ventas ====')
        total = 0
        if len(ventas) == 0:
            print('No hay ventas aun')
        else:
            for p in ventas:
                print(f'{p["nombre"]}............{p["precio"]}')
                total += p['precio']
            print('___________________________')
            print(f'Total:{total}')
        
        
    input('Presione enter para continuar...')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
#Utilizando auxiliar boolean
encontrado = False
for p in tienda:
    if p['nombre'] == nombre:
        encontrado = True

if encontrado == False:
    v
else:
    print('Producto ya existe')
'''        
    