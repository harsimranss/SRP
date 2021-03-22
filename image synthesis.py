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
'''coordinates=[]
for theta in np.arange(0,2*np.pi,2*np.pi/8):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))
for theta in np.arange(0,2*np.pi,2*np.pi/8):
       coordinates.append((2*np.cos(theta+np.pi/8),2*np.sin(theta+np.pi/8)))'''
#Circular
coordinates=[(0,0)]
for theta in np.arange(0,2*np.pi,2*np.pi/17):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))

#semi-circle
#coordinates=[(0,0),(3*np.cos(4*np.pi/3),3*np.sin(4*np.pi/3)),(3*np.cos(-np.pi/3),3*np.sin(-np.pi/3))]
'''coordinates=[(0,0)]
for theta in np.arange(0,np.pi+np.pi/17,np.pi/17):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))'''

# algorithm

#creating uv set
uvplane=set()

#setting the plot
plt.figure(1)
ax=plt.axes([0.1,0.1,0.6,0.8],projection='3d')
axes2=plt.axes([0.75,0.05,0.23,0.4],xlim=(-3.5,3.5),ylim=(-3.5,3.5))
axes3=plt.axes([0.75,0.55,0.23,0.4])

# calculating and plotting all values of uv 
for x,y in coordinates:
    axes2.plot(x,y,'rs',markersize=4)
    for x1,y1 in coordinates:
        u=x1-x
        v=y1-y
        
        uvplane.add((u,v))

        axes3.plot(u,v,"bs",markersize=2)
        u=1000*u
        v=1000*v
        uvplane.add((u,v))
axes2.grid()
axes3.grid()

# defining exp(i*2pi(ux+vy))
def z(u,v):
    l=np.arange(l_min,l_max,h)
    m=np.arange(m_min,m_max,h)
    X,Y=np.meshgrid(l,m)
    y=np.exp(2*np.pi*(complex(0,1))*(-u*X-v*Y))
    return y

# setting limits of lm plane
l_min=-2*(10**-3)
l_max=2*(10**-3)
m_min=-2*(10**-3)
m_max=2*(10**-3)
h=10**-5
def I(l,m):
     return (10**-17)*(np.exp(1000*(10**6)*(-(l-lo)**2-(m-mo)**2))+np.exp(-1000*(10**6)*(((l-l1)**2+(m-m1)**2)))+np.exp(-1000*(10**6)*(((l-l2)**2+(m-m2)**2))))
w={}
l=np.arange(l_min,l_max,h)
m=np.arange(m_min,m_max,h)
s=np.size(m)
image=np.zeros((s,s))
Synth_beam=np.zeros((s,s))
X,Y=np.meshgrid(l,m)
lo=0.4*(10**-3)
mo=0.2*(10**-3)
l1=-0.4*(10**-3)
m1=0.6*(10**-3)
l2=-0.7*(10**-3)
m2=0.5*(10**-3)
for u,v in uvplane:
    w[(u,v)]=(np.sum(np.sum(I(X,Y)*z(u,v),axis=0)))*h*h
    
for u,v in uvplane:
    image=image+z(-u,-v)*w[(u,v)]*100
    Synth_beam=Synth_beam+z(-u,-v)
    
surf=ax.contourf(X,Y,Synth_beam.real,30,cmap='gnuplot')
plt.sca(ax)
plt.colorbar(surf)
ax.set_title('Synthesised Beam')
axes2.set_title('Arrangement of Telescopic array')
axes3.set_title('uv plane')
axes3.xaxis.set_label('u')
axes3.yaxis.set_label('v')
plt.figure()
axes4=plt.axes([0.05,0.1,0.42,0.8],projection='3d')
axes5=plt.axes([0.55,0.1,0.42,0.8],projection='3d')
imag=axes4.contourf(X,Y,I(X,Y),30,cmap='gnuplot')
imag2=axes5.contourf(X,Y,image.real,30,cmap='gnuplot')
plt.sca(axes4)
plt.colorbar(imag)
plt.sca(axes5)
plt.colorbar(imag2)
plt.show()
