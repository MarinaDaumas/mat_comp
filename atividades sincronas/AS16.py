"""
A function INT_S(y,h) should return the integral of y(x), sampled evenly with a step h into the list y, 
which is always 3 or more samples long. Use Simpson's 1/3 rule, unless there's an even number of samples, 
in which case the integral of the last interval should be calculated by the trapezoidal rule. 
Return the value with 5 decimals.
"""
def INT_S(y,h):
  A = 0

  # 1/3 de Simpson.
  A = h/3*(y[0] + y[-1] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-1:2]))
    
    
  if len(y) % 2 == 0:
    
    # 1/3 de Simpson.
    A = h/3*(y[0] + y[-2] + 4*sum(y[1:-2:2]) + 2*sum(y[2:-2:2]))
    # Método dos trapézios
    A += h/2*(y[-1]+y[-2])

  return round(A, 5)


  
