g = 10

basket = sphere(color=color.orange, m=5, radius=0.2)
tennis = sphere(color=color.green, m=0.05, radius=0.05)

basket.pos.y = 0.3
tennis.pos.y = basket.pos.y+(basket.radius+tennis.radius)

tennis.vel = vec(0,0,0)
basket.vel = vec(0,0,0)

floor = box(pos=vec(0,-0.5,0), size=vec(1,0.05,1),color=vec(1,0.4,0.4))

dt = 0.01

scene.waitfor("click")
while True:
    rate(1/dt)

    basket.acc = vec(0,-g,0)    
    basket.vel = basket.vel + basket.acc*dt
    basket.pos = basket.pos + basket.vel*dt

    tennis.acc = vec(0,-g,0)    
    tennis.vel = tennis.vel + tennis.acc*dt
    tennis.pos = tennis.pos + tennis.vel*dt
    
    
    if (basket.pos.y < floor.pos.y + basket.radius and basket.vel.y < 0):
        basket.vel *= -1
        
    if (mag(basket.pos-tennis.pos)<basket.radius+tennis.radius and dot(basket.pos-tennis.pos,basket.vel-tennis.vel)<0):
        tennis.vel = 2*basket.m/(tennis.m+basket.m)*basket.vel - (basket.m-tennis.m)/(tennis.m+basket.m)*tennis.vel
        basket.vel = 2*tennis.m/(tennis.m+basket.m)*tennis.vel + (basket.m-tennis.m)/(tennis.m+basket.m)*basket.vel
