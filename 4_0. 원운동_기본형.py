R1 = 1
T1 = 1
w1 = 2*pi/T1

ball1 = sphere(radius=0.1)
ball1.pos = R1 * vec(1,0,0)
attach_trail(ball1)

t, dt = 0, 0.001
scene.waitfor('click')
while True:
    rate(1/dt)
    ball1.pos = R1 * vec(cos(w1*t), sin(w1*t), 0)
    t = t +dt