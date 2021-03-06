import numpy as np
import matplotlib.pyplot as plt
 
# Setting initial variables

    #speed of light
c=3*(10**8)

    # boltzman constant
kb=1.38*(10**-23)
    #integration Time in Seconds
int_time=10**(-3)

    # centre of frequency range in Hz
freq_centre=3*(10**9)

    # baseline length in meters
b=500

    # frequency range
freq_range=2*(10**8)

    # shanon sampling time limit
sampling_time=1/(2*freq_range)

# creating time scale with step size that of sampling time
time_scale=np.arange(0,int_time,sampling_time)

size_array=np.size(time_scale)
output=[]
output1=[]
output2=[]
# Radiation Resistance
R=377

theta_range=np.arange((np.pi/2)-0.02,(np.pi/2)+0.02,0.00025)
  
for theta in theta_range:
    
# creating noise signal with zero mean and finite standard deviation for first and second antenna
    noise_mean=0
    noise_temp=60
    noise_stddev1=(R*kb*noise_temp*freq_range)**0.5
    noise_stddev2=(R*kb*noise_temp*freq_range)**0.5
    noise_stddev=(noise_stddev1*noise_stddev2)**0.5
    noise_signal1=np.random.normal(noise_mean,noise_stddev1,size_array)
    noise_signal2=np.random.normal(noise_mean,noise_stddev2,size_array)

#creating signal received from antennas

        #amplitide of source signal
    source_temp=3
    V_mean=(R*kb*source_temp*freq_range)**0.5
    V_sourcestddev=0.5
    V_source1=V_mean
    V_source2=V_mean
    
        #time difference between two antennas
    time_gap=b*np.cos(theta)/c

    # phase distributor
    k=10
    # Number of bins=k
    delta_freq=freq_range/k
    cosiner1=np.ones((size_array,k))
    cosiner2=np.ones((size_array,k))
    
    for j in range(0,k):
        freq=(freq_centre)-(freq_range/2)+(delta_freq*j)+(delta_freq/2)
        cosiner1[:,j]=cosiner1[:,j]*freq*(time_scale)
        cosiner2[:,j]=cosiner2[:,j]*freq*(time_scale+time_gap*np.ones(size_array))
                                               
    bandwidth_phase1=np.sum(np.cos(cosiner1),axis=-1)
    bandwidth_phase2=np.sum(np.cos(cosiner2),axis=-1)
    
    # signal received from first antenna
    V_signal1=noise_signal1+(V_source1*bandwidth_phase1/(k**0.5))
    V_orig1=V_source1*(bandwidth_phase1/(k**0.5))
    
    #signal received from second antenna
    V_signal2=noise_signal2+(V_source2*bandwidth_phase2/(k**0.5))
    V_orig2=V_source2*(bandwidth_phase2/(k**0.5))
    # correlator
    correlated_output=V_signal1*V_signal2
    actual=V_orig1*V_orig2
    Noise_error=correlated_output-actual
    #integrator
    output.append(np.sum(correlated_output)*sampling_time/int_time)
    output1.append(np.sum(actual)*sampling_time/int_time)
    output2.append(np.sum(Noise_error)*sampling_time/int_time)
NR=2*(noise_stddev1**2)/((int_time/sampling_time)**0.5)

#plotting of Data
ax=plt.figure(1,facecolor="white")
axes=ax.add_axes([0.05,0.1,0.7,0.8], facecolor='white')
axes.set_title("Angular variation of output of integrator",color='green',loc='center',fontsize=14)
ax.text(0.8,0.2,"rms noise={:.3f}x10^-13\n\nsource power {:.3f}x10^-13\n\nbaseline length={}m\n\nintegration time={}s\n\nfrequency centre={} GHz\n\nfrequency range={} MHz\n\nN={}\n\nnoise temperature={}K\n\nsource brightness\ntemperature={:.2f}K\n\nstandard error in mean\nof noise={:.2f} 10^-13\n\nSNR={:.2f}".format((10**13)*(noise_stddev**2),(V_mean**2)*(10**13),b,int_time,freq_centre*(10**-9),freq_range*(10**-6),int_time/sampling_time,noise_temp,source_temp,NR*(10**13),2*(V_mean**2)/(NR)),c='g',fontsize=12,bbox=dict(facecolor="g", alpha=0.1, edgecolor='y'),horizontalalignment="left",verticalalignment="bottom")
axes.xaxis.grid(color='g',linestyle='--',linewidth=0.5)
axes.yaxis.grid(color='g',linestyle='--',linewidth=0.5)
axes.spines['left'].set_color('green')
axes.spines['bottom'].set_color('green')
plt.setp(axes.spines.values(),linewidth=3)
axes.set_xlabel("theta")
axes.set_ylabel("output of integrator")
axes.yaxis.set_label("output of integrator")
axes.xaxis.label.set_color('green')
axes.yaxis.label.set_color('green')
axes.tick_params(axis='both', color='green', labelcolor='g' )
axes.plot(theta_range,output,"g--",label="signal received",linewidth=1)
axes.plot(theta_range,output1,"r--", label="source signal",linewidth=1)
axes.plot(theta_range,output2,"b--", label='eror',linewidth=1)
axes.plot(theta_range,NR*np.ones(np.size(theta_range)),'k--',label='Theoretical error limit')
axes.plot(theta_range,-NR*np.ones(np.size(theta_range)),'k--')
axes.legend()
import os
os.chdir('C:\\Users\\lenovo\\Desktop\\project\\Graphs')
plt.show()








