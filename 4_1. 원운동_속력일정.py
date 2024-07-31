R1 = 1
T1 = 1
w1 = 2*pi/T1
ball1 = sphere(radius=0.1)
ball1.pos = R1 * vec(1,0,0)
attach_trail(ball1)

R2 = 2
T2 = 2
w2 = 2*pi/T2
ball2 = sphere(radius=0.1)
ball2.pos = R2 * vec(1,0,0)
attach_trail(ball2)

t, dt = 0, 0.001
scene.waitfor('click')
while True:
    rate(1/dt)
    ball1.pos = R1 * vec(cos(w1*t), sin(w1*t), 0)
    ball2.pos = R2 * vec(cos(w2*t), sin(w2*t), 0) 
    t = t +dt
