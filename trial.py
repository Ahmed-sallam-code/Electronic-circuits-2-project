import FFT_Sallam as wowman
import numpy as np 
import com_ard as com
com.get_serial()

sr = len(com.acceleration_listx)/1
t = np.arange(0,1,1/(len(com.acceleration_listx)))
s=com.accel_listx()
for i in range(len(s)):   
    try:  
        s[i]=float(s[i])
    except:
        s[i]=(float(s[i-10])+float(s[i+10]))/2
        print("Error encountered, couldn't covert to float")
print(s)  

d=com.accel_listy()
for i in range(len(d)):   
    try:  
        d[i]=float(d[i])
    except:
        d[i]=(float(d[i-10])+float(d[i+10]))/2
        print("Error encountered, couldn't covert to float")

f=com.accel_listx()
for i in range(len(f)):   
    try:  
        f[i]=float(f[i])
    except:
        f[i]=(float(f[i-10])+float(f[i+10]))/2
        print("Error encountered, couldn't covert to float")        

wowman.plot_fft(s,sr,t,"Frequency(hz)","time(s)","amplitude x","amplitude")
wowman.plot_fft(d,sr,t,"Frequency(hz)","time(s)","amplitude y","amplitude")
wowman.plot_fft(f,sr,t,"Frequency(hz)","time(s)","amplitude z","amplitude")
