#NUMPY.
"""Calcular la traza (suma de los elementos de la diagonal) de una matriz. 2 Opciones."""

#OPCIÓN 1. Aplicando la definición.
import numpy as np 
matriz = np.array([[2, 9, 4], [3, 6, 7], [5, 0, 1]])
dA = np.diag(matriz)
N = np.size(dA)
traza = 0.

for i in range(N): 
    traza += dA[i]
    
#print(f"La traza de la matriz es: {traza}")

#OPCIÓN 2. Utilizando la función de numpy.trace().
traza2 = np.trace(matriz)
print(f"La traza de la matriz es: {traza2}")