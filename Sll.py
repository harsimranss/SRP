import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#Y configuration
coordinates=[(0, 1), (0.69802, 1.403), (1.60362, 1.92585), (2.60862, 2.50609), (3.68415, 3.12705), (4.81537, 3.78016), (5.99304, 4.46008), (-0.69802, 1.403), (-1.60362, 1.92585), (-2.60862, 2.50609), (-3.68415, 3.12705), (-4.81537, 3.78016), (-5.99304, 4.46008), (-0.0, 0.194), (-0.0, -0.8517), (-0.0, -2.01218), (-0.0, -3.25409), (-0.0, -4.56031), (-0.0, -5.92017)]

#Circular concentric1
'''coordinates=[(0,0),(1,0),(0,1),(-1,-1),(0.5,-1)]
for theta in np.arange(0,2*np.pi,2*np.pi/9):
       coordinates.append((6*np.cos(theta),6*np.sin(theta)))
for theta in np.arange(0,2*np.pi,2*np.pi/5):
       coordinates.append((4*np.cos(theta),4*np.sin(theta)))'''
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
              
              for phi in np.arange(-np.pi/4,np.pi/4+h,h):
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
h=0.5*10**-5
delta_v=12.5*(10**6)
R=377
kb=1.38*(10**-23)
Tb=585/(5**0.5)
Ao=np.pi*(4.5**2)
lambda1=0.1
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
ooo=1
noise_temp=60
noise_stddev=6.98*(10**-16)
noise_mean=0
Noise_image=np.zeros((s,s))
for u,v in uvplane:
    exponent=z(-u,-v)
        #creating synthesised beam
    Sbeam=Sbeam+(exponent/(weight[(u,v)]))
power=(Sbeam.real**2)
# calculating THETAhpbw
P_l=power[400,:]
P_m=power[:,400]
c3=0
ratio=1
while ratio>0.5 :
       ratio=P_l[400+c3]/P_l[400]
       c3=c3+1
Theta_l=2*60*h*c3*180/np.pi
c4=0
ratio=1
while ratio>0.5 :
       ratio=P_m[400+c4]/P_m[400]
       c4=c4+1
Theta_m=(2*60*h*c4)*180/np.pi

# calculating Side lobe level
print('dimension of theta hpbw are {}x{}'.format(Theta_l,Theta_m))

plt.show()
def plotj(i):
	plt.plot(l,power[i,:],linewidth=0.3)
	plt.grid()
	plt.title(str(i))
	
plt.figure()
plt.axes(ylim=(0,power[400,400]))
for j in np.arange(0,101,2):
       plt.get_current_fig_manager().window.state('zoomed')
       plotj(j)
       ll=0
plt.figure()
plt.axes(ylim=(0,power[400,400]))
for j in np.arange(101,201,2):
       plt.get_current_fig_manager().window.state('zoomed')
       plotj(j)
       ll=0

plt.figure()
plt.axes(ylim=(0,power[400,400]))
for j in np.arange(201,301,2):
       plt.get_current_fig_manager().window.state('zoomed')
       plotj(j)
       ll=0

plt.figure()
plt.axes(ylim=(0,power[400,400]))
for j in np.arange(301,401,2):
       plt.get_current_fig_manager().window.state('zoomed')
       plotj(j)
       ll=0
plt.figure()
plt.axes(ylim=(0,power[400,400]))
for j in np.arange(380,401,1):
       plt.get_current_fig_manager().window.state('zoomed')
       plotj(j)
       ll=0
plt.figure()
plt.axes(ylim=(0,power[400,400]))
plotj(401)
plt.get_current_fig_manager().window.state('zoomed')

def Slc(SL):
       SLL=10*np.log(SL/power[400,400])/np.log(10)
       print('SLL is {}'.format(SLL))
       return SLL

plt.show()
