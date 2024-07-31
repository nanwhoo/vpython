g, v0 = 10, 30       
theta = pi/4

floor = box(pos=vec(50,-2,0), size = vec(120, 0.1, 10), color=vec(0,1,0))

ball = sphere(radius=2, color=vec(0,1,1))
ball.m = 2
ball.pos = vec(0,0,0)
ball.v = v0 * vec(cos(theta),sin(theta),0)
ball.a = vec(0,-10, 0)

attach_trail(ball, type='points', pps=1)
attach_arrow(ball, "a", shaftwidth=1, color=vec(1,0,0))
attach_arrow(ball, "v", shaftwidth=1, color=vec(0,0,1))

gV = graph(title="s-t plot", width=600, height=450)
gE = graph(title="E-t plot", width=600, height=450)
#gV = graph(title="v-t plot", width=600, height=450)

fx = gcurve(graph=gV, color=color.red, label="x", dot = True)
fy = gcurve(graph=gV, color=color.green, label="y", dot = True)

fk = gcurve(graph=gE, color=color.red, label="E_k", dot = True)
fp = gcurve(graph=gE, color=color.green, label="E_p", dot = True)
fmech = gcurve(graph=gE, color=color.blue, label="E_mech", dot = True)

scene.center = vec(50,20,0)
scene.waitfor('click')
t, dt = 0, 0.01
while True:
    rate(1/dt)
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt

    #fx.plot(t,ball.v.x)
    fx.plot(t,ball.pos.x)
    #fy.plot(t,ball.v.y)
    fy.plot(t,ball.pos.y)

    E_k = (1/2) * ball.m * mag2(ball.v)
    E_p = ball.m * g * ball.pos.y
    E_mech = E_k + E_p

    fk.plot(t,E_k)
    fp.plot(t,E_p)
    fmech.plot(t,E_mech)  
    
    t=t+dt
    
    if ball.pos.y < floor.pos.y + ball.radius:
        break