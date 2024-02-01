import numpy as np
import math

# Partición equiespaciada usando arrays de Numpy
a = 0.0          # Primer punto del intervalo
b = 2*math.pi    # Último punto del intervalo
n = 100          # Número de puntos en el intervalo

# Utilizamos la función linspace() de Numpy
x = np.linspace(a, b, n)
print(x)

# Evaluar la función sin(x) en los puntos que forman la partición
f = np.zeros(n)
for i in range(n):
    f[i] = math.sin(x[i])
# Se puede hacer sin el bucle utilizando np.sin(x) en lugar de math.sin(x)
# f = np.sin(x)

# Calcular la derivada en los puntos interiores de la partición utilizando la
# fórmula aproximada de la diferencia finita centrada
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