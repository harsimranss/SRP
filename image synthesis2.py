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
coordinates=[(0,0)]
for theta in np.arange(0,2*np.pi,2*np.pi/8):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))
for theta in np.arange(0,2*np.pi,2*np.pi/8):
       coordinates.append((1*np.cos(theta+np.pi/8),1*np.sin(theta+np.pi/8)))
#Circular
'''coordinates=[(0,0)]
for theta in np.arange(0,2*np.pi,2*np.pi/17):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))'''

#semi-circle
#coordinates=[(0,0),(3*np.cos(4*np.pi/3),3*np.sin(4*np.pi/3)),(3*np.cos(-np.pi/3),3*np.sin(-np.pi/3))]
'''coordinates=[(0,0)]
for theta in np.arange(0,np.pi+np.pi/17,np.pi/17):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))'''

uvplane=[]
plt.figure(1)
ax=plt.axes([0.1,0.1,0.6,0.8],projection='3d')
axes2=plt.axes([0.75,0.05,0.23,0.4])
axes3=plt.axes([0.75,0.55,0.23,0.4])
for y1,x1 in coordinates:
       
       axes2.plot(y1,x1,'rs',markersize=2)
       for y2,x2 in coordinates:
              y=(y1-y2)
              x=(x1-x2)
              h=np.pi/8
              uplane=[]
              vplane=[]
              delta=np.pi/9
              theta=np.pi/6
              for phi in np.arange(-np.pi/4,np.pi/4+h,h):
                     
                   v=x*(np.cos(theta)*np.cos(phi)*np.sin(delta)+np.cos(delta)*np.sin(theta))+y*np.sin(phi)*np.sin(delta)
                   u=-x*np.cos(theta)*np.sin(phi)+y*np.cos(phi)

                   uplane.append(u)
                   vplane.append(v)
                   u=1000*u
                   v=1000*v
                   uvplane.append((u,v))
              axes3.plot(uplane,vplane,"bs-",markersize=0.1,linewidth=0.2)

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

#defining actual brightness distribution
def I(l,m):
     return (10**-17)*(np.exp(10*(10**6)*(-(l-lo)**2-(m-mo)**2))+np.exp(-10*(10**6)*(((l-l1)**2+(m-m1)**2)))+np.exp(-10*(10**6)*(((l-l2)**2+(m-m2)**2))))

w={}
l=np.arange(l_min,l_max,h)
m=np.arange(m_min,m_max,h)
s=np.size(m)
image=np.zeros((s,s))
Sbeam=np.zeros((s,s))
X,Y=np.meshgrid(l,m)
lo=0.4*(10**-3)
mo=0.2*(10**-3)
l1=-0.4*(10**-3)
m1=0.6*(10**-3)
l2=-0.7*(10**-3)
m2=0.5*(10**-3)
#weight
weight={}
for u,v in uvplane:
    c=0
    for u1,v1 in uvplane:
        if ((u-u1)**2+(v-v1)**2)<100:
            c=c+1
        weight[(u,v)]=c
            
for u,v in uvplane:
    w[(u,v)]=(np.sum(np.sum(I(X,Y)*z(u,v),axis=0)))*h*h
    

for u,v in uvplane:
    image=image+(z(-u,-v)*(w[(u,v)]/weight[(u,v)]))
    Sbeam=Sbeam+(z(u,v)*(1))

surf=ax.contourf(X,Y,Sbeam.real,30,cmap='gnuplot')
plt.sca(ax)
plt.colorbar(surf)
ax.set_title('Synthesised Beam')
axes2.set_title('Arrangement of Telescopic array')
axes3.set_title('uv plane')
axes3.xaxis.set_label('u')
axes3.yaxis.set_label('v')
plt.figure(2)
axesf=plt.axes([0.05,0.1,0.45,0.8],projection='3d')
axesf2=plt.axes([0.55,0.1,0.45,0.8],projection='3d')
axesf.set_title('actual Distribution')
axesf2.set_title('synthesised image')
plot1=axesf.contourf(X,Y,I(X,Y),30,cmap='gnuplot')
plt.sca(axesf)
plt.colorbar(plot1)
plot2=axesf2.contourf(X,Y,image.real,30,cmap='gnuplot')
plt.sca(axesf2)
plt.colorbar(plot2)
plt.show()
power=(Sbeam.real)**2
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
       plt.get_current_fig_manager().window.state('zoomed')
       plotj(j)
def Slc(SL):
       SLL=10*np.log(SL/power[200,200])/np.log(10)
       print('SLL is {}'.format(SLL))
       return SLL
