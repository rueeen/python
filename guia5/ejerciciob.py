n = float(input('Ingrese un numero\n'))
m = float(input('Ingrese otro numero\n'))

if n > m:
    print(f'EL mayor es: {n}')
elif m > n:
    print(f'El mayor es: {m}')
else:
    print('Son iguales')