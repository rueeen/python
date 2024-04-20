
def cambiarLetras(palabra):
    nueva_palabra = ""
    for c in palabra:
        if c == 'u' or c == 'U':
            nueva_palabra += 'x'
        elif c == 'l':
            nueva_palabra += '7'
        elif c == 'b':
            nueva_palabra += '8'
        elif c == 's':
            nueva_palabra += '$'
        elif c == 'g':
            nueva_palabra += '6'
        else:
            nueva_palabra += c
    
    return nueva_palabra
        
p = input("Ingrese una palabra\n").lower()

resultado = cambiarLetras(p)
print(resultado)

#Como invierto una palabra con for? 5 decimas

#dato entrada -> HOLA
#dato salida  -> ALOH