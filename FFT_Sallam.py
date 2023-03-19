'''FFT_Sallam.py'''
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft 
def plot_fft(x,sr,t,xlabel1,xlabel2,ylabel1,ylabel2):
    X = fft(x)
    N = len(X)
    n = np.arange(N)
    T = N/sr
    freq = n/T 

    plt.figure(figsize = (12, 6))
    plt.subplot(121)

    plt.plot(freq, np.abs(X/N), 'hotpink')
    plt.xlabel(xlabel1)
    plt.ylabel(ylabel1)
    plt.xlim(0, 150)
    print(max(np.abs(X/N))) 
 
    plt.subplot(122)
    plt.plot(t, x, 'g')
    plt.xlabel(xlabel2)
    plt.ylabel(ylabel2)
    plt.tight_layout()
    plt.show()