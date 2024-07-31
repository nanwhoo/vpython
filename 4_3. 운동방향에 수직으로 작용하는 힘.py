m, v, f = 1, 5, 10

ball = sphere(radius=0.1)
ball.pos = vec(0,0,0)
ball.v = vec(0,v,0)
ball.f = vec(-f,0,0)
attach_trail(ball)

attach_arrow(ball,'v', color=color.green, shaftwidth = 0.05, scale=0.2)
attach_arrow(ball,'f', color=color.red, shaftwidth = 0.05, scale=0.1)

t, dt = 0, 0.0001
scene.waitfor('click')
while True:
    rate(1/dt)
    ball.f = f*norm(cross(vec(0,0,1), ball.v))
    ball.a = ball.f/m
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt
    t = t +dt
