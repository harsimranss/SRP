import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#square
#coordinates=[(0,0),(1*0.25,0),(1*0.25,1*0.25),(1*0.25,-1*0.25),(0,1*0.25),(-1*0.25,1*0.25),(-1*0.25,0),(-1*0.25,-1*0.25),(0,-0.25),(3,0),(3,3),(3,-3),(0,3),(-3,3),(-3,0),(-3,3),(0,-3),(-3,-3)]

#Y configuration
#coordinates=[(0, 1), (0.69802, 1.403), (1.60362, 1.92585), (2.60862, 2.50609), (3.68415, 3.12705), (4.81537, 3.78016), (5.99304, 4.46008), (-0.69802, 1.403), (-1.60362, 1.92585), (-2.60862, 2.50609), (-3.68415, 3.12705), (-4.81537, 3.78016), (-5.99304, 4.46008), (-0.0, 0.194), (-0.0, -0.8517), (-0.0, -2.01218), (-0.0, -3.25409), (-0.0, -4.56031), (-0.0, -5.92017)]

#Circular concentric1
'''coordinates=[(0,0),(1,0),(0,1),(-1,-1),(0.5,-1)]
for theta in np.arange(0,2*np.pi,2*np.pi/9):
       coordinates.append((6*np.cos(theta),6*np.sin(theta)))
for theta in np.arange(0,2*np.pi,2*np.pi/5):
       coordinates.append((4*np.cos(theta),4*np.sin(theta)))'''

j=[1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
coordinates=[]
for p in range(19):
       coordinates.append((p*np.cos(p)/3.2,p*np.sin(p)/3.2))
                          
#Circular
'''coordinates=[(0,0)]
for theta in np.arange(0,2*np.pi,2*np.pi/19):
       coordinates.append((6*np.cos(theta),6*np.sin(theta)))'''

#semi-circle
'''coordinates=[(0,0)]
for theta in np.arange(0,np.pi+np.pi/17,np.pi/17):
       e=1
       A=6
       coordinates.append((A*np.cos(theta),A*np.sin(theta)))'''

#random
#coordinates=[(5.93, -2.49), (5.15, -1.39), (4.52, 0.06), (-1.62, 3.07), (2.67, 2.29), (-4.43, -5.39), (-1.06, -1.85), (-4.2, 2.18), (2.58, 1.08), (3.34, -2.59), (5.74, 3.83), (4.55, -2.94), (4.2, 2.1), (2.07, 0.66), (3.9, 1.01), (-4.0, -5.43), (-0.32, -2.12), (0.1, 1.37), (1.84, 4.74)]
# creating list to store values of u,v
uvplane=[]

#setting plot parameters
plt.figure(1)
ax=plt.axes(projection='3d')
plt.figure(2)
axes2=plt.axes([0.05,0.1,0.4,0.8],xlim=(-6.5,6.5),ylim=(-6.5,6.5))
axes3=plt.axes([0.55,0.1,0.4,0.8],xlim=(-14,14),ylim=(-14,14))
no_of_tel=0

for x1,y1 in coordinates:
       #counting number of telescopes
       no_of_tel+=1

       # plotting location of telescope
       axes2.plot(x1,y1,'rs',markersize=2)
       
       for x2,y2 in coordinates:
              y=(y1-y2)
              x=(x1-x2)

              # step size for snapshot 
              h=np.pi/8

              # setting u and v list for plotting
              uplane=[]
              vplane=[]

              # declination
              delta=np.pi/4

              # lattitude
              theta=np.pi/6

              # number of snapshots
              snapshot=0
              
              # calculating values of u,v with earth rotation
              
              for phi in np.arange(0,h,h):
                   #adding number of snapshots  
                   snapshot+=1

                   #calculating u and v from X, Y in telescopes and declination and hour angle
                   v=y*(np.cos(theta)*np.cos(phi)*np.sin(delta)+np.cos(delta)*np.sin(theta))+x*np.sin(phi)*np.sin(delta)
                   u=-y*np.cos(theta)*np.sin(phi)+x*np.cos(phi)

                   # appending it to u-plane and v-plane
                   uplane.append(u)
                   vplane.append(v)

                   # multiplying by 1000 for wavelength = 0.1 m  and unit of 100m 
                   u=1000*u
                   v=1000*v

                   # adding u,v coordinate to list
                   uvplane.append((u,v))

              # plotting uv line for 1 pair
              axes3.plot(uplane,vplane,"bs-",markersize=0.5,linewidth=0.3)

# removing zeros from uv plane
for j in range(no_of_tel*snapshot):
       uvplane.remove((0,0))
####del
print(no_of_tel)
       
#axes2.grid()
#axes3.grid()
       
# defining exp(i*2pi(ux+vy))
def z(u,v):
    l=np.arange(l_min,l_max+h,h)
    m=np.arange(m_min,m_max+h,h)
    X,Y=np.meshgrid(l,m)
    y=np.exp(2*np.pi*(complex(0,1))*(-u*X-v*Y))
    return y

# setting limits of lm plane
l_min=-2*(10**-3)
l_max=2*(10**-3)
m_min=-2*(10**-3)
m_max=2*(10**-3)
h=10**-5
delta_v=12.5*(10**6)
R=377
kb=1.38*(10**-23)
Tb=585
Ao=np.pi*(4.5**2)
lambda1=0.1
def zz(x,y):
       d=x**2+y**2
       if d<10**-6 and d>0.64*(10**-6):
              return float(1)
       else:
              return float(0)
              
#defining actual brightness distribution
def I(l,m):
     return (kb*Tb*Ao/(lambda1**2))*(np.exp(1000*(10**6)*(-(l-lo)**2-(m-mo)**2))+np.exp(-1000*(10**6)*(((l-l1)**2+(m-m1)**2)))+np.exp(-1000*(10**6)*(((l-l2)**2+(m-m2)**2))))
 
#creating  dictionary to store response of each uv pair
w={}

#setting l amd m axis
l=np.arange(l_min,l_max+h,h)
m=np.arange(m_min,m_max+h,h)

#setting arrays for image , synthesised beam and meshgrid
s=np.size(m)
image=np.zeros((s,s))
Sbeam=np.zeros((s,s))
X,Y=np.meshgrid(l,m)
Noise_image=np.zeros((s,s))
# adding elements in actual brightness distribution
lo=0.4*(10**-3)
mo=0.2*(10**-3)
l1=-0.4*(10**-3)
m1=0.6*(10**-3)
l2=0.7*(10**-3)
m2=0.5*(10**-3)

#weight
weight={}

# list for evaluation of overlappig of 
overlap1=[]
overlap2=[]
for u,v in uvplane:
    c1=0
    c2=0
    for u1,v1 in uvplane:
        if ((u-u1)**2+(v-v1)**2)<8100:
            c1=c1+1
        if ((u-u1)**2+(v-v1)**2)<2025:
            c2=c2+1
    overlap1.append(c1)
    overlap2.append(c2)

    # adding element to weight dictionary
    weight[(u,v)]=1
    
# adding noise

noise_temp=60
noise_stddev=6.98*(10**-16)
noise_mean=0

Act_image=I(X,Y)
for u,v in uvplane:
    exponent=z(-u,-v)
    # calculating response
    noise_response=(np.random.normal(0,noise_stddev)/(R*delta_v))

           # response of uv pair 
    w[(u,v)]=(np.sum(Act_image*z(u,v)))*h*h+ noise_response

    # creating image from response
    image=image+(exponent*(w[(u,v)]/(weight[(u,v)]*2*np.pi)))*8100

    #creating noise image from noise response
    #Noise_image=Noise_image+(exponent*(noise_response/(weight[(u,v)]*2*np.pi)))*8100
    
    #creating synthesised beam
    Sbeam=Sbeam+(exponent/(weight[(u,v)]))

# parametrs/outputs for evaluation in noise reduction of configurations
power=(image.real**2)
output1=np.std(Noise_image.real)
output2=np.max(Noise_image.real)
output3=np.min(Noise_image.real)
output4=output2-output3
print('mean noise deviation is {}, max is {}, min is {}, bound is {}, max of image is {} '.format(output1,output2,output3,output4,np.max(image.real)))

#plotting synthesised beam
surf=ax.contourf(X,Y,Sbeam.real,30,cmap='gnuplot')
plt.sca(ax)
plt.colorbar(surf)
ax.set_title('Synthesised Beam')

# settig labels of telescope arrangement plot
axes2.set_title('Arrangement of Telescopic array')
axes3.set_title('uv plane')
axes3.xaxis.set_label('u')
axes3.yaxis.set_label('v')

# setting plot for image analysis
plt.figure(3)
axesf=plt.axes([0.05,0.1,0.45,0.8],projection='3d')
axesf2=plt.axes([0.55,0.1,0.45,0.8],projection='3d')
axesf.set_title('actual Distribution')
axesf2.set_title('synthesised image')
plot1=axesf.contourf(X,Y,Act_image,30,cmap='gnuplot')
plt.sca(axesf)
plt.colorbar(plot1)
plot2=axesf2.contourf(X,Y,image.real,30,cmap='gnuplot',vmin=0)
plt.sca(axesf2)
plt.colorbar(plot2)
power=(Sbeam.real)**2

# setting plot for noise image analysis
plt.figure()
ax5=plt.axes(projection='3d')
noise_ax=plt.contourf(X,Y,Noise_image.real,30,cmap='gnuplot')

# creating plot for overlapping analysis
plt.figure()
plt.subplot(211)
a,bb,cc=plt.hist(overlap1,np.arange(-0.5,10,1),density=True)
print(a)
plt.subplot(212)
a1,bb,cc=plt.hist(overlap2,np.arange(-0.5,10,1),density=True)
print(a1)
plt.show()


