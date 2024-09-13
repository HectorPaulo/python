import numpy as np
entradaa = 50053043044000159433307046053.0

entrada = entradaa * 2
lenEntrada = 30
a = 1
b = -80.5
c = entrada
discriminante = (b**2)+(((-1)*(b)+(4*a*c))**(1/2))
coeficientes = [a, b, discriminante]
soluciones = np.roots(coeficientes)
print(discriminante
      )
