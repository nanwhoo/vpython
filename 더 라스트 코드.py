scene = canvas(background=color.white)

R = 5
omega1 = pi
omega2 = 2*pi
t=0

ball1 = sphere(radius=0.3, color=color.magenta)
ball1.pos = R * vec(1, 0, 0)

ball2 = sphere(radius=0.3, color=color.magenta, make_trail=True)
ball2.pos = ball1.pos + R/2 * vec(1, 0, 0)

rod1 = arrow(pos=vec(0,0,0), axis=ball1.pos, shaftwidth=0.1, color=color.red)
rod2 = arrow(pos=ball1.pos, axis=ball2.pos - ball1.pos, shaftwidth=0.1, color=color.red)

dt = 0.001

scene.waitfor("click")
while True:
    rate(1/dt)
    ball1.pos = R * vec(cos(omega1*t), sin(omega1*t), 0)    
    ball2.pos = ball1.pos + R/2 * vec(cos(omega2*t), sin(omega2*t), 0)
    
    rod1.axis=ball1.pos
    rod2.pos=ball1.pos
    rod2.axis=ball2.pos - ball1.pos
    
    t = t + dt