# mar 11 oct 2022 17:01:57 CST
# diagrama_fase.py
# Diego Sarceno (dsarceno68@gmail.com)

# Resumen

# Codificado del texto: UTF8
# Compiladores probados: python3 (Ubuntu 20.04 Linux) 3.8.10
# Instruciones de Ejecución: no requiere nada mas
# python3 diagrama_fase.py

# Librerias
import math as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint

# Sistema de ecuaciones diferenciales
def simplePendulum(y, t):
    # extraer de y los valores de x, vx y 'y'. vy
    theta, omega = y

    f = [omega, -(9.8/0.5)*np.sin(theta)]
    return f


## Tiempo hacia al frente
t = np.linspace(0,20,1000)
ic = np.linspace(-20,20,15)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(simplePendulum, x0, t)
        plt.plot(xs[:,0],xs[:,1], "r-", lw = 0.5)

## Tiempo hacia atras
t = np.linspace(0,-20,1000)
ic = np.linspace(-20,20,15)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(simplePendulum, x0, t)
        plt.plot(xs[:,0],xs[:,1], "r-", lw = 0.5)


plt.grid(color = 'gray', linestyle = 'dashed', linewidth = 0.5)
plt.ylabel(r'$\omega$', fontsize=10)
plt.xlabel(r'$\theta$', fontsize=10)
plt.tick_params(labelsize=7, length=np.pi/2)
plt.xticks(np.arange(-3*np.pi,7*np.pi/2,np.pi/2))
plt.xlim(-12,12)
plt.ylim(-12,12)
plt.title('Diagrama de Fase', fontsize = 15)

# plot en campo vectorial
X, Y = np.mgrid[-20:20:60j, -20:20:60j]
u = Y
v = -(9.8/0.5)*np.sin(X)
plt.quiver(X, Y, u, v, color = 'black')

plt.savefig('diagrama_fase.pdf')
#plt.show()
















###########
