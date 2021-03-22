import numpy as np
import matplotlib.pyplot as plt
#square
#coordinates=[(0,0),(1*0.25,0),(1*0.25,1*0.25),(1*0.25,-1*0.25),(0,1*0.25),(-1*0.25,1*0.25),(-1*0.25,0),(-1*0.25,-1*0.25),(0,-0.25),(0.5,0),(0.5,0.5),(0.5,-0.5),(0,0.5),(-0.5,0.5),(-0.5,0),(-0.5,0.5),(0,-0.5),(-0.5,-0.5)]
#Y configuration
coordinates=[(0, 1), (0.69802, 1.403), (1.60362, 1.92585), (2.60862, 2.50609), (3.68415, 3.12705), (4.81537, 3.78016), (5.99304, 4.46008), (-0.69802, 1.403), (-1.60362, 1.92585), (-2.60862, 2.50609), (-3.68415, 3.12705), (-4.81537, 3.78016), (-5.99304, 4.46008), (-0.0, 0.194), (-0.0, -0.8517), (-0.0, -2.01218), (-0.0, -3.25409), (-0.0, -4.56031), (-0.0, -5.92017)]

#Concentric Circular
#coordinates=[(0, 0), (3, 0), (2, 2), (0, 3), (-2, 2), (-3, 0), (-2, -2), (0, -3), (2, -2), (1.8477590650225735, 0.7653668647301796), (0.7653668647301797, 1.8477590650225735), (-0.7653668647301795, 1.8477590650225735), (-1.8477590650225735, 0.7653668647301798), (-1.8477590650225737, -0.7653668647301793), (-0.7653668647301807, -1.847759065022573), (0.76536686473018, -1.8477590650225733), (1.847759065022573, -0.7653668647301808), (1.8477590650225735, 0.7653668647301799)]

#Circular concentric1
#coordinates=[(0, 0), (3, 0), (2, 2), (0, 3), (-2, 2), (-3, 0), (-2, -2), (0, -3), (2, -2)]
#Circular
'''coordinates=[(0,0)]
for theta in np.arange(0,np.pi*2,np.pi/8):
       coordinates.append((1*np.cos(theta),1*np.sin(theta)))'''
#semi-circle
'''coordinates=[(0,0)]
for theta in np.arange(0,np.pi*2,np.pi/8):
       coordinates.append((3*np.cos(theta),3*np.sin(theta)))'''
for y1,x1 in coordinates:
    for y2,x2 in coordinates:
        y=y1-y2
        x=x1-x2
        h=np.pi/8
        uplane=[]
        vplane=[]
        delta=np.pi/4
        theta=np.pi/6
        for phi in np.arange(-np.pi/4,np.pi/4+h,h):
            v=x*(np.cos(theta)*np.cos(phi)*np.sin(delta)+np.cos(delta)*np.sin(theta))+y*np.sin(phi)*np.sin(delta)
            u=-x*np.cos(theta)*np.sin(phi)+y*np.cos(phi)
            uplane.append(u)
            vplane.append(v)
        plt.plot(uplane,vplane,'bs-',markersize=0.2,linewidth=0.1)
plt.show()
