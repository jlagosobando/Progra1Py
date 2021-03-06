#1 calcular aS

aA=[1,2,3,4,5]
aB=[3,7,1,-2,5]

#crea arreglo con la suma de aA (de izq a der) + aB (de der a izq)
#1+5,2+-2,3+1,4+7,5+3

aS=[aA[i]+aB[4-i] for i in range(5)]

print(aS)

#2 calcular nX

aD=[2,3,2,3,1,2,3,2,0,2]
nX=aD.count(aD[5])

#nX es el contador de cuando elementos a aD[5] (2) existen (5 veces)
print(nX)

#3 calcular aD

sTxt="ABCDEFG"
aD=[ord(sTxt[i]) for i in range(7)]

#toma cada letra de sTxt y saca su valor ascii con ord, ref. A=65 ...
print(aD)

#4 calcular aD

aA=[[2,3,4],[5,6,7],[1,-1,2]]
aD=[aA[1][i]+aA[2][1] for i in range(3)]

#aD se compone de la suma de los elementos de aA[1] (5,6,7) , y aA[2][1] (-1)
print(aD)

#5 para

aI=[0,1,2,1,2,1,2,0]
aT=[[1,2,4],[3,2,4],[-7,-8,-9]]

print("punto a")
#a que imprime el sgte script
for i in aI:
  print(aT[i][0:2])
#muestra cada elemento de aT con slide [0:2] usando los valores de aI como indice
  

print("punto b")
#b que imprime el sgte script
for i in aI:
  print(aT[i])
#muestra cada elemento de aT usando los valores de aI como indice

#6

def do_it(p,q):
  ns=0
  if len(p)==len(q): #funciona solo con arreglos de igual tamaño
    for i in range(len(p)):
      ns=ns+p[i]+q[i] #agrega al sumador los elementos de los arreglos, o sea, termina sumando todos los elementos de ambos arreglos
  return ns


dd={"@":[1,2,3],"$":[-1,-2,-3],"&":[4,5,6]} #cada clave del diccionario tiene su arreglo

#el arreglo av se forma con 3 ejecuciones de doit
av=[do_it(dd["@"],dd["$"]), do_it(dd["@"],dd["&"]), do_it(dd["$"],dd["&"])] #cada ejecución de doit recibe 2 arreglos mediante la clave
print(av)
#@+$=1+2+3-1-2-3=0
#@+&=1+2+3+4+5+6=21
#$+&=-1-2-3+4+5+6=9

#7 valor de aV

def do_it(p): #recibe un arreglo como parametro
  aa=[0,0,0,0,0,0]
  nl=len(p)-1
  for i in range(nl+1):
    aa[nl-i]=p[i] #ingresa en aa el arreglo p, de der a izq
  return aa

ab=["A",2,"@",3,4,"#"]
aV=[do_it(ab)]
print(aV)

#8 valor de ad

ad=[4,3,5,0,-1]
ai=[1,1,2,-1,1]
nc=0
lok=3>2 #al ser una comparación entrega valor booleano, en este caso True

#este while da 3 vueltas repitiendo lo que tiene dentro (el for)
while nc<3 and lok: #deben cumplirse ambas condiciones para que el while funcione, lok nunca cambia, nc si
  for i in range(5): #para cada vuelta del while este ciclo se realiza completo de nuevo
    ad[i]+=ai[i] #suma a ad el elemento correspondiente de ai (con el mismo indice)
  nc+=1
  
print(ad)

#primer while
#ad queda como [5,4,7,-1,0]
#segundo while
#ad queda como [6,5,9,-2,1]
#tercer while
#ad queda como [7,6,11,-3,2]

#9 valor de av

def do_it(q,p): #recibe 2 parametros, 1 arreglos q y un entero p
  if(p<= len(q)-1): #p son los valores del arreglo ap , len(q)-1=4
    return q[p] #cuando p es menor o igual a 4 muestra la coordenada q[p]
  else: #sino envía mensaje
    return "ops!" #o fuera de rango según error de impresión 
  
ad=[1,2,3,4,5]
ap=[0,1,6,3,7,4,5]

av=[do_it(ad,i) for i in ap]
print(av)

#dentro del arreglo av se ingresan:
#p=0 , p<=4, entonces muestra ad[0]=1
#p=1 , p<=4, entonces muestra ad[1]=2
#p=6 , p no <=4, entonces muestra mensaje
#p=3 , p<=4, entonces muestra ad[3]=4
#p=7 , p no <=4, entonces muestra mensaje
#p=4 , p<=4, entonces muestra ad[4]=5
#p=5 , p no <=4, entonces muestra mensaje
