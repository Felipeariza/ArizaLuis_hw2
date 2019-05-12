# -*- coding: utf-8 -*-    
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

edificio0 = np.loadtxt("w0.dat")
edificio1 = np.loadtxt("w1.dat")
edificio2 = np.loadtxt("w2.dat")
edificio3 = np.loadtxt("w3.dat")
edificio4 = np.loadtxt("w4.dat")
freq = np.loadtxt("w.dat")

w = freq[:,0]/np.sqrt(2)




t = edificio0[:,0]

x0 = np.delete(edificio0, (0) ,axis = 1)
x1 = np.delete(edificio1, (0) ,axis = 1)
x2 = np.delete(edificio2, (0) ,axis = 1)
x3 = np.delete(edificio3, (0) ,axis = 1)
x4 = np.delete(edificio4, (0) ,axis = 1)
umax = np.delete(freq, (0) ,axis = 1)

#for i in range(int(len(x[:,0])/5)):
#    plt.scatter(x[i*5][0],y[0])

plt.figure()
y = np.linspace(0,99,3)

plt.plot(t,x0[:,0], label = "$u_1(t)$")
plt.plot(t,x0[:,1], label = "$u_2(t)$")
plt.plot(t,x0[:,2], label = "$u_3(t)$")
plt.legend()
plt.xlabel("t",fontsize=12)
plt.ylabel(r"$u_i$",fontsize=12)
plt.title(r"$u_i$", fontsize = 12)
plt.tight_layout()
plt.savefig("w0.png", bbox_inches = "tight")





plt.figure()
plt.plot(w,umax[:,0], label = "u1_max(w)")
plt.plot(w,umax[:,1], label = "u2_max(w)")
plt.plot(w,umax[:,2], label = "u3_max(w)")
plt.legend()
plt.xlabel(r"w / $\sqrt{k/m}$", fontsize = 15)
plt.ylabel(r"$u_i$ max", fontsize = 15)
plt.title("Amplitud máxima vs w")
plt.savefig("w.png",bbox="tight")



plt.figure()
plt.plot(t,x1[:,0], label = "$u_1(t)$")
plt.plot(t,x1[:,1], label = "$u_2(t)$")
plt.plot(t,x1[:,2], label = "$u_3(t)$")
plt.legend()
plt.xlabel("t",fontsize=15)
plt.ylabel(r"$u_i$",fontsize=15)
plt.title(r"$u_i$ con $w = 0.2\sqrt{k/m}$", fontsize = 15)
plt.savefig("w1.png", bbox_="tight")

plt.figure()
plt.plot(t,x2[:,0], label = "$u_1(t)$")
plt.plot(t,x2[:,1], label = "$u_2(t)$")
plt.plot(t,x2[:,2], label = "$u_3(t)$")
plt.legend()
plt.xlabel("t",fontsize=15)
plt.ylabel(r"$u_i$",fontsize=15)
plt.title(r"$u_i$ con $w = 0.452\sqrt{k/m}$", fontsize = 15)
plt.savefig("w2.png", bbox_="tight")

plt.figure()
plt.plot(t,x3[:,0], label = "$u_1(t)$")
plt.plot(t,x3[:,1], label = "$u_2(t)$")
plt.plot(t,x3[:,2], label = "$u_3(t)$")
plt.legend()
plt.xlabel("t",fontsize=15)
plt.ylabel(r"$u_i$",fontsize=15)
plt.title(r"$u_i$ con $w = 1.236\sqrt{k/m}$", fontsize = 15)
plt.savefig("w3.png", bbox_="tight")

plt.figure()
plt.plot(t,x4[:,0], label = "$u_1(t)$")
plt.plot(t,x4[:,1], label = "$u_2(t)$")
plt.plot(t,x4[:,2], label = "$u_3(t)$")
plt.legend()
plt.xlabel("t",fontsize=15)
plt.ylabel(r"$u_i$",fontsize=15)
plt.title(r"$u_i$ con $w = 1.796\sqrt{k/m}$", fontsize = 15)
plt.savefig("w4.png", bbox_="tight")







