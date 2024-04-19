
def cambiarLetras(palabra):
    nueva_palabra = ""
    for c in palabra:
        if c == 'u' or c == 'U':
            nueva_palabra += 'x'
        else:
            nueva_palabra += c
    
    return 
        
p = input("Ingrese una palabra\n")

cambiarLetras(p)

#Como invierto una palabra con for? 5 decimas

#dato entrada -> HOLA
#dato salida  -> ALOH