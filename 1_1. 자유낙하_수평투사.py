floor = box(pos=vec(50,-2,0), size = vec(120, 0.1, 10), color=vec(0,1,0))

ball1 = sphere(radius=2, color=vec(0,1,1))
ball1.pos = vec(0,45,0)
ball1.v = vec(0,0,0)
ball1.a = vec(0,-10, 0)

ball2 = sphere(radius=2, color=vec(0,1,1))
ball2.pos = vec(0,45,0)
ball2.v = vec(30,0,0)
ball2.a = vec(0,-10, 0)

scene.center = vec(50,20,0)
scene.waitfor('click')

t, dt = 0, 0.01
while True:
    rate(1/dt)
    
    ball1.v = ball1.v + ball1.a*dt
    ball1.pos = ball1.pos + ball1.v*dt

    ball2.v = ball2.v + ball2.a*dt
    ball2.pos = ball2.pos + ball2.v*dt
               
    t = t + dt

    if ball1.pos.y < floor.pos.y + ball1.radius & ball2.pos.y < floor.pos.y + ball2.radius :
        break
