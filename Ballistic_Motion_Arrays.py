import math as ma
import numpy as np
import matplotlib.pyplot as plt

g=raw_input('G Constant: ')     #This will be changed to a negative value regardless of sign here...
v0m=raw_input('Initial Velocity Magnitude (m/s): ')
v0a=raw_input('Initial Velocity Angle (degrees): ')
h0=raw_input('Initial Height (m): ')
ts=raw_input('Time Step (s): ')

g=float(g)
v0m=float(v0m)
v0a=float(v0a)
h0=float(h0)
ts=float(ts)

if g > 0:
    g=(-1)*g
else: g=g

v0a=ma.radians(v0a)

v0x=v0m*ma.cos(v0a)
v0y=v0m*ma.sin(v0a)
vy=v0y

c=1
l=[1]
tmp=h0
while tmp >= 0:
    tmp=h0+(v0y*c*ts)+(0.5*g*((c*ts)**2))
    c=c+1
    l.append(c)

t=np.zeros([1,c])
pxy=np.zeros([2,c])

for x in l:
    t.itemset((x-1),(x-1)*ts)
    pxy.itemset((0,x-1),v0x*t.item(x-1))
    pxy.itemset((1,x-1),(h0+(v0y*t.item(x-1))+(0.5*g*(t.item(x-1)**2))))

px=pxy[0,]
py=pxy[1,]
hi=np.amax(py)

c=0
a=None
while a != hi:
    a=py[c]
    c=c+1
hix=px[c-1]

print ''
print 'Total Flight Time:', np.amax(t), 'Seconds'
print ''
print 'Highest Point: (', hix, ',', hi, ')'
print ''
print 'Distance to Ground Every',ts, 'Seconds:'
print py

plt.plot(px,py)
plt.show()
