import matplotlib.pyplot as plt
import numpy as np

# Cantidad de puntos
n = 1000

X = np.linspace(-1, 1, n)

# Se calcula la función sobre cada elemento por separado
Y = np.absolute(X)

plt.plot(X, Y)
plt.show()


### Parte 2 ###


n = 1000

X = np.linspace(-5,5,n)

Y = np.exp(-X**2/2)

plt.plot(X, Y, "b--")
plt.show()