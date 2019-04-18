from math import *

cache = {0: 0, 1: 1}
def fib(n):
    #http://edupython.blogspot.com/2013/07/los-numeros-de-fibonacci.html
    #se usa memoria para hacerlo mas eficiente
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

assert fib(2)==1
assert fib(6)==8

def baseFib(n):
    nroInicial=n
    m = n*[0]  # vector que se entregara. Ponemos el cero para que dps no haya problema con el indicice [i+1]
    n_sol=0
    if(nroInicial!=n_sol): #cuando aun no es solucion
        for i in range(n+1,0,-1):
            if n>=fib(i):
                if m[i]!=1:
                    m.append(1)
                    n_sol += fib(i)
                    print(n_sol)
                    n -= fib(i)

            else:
                m.append(0)


    for i in range(len(m)): #saco todos los ceros que estan a la izquierda
        if m[0]==0:
            m.pop(0)

    print(m)
    return m



assert baseFib(5) == [1,0,0,0,0]
assert baseFib(65) == [1,0,0,0,1,0,0,0,1]