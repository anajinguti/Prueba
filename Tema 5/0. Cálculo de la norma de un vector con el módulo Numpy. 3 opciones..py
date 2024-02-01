#VECTOR NUMPY. Ejercicio 
import numpy as np
import math
v = np.array([1.0, 2.1, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 10.0])
sumatorio = 0.

#OPCIÓN 1. Aplicar la definición del sumatorio y hacer que pase por todos los valores del array
for i in range (len(v)):
    print(i) #Se puede poner para comprobar el valor de i cada vez que se repite el bucle. 
    sumatorio += (v[i]**2)
    
n = math.sqrt(sumatorio)    
print(f"La norma del vector v es {n}")

# Opción 2 (utilizamos la función norm() de Numpy,
# que está dentro del submódulo np.linalg, de "linear algebra")
n2 = np.linalg.norm(v)
print('Norma 2:',n2)

# Opción 3 (aplicamos la definición pero de una forma más eficiente y
# escribiendo menos líneas de código)
n3 = math.sqrt(np.sum(v**2))
print('Norma 3:',n3)