B0 = vector(0,0,0.2)

for x in range(-0.9, 0.9, 0.2):
    for y in range(-0.9, 0.9, 0.2):
        arrow(pos=vector(x,y,0),axis=B0,color=vector(0,1,1))
            
proton = sphere(radius=2e-2, m=1.7e-27, q= 1.6e-19, color=color.red, make_trail=True)
proton.pos = vec(-0.1,-0.1,0.2)
proton.vel = vec(0,5e6,0)
                  
scene.waitfor("click")
dt = 1e-10
while True:
    rate(1000)
    force = proton.q*cross(proton.vel,B0)
    proton.vel = proton.vel + force/proton.m*dt
    proton.pos = proton.pos + proton.vel*dt