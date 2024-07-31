G = 6.67e-11

Earth = sphere(pos = vec(0,0,0), radius = 6400000, texture = textures.earth)
Earth.m = 5.972e24
Earth.v = vec(0,0,0)

Rocket = sphere(pos = vec(0,6400000+500000,0), radius = 500000)
Rocket.m = 5e7
Rocket.v = vec(6000,0,0)
attach_trail(Rocket)

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
        
    if Earth.radius> mag(r):
        Rocket.v=vec(0,0,0)
        break