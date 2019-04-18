from math import *

def digitos(n):
    # http://python-tec.blogspot.com/2010/07/funcion-contar-digitos.html
    ind = 1
    while n > 9:
        n = int(n / 10)
        ind += 1
    return ind

#dado un entero, retorna la forma factorial del numero (una lista m)
def  baseFact(n):
    nroInicial=n
    m = []  # vector que se entregara
    dig=digitos(n)
    k=dig+3 #en un comienzo k y x son iguales
    n_sol=0
    if(nroInicial!=n_sol): #cuando aun no es solucion
         for i in range(k,0,-1):
             if n>=factorial(i): #factorial mas grande menos que n
                 for j in range(i,0,-1): #j<=i
                     if n>=(j)*factorial(i):
                         m.append(j) #numero que acompaña al factorial
                         n_sol += (j) * factorial(i)
                         n = n - j*factorial(i)

             else: #agrega 0 cuando el factorial no se multiplica por nada
                 m.append(0)


    for i in range(len(m)): #saco todos los ceros que estan a la izquierda
        if m[0]==0:
            m.pop(0)

    m.append(0)
    return m

assert baseFact(1)==[1,0]
assert  baseFact(3)==[1,1,0]
assert baseFact(463)==[3,4,1,0,1,0]

#print('#'.join(map(str, baseFact(int(input())))))

##Programa interactivo
#print("Bienvenidx al juego de retornar tu numero en forma factorial")
n=int(input())
nro=baseFact(n)
l=len(nro)
for i in range(l-1):
    print(str(nro[i])+"#", end="")
print(str(nro[l-1]))
