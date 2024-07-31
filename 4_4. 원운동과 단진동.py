R = 5
x0 = 2*R

crate=sphere(radius=0.5, color=color.blue)
crate.m=1
crate.pos=vec(R,0,0)
crate.vel=vec(0,0,0)

spring=helix(pos=vec(-2*R,0,0), axis=crate.pos-vec(-2*R,0,0), coils = 20, thickness=0.1, radius=0.3, color = color.red)
spring.const=1

omega = (spring.const/crate.m)**(1/2)
t=0

ball = sphere(radius=0.5, color=color.magenta, make_trail=True)
ball.pos = R * vec(cos(omega*t), sin(omega*t), 0)
ball.vel = R * omega * vec(-sin(omega*t),cos(omega*t),0)
ball.acc = -R* omega**2 * vec(cos(omega*t), sin(omega*t), 0)

attach_arrow(ball,"vel", color=color.green, scale=0.1)
attach_arrow(ball,"acc", color=color.red, scale=0.1)


t = 0
dt = 0.001

scene.waitfor("click")
while True:
    rate(1/dt)
    ball.acc = -R* omega**2 * vec(cos(omega*t), sin(omega*t), 0)
    ball.vel = ball.vel + ball.acc*dt
    ball.pos = ball.pos + ball.vel*dt
    
    x = crate.pos - spring.pos
    f = -spring.const*(mag(x) - x0)*norm(x) 
    
    crate.vel=crate.vel+f/crate.m*dt
    crate.pos=crate.pos+crate.vel*dt
    
    spring.axis=crate.pos - spring.pos
    
    t = t +dt