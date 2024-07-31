g, x0 = 9.8, 1

roof=box(pos=vec(0,x0,0), size= vec(1, 0.1, 0.5), color = color.green)

ball=sphere(radius=0.2, color=color.blue, pos=vec(0,0,0), v=vec(0,0,0), m = 1)
spring=helix(pos=roof.pos, axis=ball.pos-roof.pos, coils = 10, thickness=0.02, radius=0.1, color = color.red)
spring.const=100

t, dt = 0, 0.001
scene.waitfor("click")

while True:
    rate(1/dt)

    x = ball.pos - roof.pos
    f_e = vec(0,-ball.m*g, 0)
    f_s = -spring.const*(mag(x) - x0)*norm(x)
    f = f_e + f_s
    ball.a = f/ball.m

    ball.v=ball.v+ball.a*dt
    ball.pos=ball.pos+ball.v*dt
    spring.axis=ball.pos - roof.pos
    
    t=t+dt