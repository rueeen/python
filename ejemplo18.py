#funciones SIN retorno
resultado = print("Hola mundo")
print(resultado)
#Funciones CON retorno
resultado = input("Hola mundo")
print(resultado)

#Ejemplo funcion con retorno

def validarEdad(edad):
    if edad >= 18:
        print("Usted es mayor de edad")
        return True
    #elif edad >= 20:
    #    return
    # Esto retorna none si el valor es 20 o mas
    else:
        print("Usted es menor de edad")
        return False
        print("Esto no se ejecuta")
    
e = int(input("Ingrese su edad, si es mayor edad puede continuar..."))

resultado = validarEdad(e)

if resultado == True:
    print("Puede continuar con el formulario")
else:
    print("NO pu0ede continuar con el formulario")
    
def probandoRetorno():
    for i in range(100):
        if i == 50:
            return i
        
resultado = probandoRetorno()
print(resultado) #imprime 50