# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:15:40 2022

@author: javie
"""
import numpy as np

"""
Ejercicio propuesto 3:

1.- Crea un vector de tamaño 𝑛 cuyos elementos sean 𝑣(𝑖)=(−1)^𝑖/(2𝑖−1)
2.- Crea una matriz cuadrada 𝑛×n cuyos elementos sean 𝐴(𝑖,𝑗)=(𝑖/n)^(𝑗−1)

3.- Crea una función suma_dimensiones(𝐴,𝑝) que reciba como argumento una matriz 𝐴  y un entero p.
     Si p = 0 devolverá un vector del tamaño el número de columnas que tenga 𝐴 y 
     cuyos elementos serán la suma de la columna correspondiente de A.
     Si p = 1 devolverá un vector del tamaño el número de filas que tenga 𝐴 y 
     cuyos elementos serán la suma de la fila correspondiente de A

4.- Crea una función producto(𝐴,𝑣,𝑝) que reciba como argumento una matriz 𝐴, un vector 𝑣 y un entero p.
     Si p = 0 devolverá el vector producto 𝐴v.
     Si p = 1 devolverá el vector producto 𝑣^𝑇 𝐴.
En ambos casos comprobará que las dimensiones son adecuadas.

5.- Crea una función traspuesta(A) que reciba como argumento una matriz 𝐴 y 
devuelva la matriz traspuesta.


"""
n = 4
vector = np.fromfunction(lambda i: ((-1)**(i+1))/(2*(i+1)-1), (n,)) 
matriz = np.zeros((n,n))
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j] = ((i+1)/n)**(j)
        
def suma_dimensiones(A,p):
    filas = A.shape[0]
    cols  = A.shape[1]
    if p==0:
        v = np.array( [sum(A[:,j]) for j in range(cols)])
    elif p == 1:
        v = np.array([sum(A[i,:]) for i in range(filas)])
    return v
    
A = np.array([[1,2,3],[1,2,3],[1,2,3]])
print (suma_dimensiones(A, 0))
print(np.sum(A, axis=0))

print (suma_dimensiones(A, 1))
print(np.sum(A, axis=1))

def producto(A,V,p):
    filas = A.shape[0]
    cols  = A.shape[1]
    
    if p == 0:
        U = np.zeros((filas))
        if cols==np.size(V):
            for i in range(filas):
                for j in range(cols):
                    U[i] += A[i,j]*V[j]
            return U
        else:
            print('Dimensiones incorrectas')
            print(filas, cols,np.shape(V) )
            return None  
    if p == 1:
        U = np.zeros((cols))
        if filas==np.size(V):
            for j in range(cols):
                for i in range(filas):
                    U[j] += A[i,j]*V[i]
            return U
        else:
            print('Dimensiones incorrectas')
            return None   
        
V = np.ones(3)
print(producto(A,V,1))

def traspuesta(A):
    filas = A.shape[0]
    cols  = A.shape[1]
    B = np.zeros((cols,filas))
    for i in range(filas):
        for j in range(cols):
            B[j,i] = A[i,j]
    return B

C = np.array([[1,2,3],[1,2,3]])
print (traspuesta(C))
    