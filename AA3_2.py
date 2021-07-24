
"""
Função sen(x) aproximada por MacLaurin até a nona potência de x.
O input deve ser um número x tal que 0 <= x < 1 usando '.' como separador decimal.
"""

def fatorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return fatorial(n - 1) * n

def maclaurin_sen(x):
    result = 0
    for n in range(9): 
        result += (-1)**n/fatorial(2*n+1)*x**(2*n+1)
    return result, (-1)**(n+1)/fatorial(2*n+2)*x**(2*n+2)

if __name__ == "__main__":
    x = eval(input('insira x (0<=x<1) = '))
    result, erro_max = maclaurin_sen(x)
    print("resultado aproximado = ",result,", erro absoluto verdadeiro máx. = ", erro_max)