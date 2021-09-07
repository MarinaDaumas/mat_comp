# Interpolation by Direct method


def compatibility(a):
    for i in range(len(a)):
        print(a[i][i], '88', a[i])
        if 2*a[i][i] < sum(a[i]):
            return False
        
    return True


def matrix_multiplication(m1, m2, size_a, size_b):

    result = []
    for i in range(size_a):
        for j in range(size_b):
            partial_res = 0
            for k in range(size_a):
                partial_res += m1[i][k]*m2[k]
            
        result.append(partial_res)

    return result


def gauss_seidel(a, b, iter):
    
    size = len(a)

    if not compatibility(a):
        print('Não foi possível realizar a operação.')
        return('Não foi possível realizar a operação.')

    X = []
    #X = [1, 2, 5]

    for i in range(size):
        X.append(0)

    
    for j in range(iter):
        for i in range(size):
            temp = 0   
            for k in range(size):
                temp += a[i][k]*X[k] 
            temp -= a[i][i]*X[i]                
            X[i] = (b[i]-temp)/a[i][i]

    return X

def matrix_mult(list_x, list_y):

    list_x = [1,2,3]
    list_y = [6,17,34]
    for i in range(len(list_x)):
        x_temp = []
        for j in range(len(list_x)):
            x_temp.append(list_x[i]**j)
        
        list_x[i] = x_temp

    print(list_x)

    list_a = gauss_seidel(list_x, list_y,10)
    print(list_a)
    return list_a


def calculated_y(list_a, x):
    result_y = []
    for i in range(len(x)):
        res_y = 0
        for j in range(len(list_a)):    
            res_y += a[j]*x[i]**j
        result_y.append(res_y)   
    return result_y


def erro(y, result_y):
    erro_y = sum(abs(result_y - y))/len(y) 
    return erro_y 


def fucntion(list_xy):
    
    x = []
    y = []  
    for i in list_xy:
        x.append(i[0])
        y.append(i[1])


    erro = 10
    for i in range(len(x)):



        list_a = matrix_mult(x[:1], y[:i])

        result_y = calculated_y(list_a, x)
        
        erro = erro(y, result_y)
        if erro < 1:
            break


    return list_a




matrix_mult([6, 5, 10], [])
        


