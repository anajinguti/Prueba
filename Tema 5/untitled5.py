#Continuación partición de un intervalo.
"""
- Crear una partición del intervalo [0,2pi] en 100 elementos. 
1) Evaluar la función f(x) = sin(x) en los puntos de la partición. 
2) Calcular f'(x) en los puntos internos de la partición, utilizando:
    f'(xi)= ((f(xi+Ax)-f(xi-Ax))/2Ax) equivalente a f'(xi) = ...
    Para los extremos, tenemos que utilizar otras dos fórmulas para evaluar la derivada: 
        f'()
3)  Calcular el error cometido al aproximar la derivada con esa fórmula: E(xi) = f'(xi) - cos(xi)
"""
#Partición del intervalo. 
import numpy as np
import math
a = 0. 
b = 2.*math.pi
n = 100

vector = np.linspace(a, b, n) #Almacena los valores de la partición.
print(f"Los valores de la partición son {vector}")

#Creo un vector donde voy a almacenar los valores de la partición en la función seno. 
valores_funcion_particiones = np.zeros(len(vector))
def funcion(x): 
    resultado = math.sin(x)
    return resultado

for i in range (len(vector)): 
    valores_funcion_particiones[i]= funcion(vector[i])
print(f"Los valores de la partición en la función seno son {valores_funcion_particiones}")
    
"""def derivada (x1, x2): 
    deltax = abs(x2-x1)
    deriv = (funcion(x1)- funcion(x2))/2.*deltax
    return deriv
"""

# Calcular la derivada en los puntos interiores de la partición utilizando la
# fórmula aproximada de la diferencia finita centrada
def derivada(x, f):
    df = np.zeros(n)
    Deltax = x[1] - x[0]    # Es lo mismo que el paso (step)
    for i in range(1,n-1):
        df[i] = (f[i+1] - f[i-1])/(2.0*Deltax)

# Calcular la derivada en los puntos extremos de la partición utilizando las
# fórmulas aproximadas de la diferencia finita adelantada y atrasada
df[0] = (f[1] - f[0])/Deltax
df[n-1] = (f[n-1] - f[n-2])/Deltax

# Calcular el error cometido al estimar la derivada mediante la fórmula
# aproximada
err = np.zeros(n)
for i in range(n):
    err[i] = df[i] - math.cos(x[i])

print(err)