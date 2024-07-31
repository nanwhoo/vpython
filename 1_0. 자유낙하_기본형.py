floor = box(pos=vec(50,-2,0), size = vec(120, 0.1, 10), color=vec(0,1,0))

ball1 = sphere(radius=2, color=vec(0,1,1))
ball1.pos = vec(0,45,0)
ball1.vel = vec(0,0,0)
ball1.acc = vec(0,-10, 0)

scene.center = vec(50,20,0)
scene.waitfor('click')

t, dt = 0, 0.01
while True:
    rate(1/dt)
    
    ball1.vel = ball1.vel + ball1.acc*dt
    ball1.pos = ball1.pos + ball1.vel*dt
               
    t = t + dt