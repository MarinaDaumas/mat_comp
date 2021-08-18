"""
Programa para calcular os valores de 'a' e 'b' pelo método de descida de gradiente simples em y(x) = a*exp(b*x)   
"""

def fatorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return fatorial(n - 1) * n


def exp(x):
    result = 0
    for n in range(9): 
        result += x**n/fatorial(n)
    return result


def Model(L, p, max_iter):
    
    a = 1
    b =  -1

    erro_acp = []
    iter = 0

    while iter < max_iter: 
        erro = 0 
        gradient_a = 0
        gradient_b = 0

        for coordinate in L:
            x = coordinate[0]
            y = coordinate[1]
            y_calculated = a/exp(-b*x)

            w += (y_calculated - y)**2

            der_a = 2*( y_calculated - y)/exp(-x*b)
            der_b = 2*(y_calculated - y)*a*x/exp(-x*b)

            gradient_a += der_a
            gradient_b += der_b

        a -= gradient_a*p
        b -= gradient_b*p

        print('var ', a, b)
        print('erro ', erro)
        print('')
        iter += 1

        erro_acp.append(w)
    print(erro_acp)


L1 = [[0.0, 1.3], [1.0, 0.5841], [2.0, 0.2625], [3.0, 0.1179], [4.0, 0.053], [5.0, 0.0238], [6.0, 0.0107], [7.0, 0.0048], [8.0, 0.0022], [9.0, 0.001], [10.0, 0.0004]]

L2 = [[1.0, 0.3162], [2.0, 0.1053], [3.0, 0.035], [4.0, 0.0117], [5.0, 0.0039], [6.0, 0.0013], [7.0, 0.0004], [8.0, 0.0001], [9.0, 0.0]]

L3 = [[1.0, 0.3115], [2.0, 0.1077], [3.0, 0.0498], [4.0, 0.017], [5.0, 0.0179], [6.0, 0.0035], [7.0, 0.0068], [8.0, 0.0095], [9.0, 0.0078]]


Model(L1, 0.1, 1000)