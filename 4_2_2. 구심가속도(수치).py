scene = canvas(background=color.white)

R = 5
omega = pi
t=0

ball = sphere(radius=0.3, color=color.magenta, make_trail=True)
ball.pos = R * vec(cos(omega*t), sin(omega*t), 0)

rod = arrow(pos=vec(0,0,0), axis=ball.pos, shaftwidth=0.1, color=color.red)
attach_arrow(ball,"v", color=color.green, shaftwidth=0.1, scale=0.05)
attach_arrow(ball,"a", color=color.blue, shaftwidth=0.1, scale=0.05)

dt = 0.001

scene.waitfor("click")
while True:
    rate(1/dt)
    ball.pos = R * vec(cos(omega*t), sin(omega*t), 0)
    ball.pos_prime = R * vec(cos(omega*(t+dt)), sin(omega*(t+dt)), 0)
    ball.v = (ball.pos_prime - ball.pos)/dt
    t = t + dt
    ball.pos_pprime = R * vec(cos(omega*(t+dt)), sin(omega*(t+dt)), 0)
    ball.v_prime = (ball.pos_pprime - ball.pos_prime)/dt
    ball.a = (ball.v_prime - ball.v)/dt
        
    rod.axis=ball.pos