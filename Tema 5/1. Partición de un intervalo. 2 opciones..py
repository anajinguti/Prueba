#NUMPY. Ejercicio de partición de intervalo. 
"""Crear una partición del intervalo [0,2pi] en 100 elementos. 2 opciones."""

#OPCIÓN 1. Manualmente con un bucle "for".
import numpy as np
import math
a = 0. 
#b = 2.*math.pi
b = 3.
N = 3
p = np.zeros(N)
x = (b-a)/N

for i in range (N):
    p[i] = a + i*x
    
#print(p)

#OPCIÓN 2. Utilizando la función numpy.linspace(inicio, fin, num)
vector = np.linspace(a, b, N) 
print(vector)