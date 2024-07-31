G = 6.67430e-11  

body1 = sphere(pos=vec(-1, 0, 0), radius=0.1, color=color.red, make_trail=True)
body2 = sphere(pos=vec(1, 0, 0), radius=0.1, color=color.blue, make_trail=True)
body3 = sphere(pos=vec(0, 1.732, 0), radius=0.1, color=color.green, make_trail=True)

body1.mass = 1e30
body2.mass = 1e30
body3.mass = 1e30

body1.vel = vec(0, 50, 0)
body2.vel = vec(0, -50, 0)
body3.vel = vec(-100, 0, 0)

bodies = [body1, body2, body3]

scene.waitfor("click")

dt = 0.01 
while True:
    rate(1/dt) 
    for i, body in enumerate(bodies):
        force = vec(0, 0, 0)
        for other in bodies[:i] + bodies[i+1:]:
            r = other.pos - body.pos
            force += (G * body.mass * other.mass / mag(r)**3) * r
        
        body.vel += force / body.mass * dt
        body.pos += body.vel * dt