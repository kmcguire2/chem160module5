from math import sqrt
from drawtraj import drawtraj

def force(x,y,m,mstar):
    r2=x**2+y**2
    r32=r2*sqrt(r2)
    fx=-x*m*mstar/r32
    fy=-y*m*mstar/r32
    return fx,fy

def integrate(x,y,vx,vy,fx,fy,m,dt):
    ax, ay = fx/m, fy/m #x and y components of acceleration
    vx += ax * dt #x component of velocity
    vy += ay * dt #y component of velocity
    x += vx * dt #update x position
    y += vy * dt #update y position
    return x,y,vx,vy

# Main part of the program

mstar = 100
m = 1
nsteps = 5000000
dt = 0.01
r = 50
x, y = 0, r
vx, vy = 0.2, 0.4
trajx, trajy = [], []

for t in range(nsteps):
    fx, fy = force(x,y,m,mstar) #caluclate forces
    x,y,vx,vy = integrate(x,y,vx,vy,fx,fy,m,dt) #calculate new positions and velocities
    trajx.append(x) #put x-y position in list
    trajy.append(y)
    

drawtraj(trajx,trajy,12*r)
