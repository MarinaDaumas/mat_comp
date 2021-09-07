# Python 3 para py3.codeskulptor.org
# Prof. Frederico C. Jandre -- Programa de Engenharia Biomédica
# Para COC351 2021.1

import math as m

def f(x):
    return m.sin(x);


x0 = 0;0;
x1 = m.pi/2;

dsret = []
dstrap = []
dssimp = []
for N in range(5,12,2):
  # Definição dos pontos amostrados da função
  x = [x0+i*(x1-x0)/N for i in range(0,N+1)];
  # Cômputo da função nos pontos
  y = [f(i) for i in x];
  # Cômputo do efetivo intervalo (passo) de amostragem
  h = (x1-x0)/N;

  # As linhas abaixo devem computar as integrais de f(x) entre 0 e pi/2.
  # Exercício: corrija o que estiver errado, apresente as linhas corrigidas e
  # comente os resultados.
 
  # Método dos retângulos
  Aret = h*(sum(y[:-2]));
  # Método dos trapézios
  Atrap = h/2*(y[0] + sum(y[1:-2]) + y[-1]);
  # 1/3 de Simpson.
  Asimp = h/3*(y[0] + y[-1] + sum(y[1:-2:2]) + sum(y[2:-2:2]) )
  dsret.append((N,Aret))
  dstrap.append((N,Atrap))
  dssimp.append((N,Asimp))

print(dsret)
print(dstrap)
print(dssimp)
