import matplotlib.pyplot as plt
import numpy as np

# SE DEFINEN LAS CONSTANTES
v0 = 10
k = 0.1

# SE CREA LA LISTA CON ELEMENTOS DE TIEMPO
t = np.linspace(0,100,1000)

# SE VALUAN LAS FUNCIONES Y SE CREAN SUS ARREGLOS
v = v0 * np.exp(-k*t)
x = (v0 / k) * (1 - np.exp(-k*t))


# SE CREAN LOS PLOTS Y SE MUESTRAN PARA RESETEAR LA GRAFICA ANTERIOR
# v-t
plt.grid(color='darkgrey',linestyle='--', linewidth=1)
plt.xlabel('Tiempo')
plt.ylabel('Velocidad')
plt.title('Gráfica v-t')
plt.plot(t,v, '-b')
plt.savefig('problema3_1.pdf')
plt.show()

# x-t
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Gráfica x-t')
plt.plot(t,x, '-g')
plt.savefig('problema3_2.pdf')
plt.show()

# v-x
plt.xlabel('Posición')
plt.ylabel('Velocidad')
plt.title('Gráfica x-t')
plt.plot(x,v, '-r')
plt.savefig('problema3_3.pdf')
plt.show()








# SE MUESTRAN LAS GRAFICAS
#plt.show()
