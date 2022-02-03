####### Con vectores: #######

import matplotlib.pyplot as plt
import math

def f(x):
  return math.sin( 2 * math.pi * x )

n = 100  # Cantidad de puntos

X = [ x/(n-1) for x in range(n) ] 
Y = [ f(x) for x in X ]

plt.plot(X, Y)    # plt.plot recibe 2 listas de igual longitud, la primera para el eje X, la segunda para el eje Y
plt.show()        # Luego de generar el gráfico, lo mostramos

####### Usando numpy: #######

import matplotlib.pyplot as plt
import numpy as np

# Cantidad de puntos
n = 100

X = np.linspace(0, 1, n)
print('X =\n', X,'\n')

# Se calcula la función sobre cada elemento por separado
Y = np.sin( 2 * np.pi * X )
print('Y =\n', Y,'\n')

plt.plot(X, Y)
plt.show()