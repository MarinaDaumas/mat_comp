import math

def fatorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return fatorial(n - 1) * n
        
def exp(x):
    print(x)
    result = 0
    for n in range(20): 
        result += x**n/fatorial(n)
    return result


def function(a, b):
    
    # sempre calcula a integral dividindo o intervalo em 100 partes
    n = 100

    h = (b - a)/n
 
    x = []
    fx = []
     
    i = 0
    while i<= n:
        x.append(a + i * h)
        if x[i] >= 0:
            fx.append(1/exp((x[i]*x[i])))
        else:
            fx.append(exp(-(x[i]*x[i])))
        i += 1
 

    res = 0
    i = 0
    while i<= n:
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res
     
