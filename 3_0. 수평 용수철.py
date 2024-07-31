x0=10

wall_left=box(pos=vec(-x0,0,0), size= vec(0.2, 5, 5), color = color.green)
wall_right=box(pos=vec(x0,0,0), size= vec(0.2, 5, 5), color = color.green)

ball=sphere(pos=vec(3,0,0),vel=vec(3,0,0), radius=2.5, mass=1, color=color.blue)

spring_left = helix(constant = 1, pos=wall_left.pos, axis=ball.pos - wall_left.pos, coils = 10, thickness=0.2, radius=1, color=color.red)
spring_right = helix(constant = 1, pos=wall_right.pos, axis=ball.pos - wall_right.pos, coils = 10, thickness=0.2, radius=1, color=color.red)

def acc():
    r_left = ball.pos - wall_left.pos
    force_left = -spring_left.constant*(mag(r_left) - x0)*norm(r_left)
    r_right = ball.pos - wall_right.pos
    force_right = -spring_right.constant*(mag(r_right) - x0)*norm(r_right)
    return (force_right+force_left)/ball.mass

t, dt=0, 0.01
scene.waitfor("click")
while True:
    rate(100)
    ball.vel=ball.vel+acc()*dt
    ball.pos=ball.pos+ball.vel*dt
    
    spring_right.axis=ball.pos - wall_right.pos
    spring_left.axis=ball.pos - wall_left.pos
    
    ball.acc=acc()
    attach_arrow(ball,"vel", shaftwidth=0.5, color=color.green)
    attach_arrow(ball,"acc", shaftwidth=0.5, color=color.cyan)
    
    t=t+dt
