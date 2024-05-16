import os # utilizado para limpiar pantalla

curso = [] # creando lista vacia

# Funcion para buscar alumno
def buscar_alumno(nombre, apellido):
    for alumno in curso:
        if nombre == alumno['nombre'] and apellido == alumno['apellido']:
            return alumno
    return None

while True:
    os.system('cls')
    print('==== Menu de opciones ====')
    print('1. Agregar alumno')
    print('2. Modificar nota')
    print('3. Listar alumnos')
    print('4. Reportes')
    print('0. Salir')
    
    op = input('Ingrese su opcion\n')
    os.system('cls')
    if op == '1':
        print('==== Agregar alumno ====')
        nombre = input('Ingrese su nombre\n').capitalize()
        apellido = input('Ingrese su apellido\n').capitalize()
        try:
            nota = float(input('Ingrese nota alumno\n'))
            if nota >= 1 and nota <= 7:
                alumno = {'nombre':nombre, 'apellido':apellido, 'nota':nota}
                curso.append(alumno)
                print('Se agrego alumno a curso')
            else:
                print('La nota debe estar entre 1 y 7')
        except:
            print('La nota ingresada no es valida')
    elif op == '2':
        print('==== Modificar nota ====')
        nombre = input('Ingrese su nombre\n').capitalize()
        apellido = input('Ingrese su apellido\n').capitalize()
        
        alumno = buscar_alumno(nombre, apellido)
        
        if alumno is not None:
            try:
                nueva_nota = float(input('Ingrese nota alumno\n'))
                if nueva_nota >= 1 and nueva_nota <= 7:
                    alumno['nota'] = nueva_nota
                    print('Se modifico nota alumno')
                else:
                    print('La nota debe estar entre 1 y 7')
            except:
                print('La nota ingresada no es valida')
        else:
            print('No se encontro al alumno')
    
    elif op == '3':
        print('==== Listado alumnos ====')
        
        if len(curso) == 0:
            print('Curso sin alumnos')
        else:
            for alumno in curso:
                print(f'Nombre completo: {alumno["nombre"]} {alumno["apellido"]}')
                print(f'Nota: {alumno["nota"]}')
                print('-----------------------------------------------------')
                
    elif op == '4':
        print('==== Reportes ====')
        promedio = 0
        aprobados = 0
        reprobados = 0
        if len(curso) == 0:
            print('Curso sin alumnos')
        else:
            for alumno in curso:
                promedio += alumno['nota'] #sumando todas las notas del curso
                if alumno['nota'] < 4: # alumnos reprobados
                    reprobados += 1
                else:
                    aprobados += 1

            print(f'El promedio del curso es: {promedio/len(curso)}')
            print(f'La cantidad de aprobados es: {aprobados}')
            print(f'La cantidad de reprobados es: {reprobados}')
        
    elif op == '0':
        input('Saliendo de progra. Presione enter para continuar...')
        break
            
        
    input('Presione enter para continuar...')