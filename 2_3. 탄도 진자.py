g=9.8
L=1
k=150000

pivot=vec(0,1,0)
roof=box(pos=pivot,size=vec(1,0.1,1),color=color.green)
target=box(pos=pivot + vec(0,-L,0),size=vec(0.2,0.2,0.2),color=color.blue)
target.m = 5
target.v = vec(0,0,0)
rod=cylinder(pos=pivot,axis=target.pos-pivot,radius=0.01,color=color.red)

bullet=sphere(pos=vec(-1,0,0), size=vec(0.1,0.05,0.05))
bullet.m = 1
bullet.v = vec(10,0,0)

dt=0.001
scene.waitfor("click")
while True:
    rate(1/dt)
    bullet.pos = bullet.pos + bullet.v*dt
    if target.pos.x - bullet.pos.x < 0:
        target.v = bullet.m*bullet.v/(bullet.m + target.m)
        while True:
            rate(1/dt)
            bullet.pos = target.pos
            force = -k*(mag(rod.axis)-L)*norm(rod.axis)
            target.a = vec(0,-g,0) + force/target.m
            target.v += target.a * dt
            target.pos += target.v * dt
            rod.axis = target.pos-pivot