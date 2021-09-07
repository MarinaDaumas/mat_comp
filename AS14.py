def Jacobi(A,B,N):
    
    size = len(A)

    X = []

    for i in range(size):
      X.append(B[i]/10)

    for j in range(N):
        X_temp = [i for i in X]
        for i in range(size):
            temp = 0.0
            for k in range(size):
                if A[k][k] == 0.0:
                    return []    
                temp += A[i][k]*X[k] 
            temp -= A[i][i]*X[i]                
            X_temp[i] = (B[i]-temp)/A[i][i]
        X = X_temp
        
    for i in range(size):
      X[i] = round(X[i],5)
    return X


Jacobi([[1.0, 0.1, 0.1], [0.1, 2.0, 0.1], [0.2, 0.1, 1.5]], [1.0, 2.0, 3.0], 20)