#Ejercicios iniciales de funciones

#suma 2 numeros
def suma2(x,y):
    return x+y

#uso suma2
s=suma2(4,5) #9
print(s)

#uso suma2 con valores por teclado
a=int(input("primer valor "))
b=int(input("segundo valor "))
print(suma2(a,b))

#uso de suma2 como parametro
s=suma2(suma2(1,2),suma2(3,4)) #10
print(s)
