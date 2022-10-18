# mar 18 oct 2022 12:04:34 CST
# overDampingPD.py
# Diego Sarceno (dsarceno68@gmail.com)

# Resumen

# Codificado del texto: UTF8
# Compiladores probados: python3 (Ubuntu 20.04 Linux) 3.8.10
# Instruciones de Ejecución: no requiere nada mas
# python3 overDampingPD.py

# Librerias
import math as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint

# Sistema de ecuaciones diferenciales
def odeSystem(y, t):
    # extraer de y los valores de x, vx y 'y'. vy
    theta, omega = y

    f = [omega, 10*omega + 16*theta]
    return f

## Tiempo hacia al frente
t = np.linspace(0,20,1000)
ic = np.linspace(-20,20,20)
for r in ic:
  for s in ic:
    y = [r, s]
    xs = odeint(odeSystem, y, t)
    plt.plot(xs[:,0], xs[:,1], "r-")


## Tiempo hacia atras
t = np.linspace(0,-20,1000)
ic = np.linspace(-20,20,20)
for r in ic:
  for s in ic:
    x0 = [r, s]
    xs = odeint(odeSystem, x0, t)
    plt.plot(xs[:,0], xs[:,1], "r-")


plt.grid(color = 'gray', linestyle = 'dashed', linewidth = 0.5)
plt.ylabel(r'$\omega$', fontsize=10)
plt.xlabel(r'$\theta$', fontsize=10)
plt.tick_params(labelsize=15)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title('Diagrama de Fase, Mov. Sobremortiguado', fontsize = 15)

# Plot the vectorfield.
X, Y = np.mgrid[-5:5:40j, -5:5:40j]
u=Y
v=-2*(9.8/0.5)**(1/2)*Y - (9.8/0.5)*np.sin(X)
plt.quiver(X, Y, u, v, color = 'b')

plt.savefig('overDampingPD.pdf')
