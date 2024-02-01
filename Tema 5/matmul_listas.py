#Multiplicación de matrices. 
import numpy as np
import time


def matmul_listas(A, B):
    C = []
    filas = len(A)
    columnas = len(B[0])
    bucle = len(B)

    if bucle != len(A[0]):
        print('Dimensiones incorrectas')
    else:
        for i in range(filas):
            C.append([])
            for j in range(columnas):
                C[i].append(0)
                for k in range(bucle):
                    C[i][j] += A[i][k]*B[k][j]
    return C


def matmul(A, B):
    filas_A, columnas_A = np.shape(A)
    filas_B, columnas_B = np.shape(B)

    if columnas_A != filas_B:
        print('Dimensiones incorrectas')
    else:
        C = np.zeros((filas_A, columnas_B))
        for i in range(filas_A):
            for j in range(columnas_B):
                for k in range(columnas_A):
                    C[i, j] += A[i, k]*B[k, j]
    return C


"""
n = 10
A = [[i+j for i in range(n)] for j in range(n)]
B = [[i-j for i in range(n)] for j in range(n)]

t1 = time.time()
C = matmul_listas(A, B)
t2 = time.time()
print('Tiempo multiplicar listas:', t2-t1)

mA = np.array(A)
mB = np.array(B)

t1 = time.time()
mC = np.matmul(mA, mB)
t2 = time.time()
print('Tiempo multiplicar matrices:', t2-t1)
"""
A = [[1, 2, 3], [1, 0, -1]]
B = [[1, 1], [0, 2], [-1, 3]]

C = matmul_listas(A, B)
print(C)

mA = np.array(A)
mB = np.array(B)

mC = matmul(mA, mB)
print(mC)
