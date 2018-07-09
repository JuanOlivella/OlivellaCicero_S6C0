import numpy as np
import matplotlib.pylab as plt


datos=np.genfromtxt("datos.dat")

x = datos[:,0]

y = datos[:,1]

error = abs((y-np.exp(x))/(np.exp(x)))

plt.figure()
plt.plot(x,y)
plt.title("Solucion con el metodo de Euler")
plt.xlabel("$x$")
plt.ylabel("$y(x)$")
plt.savefig("Solucion.pdf")


plt.figure()
plt.plot(x,error)
plt.title("Error con el metodo de Euler")
plt.xlabel("$x$")
plt.ylabel("$Error$")
plt.savefig("Error.pdf")
