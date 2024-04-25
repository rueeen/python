#Como se guardan las listas en memoria

a = [1, 2, 3, 4]
#insert agrega un elemento en el indice indiado
#       indice  valor
a.insert(1,     10)

print(a) #[1, 10, 2, 3, 4]
#Sera b una lista diferente a "a"?
b = a #SON LA MISMA LISTA
#b tiene el mismo contenido que "a"
print(b)
b.pop(3) #
print("b", b) #[1, 10, 2, 4]
print("a",a) #[1, 10, 2, 4]

#Para extraer contenido de una lista y crear listas nuevas utilizamos slicing
c = a[:] #Esto extrae toda la lista
print("c", c) #[1, 10, 2, 4]
c.pop() #Se elimina el ultimo elemento, 4
print("c", c) #c y a son LISTAS DISTINTA AHORA
print("a", a)

#La sintaxis a[:] indica copiar todo

d = b[2:400000000000000000] #slicing no da problemas por index error
print(d) #d es una lista nueva con 2 elementos [2, 4]

e = a[348273498732984:]
print(e) #[]

f = a[-1: 0]
print(f)
f = a[-1: 0:-1]
print(f)

palabra = 'Hola mundo'
print(palabra[5:2:-1]) #m a