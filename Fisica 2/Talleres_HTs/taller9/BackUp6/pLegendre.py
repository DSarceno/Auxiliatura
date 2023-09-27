# @Author: Diego Sarceno
# Date: 15.10.2020

import sympy as sym
import math as m
import sympy.plotting as splt
import numpy as np
import matplotlib.pyplot as plt
import sys

x = sym.symbols('x')

x_val = np.linspace(-1,1,1000)
p_val = np.zeros(len(x_val))
# la funcion recibe enteros
def P(i):
    '''Esta funcion toma como parametro un entero, y devuelve el arreglo
    de los valores del i-esimo polinomio de legendre valuado en x_val.'''
    a = 1/(2**i * m.factorial(i))
    dif = sym.diff((x**2 - 1)**i, x, i)
    p_lam = sym.lambdify(x,a*dif, modules=['numpy'])
    for j in range(len(x_val)):
        p_val[j] = p_lam(x_val[j])
    return p_val

n = int(sys.argv[1])

for i in range(n):
    lab = '$P_{num}$'.format(num = str(i))
    plt.plot(x_val,P(i),label=lab)

plt.title('Polinomios de Legendre')
plt.legend()
plt.xlim(-1,1)
plt.ylim(-1.25,1.25)
plt.xlabel('$x$')
plt.ylabel('$P_n$')
plt.savefig('polinomiosLegendre.pdf')
plt.show()

