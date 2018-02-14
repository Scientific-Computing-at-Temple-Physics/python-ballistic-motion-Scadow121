import math as ma
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

t=[0.]
px=[0.]
py=[h0]
vx=[v0x]
vy=[v0y]

c=1
t.append(ts*c)
px.append(v0x*t[c])
py.append(h0+(v0y*t[c])+(0.5*g*(t[c]**2)))
vx.append(v0x)
vy.append(v0y+(g*t[c]))

#print py

while py [c] >= 0:
    t.append((c+1)*ts)
    px.append(v0x*t[c+1])
    py.append(h0+(v0y*t[c+1])+(0.5*g*(t[c+1]**2)))
    vx.append(v0x)
    vy.append(v0y+(g*t[c+1]))
    c=c+1

f=len(t)
#print t
print ''
print 'Total Flight Time:', t [f-1], 'Seconds'
print ''
hi=py.index(max(py))
print 'Highest Point: (', px [hi], ',', max(py), ')'
print ''
print 'Distance to Ground Every',ts, 'Seconds:', py

plt.plot(px,py)
plt.show()
