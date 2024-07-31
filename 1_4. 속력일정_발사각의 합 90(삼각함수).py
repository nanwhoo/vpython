floor = box(pos=vec(50,-2,0), size = vec(120, 0.1, 10), color=vec(0,1,0))

v0 = 32
theta1 = 30
theta2 = 90 - theta1

theta1 = theta1 * pi/180
theta2 = theta2 * pi/180

ball1 = sphere(radius=2, color=vec(0,1,1))
ball1.pos = vec(0,0,0)
ball1.v = v0*vec(cos(theta1), sin(theta1),0)
ball1.a = vec(0,-10, 0)

ball2 = sphere(radius=2, color=vec(0,1,1))
ball2.pos = vec(0,0,0)
ball2.v = v0*vec(cos(theta2), sin(theta2),0)
ball2.a = vec(0,-10, 0)

scene.center = vec(50,20,0)
scene.waitfor('click')

t, dt = 0, 0.01
while True:
    rate(1/dt)
    
    ball1.v = ball1.v + ball1.a*dt
    ball1.pos = ball1.pos + ball1.v*dt
    if ball1.pos.y < floor.pos.y + ball1.radius :
        ball1.v = ball1.a = vec(0,0,0)

    ball2.v = ball2.v + ball2.a*dt
    ball2.pos = ball2.pos + ball2.v*dt
    if ball2.pos.y < floor.pos.y + ball2.radius :
        ball2.v = ball2.a = vec(0,0,0)
               
    t = t + dt