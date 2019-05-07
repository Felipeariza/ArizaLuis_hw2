import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


# Se leen los datos de signal.dat 
signal = np.genfromtxt('signal.dat',usecols=[0,2])

# Se grafican los datos y se guarda en un pdf
plt.plot(signal[:,0],signal[:,1],label='Signal')
plt.title('Senal Signal')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.savefig('ArizaFelipe_signal.pdf')
plt.close()

# Se hace la implementacion de fourier
def fourier(datos):
	fourier=[]
	for n in range(0,len(datos)):
		f=0.0
		for k in range(0,len(datos)):
			f+= (datos[k])*(np.cos(-2*np.pi*k*n/len(datos))+1j*np.sin(-2*np.pi*k*n/len(datos)))
		fourier.append(f)
	return fourier

fts=fourier(signal[:,1])
fts=np.asarray(fts) 

ffts=np.fft.fftfreq(len(fts),0.00015)

####Cuarto punto: Se hace la grafica de la transformada de Fourier y se guarda en un pdf
plt.plot(abs(ffts),abs(fts),label='Signal',color='g')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')
plt.title('Fourier de signal')
plt.legend()
plt.xlim([0,1000])
plt.savefig('ArizaFelipe_TF.pdf')
plt.close()

