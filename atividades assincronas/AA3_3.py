import math
from AA3_1 import maclaurin_e
from AA3_2 import maclaurin_sen

"""
Usando biblioteca math.
O input deve ser um número x tal que 0 <= x < 1 usando '.' como separador decimal.
"""

def f(x):
    e, erro_e = maclaurin_e(x)
    sen, erro_sen = maclaurin_sen(x)
    erro = math.sqrt(e**2*erro_sen**2 + sen**2*erro_e**2)
    return (e*sen, erro)

def g(x):
    return math.sin(x)*math.exp(x)

x = eval(input('insira x (0<=x<1) = '))
print('erro absoluto máx. = ', f(x)[1], ', erro pela diferença = ', f(x)[0] - g(x))
