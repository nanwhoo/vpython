G = 6.67e-11

Earth = sphere(pos = vec(0,0,0), radius = 6400000, texture = textures.earth)
Earth.m = 5.972e24
Earth.v = vec(0,0,0)

Rocket = sphere(pos = vec(0,6400000+500000,0), radius = 500000)
Rocket.m = 5e7
Rocket.v = vec(10000,0,0)
attach_trail(Rocket)

fk1 = gcurve(color=color.red, label="E_k1", dot = True)
fk2 = gcurve(color=color.magenta, label="E_k2", dot = True)
fp = gcurve(color=color.green, label="E_p", dot = True)
fmech = gcurve(color=color.blue, label="E_mech", dot = True)

scene.waitfor('click')

t, dt = 0, 1
while True:
    rate(1000)
    
    r = Earth.pos - Rocket.pos
    Rocket.f = G*Earth.m*Rocket.m/mag2(r)*norm(r)
    Earth.f= -Rocket.f
    
    Rocket.v = Rocket.v + Rocket.f/Rocket.m*dt
    Earth.v = Earth.v + Earth.f/Earth.m*dt
    Rocket.pos = Rocket.pos + Rocket.v*dt
    Earth.pos = Earth.pos + Earth.v*dt

    E_k1 = (1/2) * Earth.m * mag2(Earth.v)
    E_k2 = (1/2) * Rocket.m * mag2(Rocket.v)
    E_p = -G*Earth.m*Rocket.m/mag(r)
    E_mech = E_k1 + E_k2 + E_p

    fk1.plot(t,E_k1)
    fk2.plot(t,E_k2)
    fp.plot(t,E_p)
    fmech.plot(t,E_mech)

    t = t + dt
       
    if Earth.radius> mag(r):
        Rocket.v=vec(0,0,0)
        break