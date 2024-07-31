balls = []

n = 31
v0 = 32       

floor = box(pos=vec(50,-2,0), size = vec(120, 0.1, 10), color=vec(0,1,0))

for i in range(n):
  balls[i] = sphere(radius=2, color= 2.0*vec.random())
  balls[i].pos = vec(0,0,0)
  balls[i].v = v0*vec(cos(radians(3*i)), sin(radians(3*i)), 0)
  balls[i].a = vec(0, -10, 0)
  attach_trail(balls[i])

scene.center = vec(50,20,0)
scene.waitfor('click')

t, dt = 0, 0.01      
while True:
    rate(1/dt)
    for i in range(n):   
      balls[i].v = balls[i].v + balls[i].a * dt
      balls[i].pos = balls[i].pos + balls[i].v * dt
      if balls[i].pos.y < floor.pos.y + balls[i].radius :
        balls[i].v = balls[i].a = vec(0,0,0)