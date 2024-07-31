scene = canvas(width=400, height=500, center=vector(0,0,0), background=color.white) 

gd = graph(width=600, height=150,background=color.white)
f1 = gcurve( color=color.red, label="E_k", dot = True)
f2 = gcurve( color=color.green, label="E_p,e", dot = True)
f3 = gcurve( color=color.blue, label="E_p,g", dot = True)
f4 = gcurve( color=color.black, label="E_mech", dot = True)


g = 9.8
x0 = 1

ball=sphere(radius=0.2, color=color.blue)
ball.m=1
ball.pos=vec(0.2,0,0)
ball.vel=vec(0,0,0)

wall=box(pos=vector(0,x0,0), size= vector(1, 0.1, 0.5), color = color.green)

spring=helix(pos=wall.pos, axis=ball.pos-wall.pos, coils = 10, thickness=0.02, radius=0.1, color = color.red)
spring.const=100

def acc():  
    x = ball.pos - wall.pos
    force_earth = vec(0,-ball.m*g, 0)
    force_spring = -spring.const*(mag(x) - x0)*norm(x) 
    force = force_earth + force_spring
    return force/ball.m

t=0
dt=0.01

scene.waitfor("click")
while True:
    rate(1/dt)
    ball.vel=ball.vel+acc()*dt
    ball.pos=ball.pos+ball.vel*dt
    spring.axis=ball.pos - wall.pos
    
    E_k = (1/2)*ball.m*mag(ball.vel)**2
    E_pg = ball.m*g*ball.pos.y
    E_ps = (1/2)*spring.const*(mag(ball.pos-wall.pos)-x0)**2
    E_mech = E_k + E_pg + E_ps
           
    f1.plot(t,E_k)
    f2.plot(t,E_pg)
    f3.plot(t,E_ps)
    f4.plot(t,E_mech)

    t=t+dt
