#Diccionarios

#Definiendo un diccionario key = k , value = v
#              (k    v) (k  v)   (k     v)
diccionario = {'uno':1, 0:  2,  True:"False"}
#puedo utilizar como k cualquier tipo de dato
print(diccionario)

dic = {'Nombre': 'Perico', 'Apellido':'Los palotes', 'Apellido':'Malaya'}
print(dic) #Apellido sale una vez porque se considera como llave UNICA

#Imprimiendo elementos de diccionario
print(dic['Apellido'])

#Modificando diccionario
dic['Nombre'] = 'Maria'
print(dic)
#Agregando elemento a diccionario
dic['Direccion'] = 'Nueva direccion'
print(dic)