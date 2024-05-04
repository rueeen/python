#Variables con python
#Se componen de nombre_variable = valor_variable
nombre = 'Perico'
apellido = 'Los Palotes'
edad = 36
#Recordando un poco de pseint
print('Su nombre es: ', nombre)
#Aqui se escribiran espacio de mas, esto debido al sep
print(nombre, " ", apellido, " ", edad)
# por defecto print tiene un argumento llamado 'sep'
# este argumento genera un espacio por defecto entre parametros
print(nombre, apellido, edad, sep='')

from ejemplo02 import funcion_importada

funcion_importada()