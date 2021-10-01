def der_x(x,A,t):
    der = []
    for i in range(len(A)):
        dxi = 0.0
        for j in range(len(A)):
            dxi += x[j]*A[i][j]
        der.append(dxi)

    return der

def evolve(x0,A,h,t):
    tmax = t
    t = 0.0
    xs = range(len(x0))
    x = x0[:]
    x_list = []
    x_list.append(x0)
 
    while t<tmax:
        k1 = der_x(x,A,t)
        k2 = der_x([x[i] + (h/2.0)*k1[i] for i in xs],A, t + h/2.0)
        k3 = der_x([x[i] + (h/2.0)*k2[i] for i in xs],A, t + h/2.0)
        k4 = der_x([x[i] + h*k3[i] for i in xs],A, t + h)
        x = [x[i] + (h/6.0)*(k1[i] + 2.0*k2[i] + 2.0*k3[i] + k4[i]) for i in xs]
        x_list.append(x)
        t += h
 
    x_list =[[round(i,5) for i in x] for x in x_list]
    return x_list

evolve([1.0, 0.0], [[0.0, 1.0], [-1.0, 0.0]], 1.0, 7.0)