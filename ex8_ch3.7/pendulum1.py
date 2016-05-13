import math
import matplotlib.pyplot as plt  
from matplotlib import animation      
g=9.8 
#calculate the trajectory
def DampedDriven(omega0,theta0,q,FD,omegaD,l,T):#q is related to damping force, while FD and omegaD is related to the driving force. the length of the rod is l.T is the interest time.
    dt=0.001
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while t<= T:
        omega = omega+(-g*theta/l-q*omega+FD* math.sin(omegaD*t))*dt
        theta = theta+omega*dt
        t = t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion
#Fig.1.damped pendulum without driving force
d=DampedDriven(0,0.2,1,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=1')
d=DampedDriven(0,0.2,3,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=3')
d=DampedDriven(0,0.2,9.8**0.5*2,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q='+r'$2\sqrt{g/l}$')
d=DampedDriven(0,0.2,10,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=10')
d=DampedDriven(0,0.2,30,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=30')
plt.xlim(0,10)
plt.grid(True,color='k')
plt.title('Fig.1 Damped Pendulum')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()

#Fig.2 damped driven pendulum, also known as linear forced pendulum
d=DampedDriven(0,0.2,1,0.2,2.0,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0)

plt.title('Fig.2 Damped Driven Pendulum')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()








