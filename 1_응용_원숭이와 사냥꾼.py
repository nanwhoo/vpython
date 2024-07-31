g, v0, f = 10, 30, 0.2       
floor = box(pos=vector(50,-2,0), size = vector(120,0.1,10), color=vec(0,1,0))

target = sphere(radius=2, color = color.cyan)
target.pos = vec(100,50,0)
target.v = vec(0, 0, 0)
target.a = vec(0, -g, 0)
attach_trail(target, type='points', pps=5)
attach_arrow(target, "v", shaftwidth=1, color=vec(0,0,1))

bullet = sphere(radius=2, color = color.cyan)
bullet.pos = vec(0,0,0)
bullet.v = f*vec(target.pos.x-bullet.pos.x, target.pos.y-bullet.pos.y, 0)
bullet.a = vec(0, -g, 0)
attach_trail(bullet, type='points', pps=5)
attach_arrow(bullet, "v", shaftwidth=1, color=vec(0,0,1))

scene.center = vec(50, 20, 0)
scene.waitfor('click')
t, dt = 0, 0.01      
while True:
    rate(100)

    target.v = target.v + target.a * dt
    target.pos = target.pos + target.v * dt
    
    bullet.v = bullet.v + bullet.a * dt
    bullet.pos = bullet.pos + bullet.v * dt

    if mag(target.pos-bullet.pos)< target.radius + bullet.radius :
       break