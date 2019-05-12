import numpy as np
from scipy.fftpack import ifft, fft, fftfreq
import matplotlib.pyplot as plt
#Se cargan los datos signal.dat y sumaSignal.dat
#Se utiliza unpack para separar los valores directamente
S_signal,S_signal_t=np.genfromtxt('signalSuma.dat', unpack=True)
signal,signal_t=np.genfromtxt('signal.dat', unpack=True)
#Plot de los datos
plt.figure()
grafica,ejes=plt.subplots(2,1,1)
ejes[0].plot(signal,signal_t,c='yellow')
ejes[1].plot(S_signal,S_signal_t,c='red')
ejes[0].set_xlabel('Amplitud')
ejes[0].set_ylabel('Tiempo')
ejes[1].set_xlabel('Amplitud Suma')
ejes[1].set_ylabel('Tiempo')
ejes[0].set_title('Datos Signal')
ejes[1].set_title('Datos Signal Suma')
plt.savefig('Datos_iniciales.pdf')
#plt.show()
plt.close()
#Se define la implementacion propia de la transformada discreta de Fourier
# Se hace la implementacion de fourier cabiando la forma del exponencial debido a que presento problemas corriendo con los el seno y coseno
#def fourier(datos):
#	fourier=[]
#	for n in range(0,len(datos)):
#		f=0.0
#		for k in range(0,len(datos)):
#			f+= (datos[k])*(np.cos(-2*np.pi*k*n/len(datos))+1j*np.sin(-2*np.pi*k*n/len(datos)))
#		fourier.append(f)
#	return fourier
def transformada(datos):
    fourier=[]
    for i in range(len(datos)):
        #Se inicializa la variable que guarda el valor de la transformada para cada punto y luego se agrega al arreglo
        trans_f=0+0j
        for l in range(len(datos)):
            trans_f+=datos[l]*np.exp(-(2j*np.pi*i*l)/len(datos))
        fourier.append(trans_f)
    return np.array(fourier)
#Se aplica la transformada a cada una de las señales y se usa la funcion fftfreq del paquete fft para obtener la frecuencia de la senhal
#SignalSuma
transformada_real_suma=np.sqrt(np.real(transformada(S_signal_t))**2+np.imag(transformada(S_signal_t))**2)
frecuencia_suma=np.fft.fftfreq(len(S_signal_t),S_signal[1]-S_signal[0])
#Signal
transformada(signal_t)=transformada(signal_t)
frecuencia_signal=np.fft.fftfreq(len(signal_t),signal[1]-signal[0])
transformada_real_signal=np.sqrt(np.real(transformada(signal_t))**2+np.imag(transformada(signal_t))**2)
#Se grafican nuevamente las señales transfomadas en funcion de la frecuencia
plt.figure()
plt.plot(frecuencia_suma,transformada_real_suma,c='blue')
plt.plot(frecuencia_signal,transformada_real_signal,c='black')
plt.ylabel('Amplitud')
plt.xlabel('Frecuencia')
plt.xlim(-500,500)
plt.title('Transformada')
plt.savefig('Datos_transformados.pdf')
plt.close()
#Se realizan los espectogramas con los parametros similares a los vistos en la referencia dada
#Se establece Fs de 2 para tomar dos muestras de frecuencia por unidad
plt.figure()
plt.specgram(S_signal_t,Fs=2,NFFT=256)
plt.xlabel('Tiempo en [s]'')
plt.ylabel('Frecuencia en [Hz/s]')
plt.title('Espectrograma Suma')
plt.savefig('Espectro_suma.pdf')
plt.figure()
plt.specgram(signal_t,Fs=2,NFFT=256,noverlap=128)
plt.title('Espectrograma Signal')
plt.ylabel('Frecuencia en [Hz/s]')
plt.xlabel('Tiempo en [s]'])
plt.savefig('Espectro_signal.pdf')
