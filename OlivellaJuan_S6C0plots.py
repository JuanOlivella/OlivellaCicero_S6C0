import numpy as np
import matplotlib.pylab as plt


datos=np.genfromtxt("datos.dat")

plt.figure()
plt.plot(datos[:,0],datos[:,1])
plt.title("Solucion con el metodo de Euler")
plt.xlabel("$x$")
plt.ylabel("$y(x)$")
plt.savefig("plot.pdf")
