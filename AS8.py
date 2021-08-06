'''
f_y= y*y - x = 0
'''
def SQRT_NR(x):
  
    max_iterations = 50 
    x_i = 1.5
    x_il = 0

    erro = 100
    i = 0
    while i < max_iterations and  erro > 1.0e-4:
        i += 1
        x_il = x_i - (x_i*x_i - x)/(2*x_i)
        erro = abs(x_il - x_i)
        x_i = x_il       

    return [round(x_i, 12), i]
