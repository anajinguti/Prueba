#Ejercicio propuesto 3. Diapositiva 35. 
#1. Crea un vector de tamaño n cuyos elementos sean v(i)= ((-1)**i)/2i-1
import numpy as np
n = 5 #Tamaño del vector. 
"""Ejemplo: v[0] = (-1)**1/2i-1"""

def funcionv(i): 
    resultado = ((-1.)**i)/(2.*i-1.)
    return resultado
    
v = np.zeros(n)
for i in range (n): 
    v[i] = funcionv(i+1.)
    
print(f"El vector pedido es {v}")

#2. Crea una matriz cuadrada de nxn cuyos elementos sean A(i,j) = (i/n)**(j-1).
matriz = np.zeros((n, n))
def funcionA(i,j): 
    