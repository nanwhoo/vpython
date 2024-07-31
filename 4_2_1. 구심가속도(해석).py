R = 5
omega = pi
t=0

ball = sphere(radius=0.3, color=color.magenta, make_trail=True)
ball.pos = R * vec(cos(omega*t), sin(omega*t), 0)
ball.v = R * omega * vec(-sin(omega*t),cos(omega*t),0)
ball.a = -R* omega**2 * vec(cos(omega*t), sin(omega*t), 0)

rod = arrow(pos=vec(0,0,0), axis=ball.pos, shaftwidth=0.1, color=color.red)
attach_arrow(ball,"v", color=color.green, shaftwidth=0.1, scale=0.05)
attach_arrow(ball,"a", color=color.blue, shaftwidth=0.1, scale=0.05)

dt = 0.001

scene.waitfor("click")
while True:
    rate(1/dt)
    ball.a = -R* omega**2 * vec(cos(omega*t), sin(omega*t), 0)
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt
    rod.axis=ball.pos
    t = t + dt