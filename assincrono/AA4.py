import math
""""
Programa para calcular o valor de ln(x) pelo método da bissecção.
"""                                                     
def fatorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return fatorial(n - 1) * n


def maclaurin_e(x):
    result = 0
    for n in range(9): 
        result += x**n/fatorial(n)
    return result, abs(math.exp(x)-result)


def ln_bis(x):
    max_iterations = 50
    inf = 0.0 # limites inferior e superior
    sup = 0.7
    mid = (inf + sup)/2

    i = 0
    while i < max_iterations and abs(sup-inf) >= 1.0e-8:
        i += 1
        last_mid = mid
        mid = (inf + sup)/2
        f_inf =  maclaurin_e(inf)[0] - x
        f_sup =  maclaurin_e(sup)[0] - x
        f_mid = maclaurin_e(mid)[0] - x

        if f_inf*f_mid < 0:
            sup = mid

        elif f_sup*f_mid < 0:
            inf = mid

        raiz = mid

    return round(raiz, 8)


def ln_nr(x):
    max_iterations = 50 
    x_i = 0.7
    

    erro = 100
    i = 0
    while i < max_iterations and  abs(erro) > 1.0e-8:
        i += 1
        exp = maclaurin_e(x_i)[0] 
        x_il = x_i - (exp - x - 0)/exp
        erro = abs((x_il - x_i)/x_il*100) 
        x_i = x_il       

    return round(x_i, 8)


x = eval(input('x: '))
y_bis = ln_bis(x) 
y_nr = ln_nr(x)

print('\nPor bissecção:\ny = ', y_bis,'\n\nPor Newton Raphson:\ny = ', y_nr)