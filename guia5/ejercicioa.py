peso = float(input('Ingrese su peso\n'))
altura = float(input('Ingrese su altura\n'))

imc = peso / (altura * altura) # altura ** 2

#comprobar estado imc
if imc <= 15:
    print('Delgadez muy severa.')
elif imc > 15 and imc <= 15.9:
    print('Delgadez severa.')
elif imc <= 18.4:
    print('Delgadez')
elif imc <= 24.9:
    print('Peso saludable')
elif imc <= 29.9:
    print('Sobrepeso')
else:
    print('Obesidad moderada')