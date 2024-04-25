#Ordenando lista

import random

lst = []

for i in range(30):
    lst.append(random.randrange(100))
    
print(lst)

#Ordena una lista de forma ascendente
lst.sort()
print(lst)

nombres = ["Perico", "Maria", "Pedro", "Alberto", "Goku"]
nombres.sort()
print(nombres)

lista_mixta = [1, 3, 5, 0, "Nombres", "asdasd"]
lista_mixta.sort() #Error
print(lista_mixta)