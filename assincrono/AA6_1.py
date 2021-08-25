
#função principal é LU_decomposition

def id_matrix(size):

    m = []
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(0)
        m.append(temp)
        m[i][i] = 1

    return m


def zero_matrix(size):

    m = []
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(0)
        m.append(temp)
    return m


def reorder_rows(u, l, p, column):

    for i in range(column, len(u)):
        for j in range(i+1, len(u)):
            if u[i][column] < u[j][column]:
                temp = u[i] 
                u[i] = u[j]
                u[j] = temp
                temp = l[i] 
                l[i] = l[j]
                l[j] = temp
                temp = p[i] 
                p[i] = p[j]
                p[j] = temp
      
    return u, l, p


def transpose_matrix(original):
    m = original
    for i in range(size):
        for j in range(size):
            m[j][i] = original[i][j]
    return m 


def matrix_multiplication(m1, m2, size):
    """
    Multiplicação de matrizes quadradas de mesmas dimeções
    """
    result = []
    for i in range(size):
        temp =[]
        for j in range(size):
            partial_res = 0
            for k in range(size):
                partial_res += m1[i][k]*m2[k][j]
            temp.append(partial_res)
        result.append(temp)

    return result


def matrix_size(original_matrix):
    """
    retorna o comprimento da matriz quadrada e a matriz como lista de listas
    """
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


def update_row(row, added_row, mult):

    for i in range(len(row)):
        row[i] += mult*added_row[i]
        row[i] = round(row[i], 1)

    return row


def back_to_list(m, size):
    m_as_list = []
    for i in range(size):
        for j in range(size):
            m_as_list.append(m[i][j])

    return m_as_list


def LU_decomposition(a):
    """
    recebe a matrix a em forma de lista e retorna as matrizes p, l e u
    """
    original_matrix = a
    size, a = matrix_size(original_matrix)

    u = a
    l = zero_matrix(size)
    p = id_matrix(size)

    for i in range(size):
        # i é a linha acima da que está sendo usada para zerar as de baixo
        u, l, p = reorder_rows(u, l, p, i)
        l[i][i] = 1
        if i != 0:
            print('UUUU',u)
            for j in range(i, size):
                
                if u[i-1][i-1] != 0:
                
                    x = -u[j][i-1]/u[i-1][i-1]
                    l[j][i-1] = x
        
                    u[j] = update_row(u[j], u[i-1], x) 
    
    p = back_to_list(p)
    l = back_to_list(l)
    u = back_to_list(u)

    return (p, l, u)