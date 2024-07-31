G = 6.67e-11

Earth = sphere(pos = vec(0,-5000000,0), radius = 500000)
Earth.m = 10e24
Earth.v = vec(-3000,0,0)
attach_trail(Earth, type='points', pps=5)

Rocket = sphere(pos = vec(0,5000000,0), radius = 500000)
Rocket.m = 5e24
Rocket.v = vec(3000,0,0)
attach_trail(Rocket, type='points', pps=5)

t = 0
dt = 1

fk1 = gcurve(color=color.red, label="E_k1", dot = True)
fk2 = gcurve(color=color.magenta, label="E_k2", dot = True)
fp = gcurve(color=color.green, label="E_p", dot = True)
fmech = gcurve(color=color.blue, label="E_mech", dot = True)

scene.waitfor('click')
while True:
    rate(1000)
    
    r = Earth.pos - Rocket.pos
    Rocket.f = G*Earth.m*Rocket.m/mag(r)**2*norm(r)
    Earth.f= -Rocket.f
    
    Rocket.v = Rocket.v + Rocket.f/Rocket.m*dt
    Earth.v = Earth.v + Earth.f/Earth.m*dt
    Rocket.pos = Rocket.pos + Rocket.v*dt
    Earth.pos = Earth.pos + Earth.v*dt
                
    E_k1 = (1/2) * Earth.m * mag(Earth.v)**2
    E_k2 = (1/2) * Rocket.m * mag(Rocket.v)**2
    E_p = -G*Earth.m*Rocket.m/mag(r)
    E_mech = E_k1 + E_k2 + E_p

    fk1.plot(t,E_k1)
    fk2.plot(t,E_k2)
    fp.plot(t,E_p)
    fmech.plot(t,E_mech)

    if Earth.radius> mag(r):
        Rocket.v=vec(0,0,0)
        break

    t=t+dt
