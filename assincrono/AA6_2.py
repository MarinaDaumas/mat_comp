# método gauss-seidel.
# Feito em Grupo com Júlia Xexéo e Ney Guindane.
 
def compatibility(a):
    for i in range(len(a)):
        if 2*a[i][i] < sum(a[i]):
            return False
        
    return True


def matrix_size(original_matrix):
    size = int(len(original_matrix)**(1/2))
    
    matrix = []
    k = 0
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(original_matrix[k])
            k+=1
        matrix.append(temp)

    return size, matrix


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
    
    size, a = matrix_size(a)

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

