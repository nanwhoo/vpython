gd1 = graph(width=600, height=150,background=color.white, ymin=0, ymax=1.0e11)
gd2 = graph(width=600, height=150,background=color.white)

G = 6.67e-11

star1 = sphere(pos = vec(0,-5000000,0), radius = 5e5)
star1.m = 10e24
star1.v = vec(-3000,0,0)
attach_trail(star1, type='points', pps=5)

star2 = sphere(pos = vec(0,5000000,0), radius = 5e5)
star2.m = 5e24
star2.v = vec(3000,0,0)
attach_trail(star2, type='points', pps=5)

cm = sphere(radius = 5e5, color=color.green, pos = (star1.m*star1.pos + star2.m*star2.pos)/(star1.m + star2.m)) 
attach_trail(cm, color=color.green, type='points', pps=1)

t = 0
dt = 1

f1 = gcurve(graph=gd1, color=color.red, label="L", dot = True)
f2 = gcurve(graph=gd2, color=color.red, label="cm_x", dot = True)
f3 = gcurve(graph=gd2, color=color.red, label="cm_y", dot = True)

scene.waitfor('click')
while True:
    rate(1000)
    
    r = star2.pos - star1.pos
    star1.f = G*star1.m*star2.m/mag(r)**2*norm(r)
    star2.f= -star1.f
    
    star1.v = star1.v + star1.f/star1.m*dt
    star2.v = star2.v + star2.f/star2.m*dt
    star1.pos = star1.pos + star1.v*dt
    star2.pos = star2.pos + star2.v*dt
    
    cm.pos = (star1.m*star1.pos + star2.m*star2.pos)/(star1.m + star2.m)
           
    f1.plot(t,mag(r.cross(star1.v-star2.v)))
    f2.plot(t,cm.pos.x)
    f3.plot(t,cm.pos.y)

    t=t+dt
