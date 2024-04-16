# parametros por defecto

print("hola mundo", end='\n', sep=' ')
print("hola mundo")

def suma(a=5, b=3):
    print(a+b)
    
suma() #8
suma(4) #7
suma(b=-3) #2
suma(3, 3) #6

#suma(c=5)#Error