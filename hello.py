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
hhh=np.arange((np.pi/2)-0.02,(np.pi/2)+0.02,0.00025)
  
for theta in hhh:
    
# creating noise signal with zero mean and finite standard deviation for first and second antenna
    noise_mean=0
    noise_temp=60
    noise_stddev=(kb*noise_temp*freq_range)**0.5
    noise_signal1=np.random.normal(noise_mean,noise_stddev,size_array)
    noise_signal2=np.random.normal(noise_mean,noise_stddev,size_array)

#creating signal received from antennas

        #amplitide of source signal
    source_temp=3
    V_mean=(kb*source_temp*freq_range)**0.5
    V_sourcestddev=0.5
    V_source1=V_mean
    V_source2=V_mean
        # angle of the source from the ground
    
    
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
    #integrator
    output.append(np.sum(correlated_output)*sampling_time/int_time)
    output1.append(np.sum(actual)*sampling_time/int_time)
    #display
#print("output of integrator is {}".format(output))
#print("output of actual signal {}".format(output1))
ax=plt.figure(1,facecolor="black")
axes=ax.add_axes([0.05,0.1,0.7,0.8], facecolor='black')
axes2=ax.add_axes([0.77,0.1,0.22,0.8], facecolor='black')
axes.set_title("Angular variation of output of integrator",color='green',loc='center',fontsize=14)
axes2.text(0,0.1,"rms noise={}\n\nsource power {}\n\nbaseline length={}m\n\nintegration time={}s\n\nfrequency centre={}\n\nfrequency range={}\n\nN={}\n\nnoise temperature={}K\n\nsource brightness\ntemperature={:.2f}K\n\nstandard error in mean\nof noise temperature={:.2f}\n\nbrightness temperature/SEM={:.2f}".format(noise_stddev**2,V_mean**2,b,int_time,freq_centre,freq_range,int_time/sampling_time,noise_temp,source_temp,noise_temp/((int_time/sampling_time)**0.5),source_temp/(noise_temp/((int_time/sampling_time)**0.5))),c='g',fontsize=10,bbox=dict(facecolor="g", alpha=0.2, edgecolor='y'),horizontalalignment="left",verticalalignment="bottom")
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
axes.plot(hhh,output,label="signal received",color="green",linewidth=3)
axes.plot(hhh,output1,"r", label="source signal",linewidth=1)
axes.legend()
plt.show()
"""a=plt.figure(2)
ax=a.add_axes([0.05,0.5,0.5,0.35])
ax.plot(time_scale,V_signal1)
bx=a.add_axes([0.05,0.05,0.5,0.35])
bx.plot(time_scale,V_signal2)
aa=a.add_axes([0.6,0.5,0.35,0.35])
aa.plot(time_scale,V_orig1)
bb=a.add_axes([0.6,0.05,0.35,0.35])
bb.plot(time_scale,V_orig2)
plt.show()
a2=plt.figure(3)
plt.subplot(211)
plt.plot(time_scale,correlated_output)
plt.subplot(212)
plt.plot(time_scale,actual)
plt.show()"""
#plt.plot(np.arange(np.pi/4,(np.pi/4)+0.1,0.001),output,np.arange(np.pi/4,(np.pi/4)+0.1,0.001),output1)








