import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#square
#coordinates=[(0,0),(1*0.25,0),(1*0.25,1*0.25),(1*0.25,-1*0.25),(0,1*0.25),(-1*0.25,1*0.25),(-1*0.25,0),(-1*0.25,-1*0.25),(0,-0.25),(3,0),(3,3),(3,-3),(0,3),(-3,3),(-3,0),(-3,3),(0,-3),(-3,-3)]

#Y configuration
#coordinates=[(0.0, 0.0), (-0.2857142857142857, 0.4942857142857143), (-0.5714285714285714, 0.9885714285714285), (-0.8571428571428571, 1.4828571428571427), (0.2857142857142857, 0.4942857142857143), (0.5714285714285714, 0.9885714285714285), (0.8571428571428571, 1.4828571428571427), (0.0, -0.5714285714285714), (0.0, -1.1428571428571428), (0.0, -2.2857142857142856), (0.0, -1.7142857142857142), (1.1428571428571428, 1.977142857142857), (-1.1428571428571428, 1.977142857142857), (1.4285714285714286, 2.4714285714285715), (-1.4285714285714286, 2.4714285714285715), (0.0, -2.857142857142857)]

#Concentric Circular
#coordinates=[(0, 0), (3, 0), (2, 2), (0, 3), (-2, 2), (-3, 0), (-2, -2), (0, -3), (2, -2)]

#Circular concentric1
coordinates=[]
for theta in np.arange(0,2*np.pi,2*np.pi/9):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))
for theta in np.arange(0,2*np.pi,2*np.pi/7):
       coordinates.append((2*np.cos(theta),2*np.sin(theta)))
#Circular
'''coordinates=[(0,0)]
for theta in np.arange(0,2*np.pi,2*np.pi/17):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))'''

#semi-circle
#coordinates=[(0,0),(3*np.cos(4*np.pi/3),3*np.sin(4*np.pi/3)),(3*np.cos(-np.pi/3),3*np.sin(-np.pi/3))]
'''coordinates=[(0,0)]
for theta in np.arange(0,np.pi+np.pi/17,np.pi/17):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))'''

#set to store values of u,v
uvplane=set()

#creating plot for uv plane covergae
plt.figure(1)
ax=plt.axes([0.1,0.1,0.6,0.8],projection='3d')
axes2=plt.axes([0.75,0.05,0.18,0.4],xlim=(-3.5,3.5),ylim=(-3.5,3.5))
axes3=plt.axes([0.75,0.55,0.18,0.4])

for x,y in coordinates:
    #plotting location of individual antenaa
    axes2.plot(x,y,'rs',markersize=4)
    
    for x1,y1 in coordinates:
        #calculating u and v 
        u=(x1-x)
        v=(y1-y)


        # plotting u,v in u-v plane
        axes3.plot(u,v,"bs",markersize=2)
        
        u=1000*u
        v=1000*v
        uvplane.add((u,v))
axes2.grid()
axes3.grid()

# Creating plot of synthesised Beam

#defining function which returns value of exp(i2*pi(ux+vy)) over whole grid 
def z(u,v):
    l=np.arange(l_min,l_max,h)
    m=np.arange(m_min,m_max,h)
    X,Y=np.meshgrid(l,m)
    y=np.exp(2*np.pi*(complex(0,1))*(u*X+v*Y))
    return y

# setting limits of lm plane
l_min=-2*(10**-3)
l_max=2*(10**-3)
m_min=-2*(10**-3)
m_max=2*(10**-3)
#step size
h=10**-5
#setting limits of field of view
l=np.arange(l_min,l_max,h)
m=np.arange(m_min,m_max,h)
s=np.size(m)
# creatig image vector which will store information of synthesised beam
image=np.zeros((s,s))

# creating meshgrid
X,Y=np.meshgrid(l,m)

#calculating synthesised beam
for u,v in uvplane:
    image=image+z(u,v)

# plotting synthesised beam
power=(image.real)*(image.real)
surf=ax.contourf(X,Y,image.real,30,cmap='gnuplot')
ax.set_xlabel('l')
ax.set_ylabel('m')
ax.grid()
plt.sca(ax)
plt.colorbar(surf)
ax.set_title('Synthesised Beam')
axes2.set_title('Arrangement of Telescopic array')
axes3.set_title('uv plane')
axes3.xaxis.set_label('u')
axes3.yaxis.set_label('v')
plt.show()

# calculating THETAhpbw
P_l=power[200,:]
P_m=power[:,200]
c=0
ratio=1
while ratio>0.5 :
       ratio=P_l[200+c]/P_l[200]
       c=c+1
Theta_l=2*60*h*c*180/np.pi
c=0
ratio=1
while ratio>0.5 :
       ratio=P_m[200+c]/P_m[200]
       c=c+1
Theta_m=(2*60*h*c)*180/np.pi

print('dimension of theta hpbw are {}x{}'.format(Theta_l,Theta_m))
def plotj(i):
	plt.plot(l,power[i,:])
	plt.grid()
	plt.title(str(i))
	plt.show()

for j in np.arange(175,201,1):
	plotj(j)
def Slc(SL):
       SLL=10*np.log(SL/power[200,200])/np.log(10)
       print('SLL is {}'.format(SLL))
       return SLL
       

