x0=10

wall_left=box(pos=vec(-15,0,0), size= vec(0.2, 5, 5), color = color.green)
wall_right=box(pos=vec(15,0,0), size= vec(0.2, 5, 5), color = color.green)
bob1=box(pos=vec(-5,0,0), vel=vec(5,0,0), size=vec(2.5,2.5,2.5), mass=1, color=color.blue)
bob2=box(pos=vec(5,0,0), vel=vec(0,0,0), size=vec(2.5,2.5,2.5), mass=1, color=color.blue)

spring_left=helix(constant = 1, pos=wall_left.pos, axis=bob1.pos-wall_left.pos, coils = 10, thickness=0.2, radius=1, color=color.red)
spring_center=helix(constant = 1, pos=bob1.pos, axis=bob2.pos-bob1.pos, coils = 10, thickness=0.2, radius=1, color=color.red)
spring_right=helix(constant = 1, pos=bob2.pos, axis=wall_right.pos-bob2.pos, coils = 10, thickness=0.2, radius=1, color=color.red)

def acc1():
	r_left = bob1.pos - wall_left.pos
	force_left = -spring_left.constant*(mag(r_left) - x0)*norm(r_left)
	r_center = bob2.pos - bob1.pos
	force_center = -spring_right.constant*(mag(r_center) - x0)*norm(r_center)
	return (force_left-force_center)/bob1.mass
def acc2():
	r_center = bob2.pos - bob1.pos
	force_center = -spring_right.constant*(mag(r_center) - x0)*norm(r_center)
	r_right = wall_right.pos-bob2.pos
	force_right = -spring_right.constant*(mag(r_right) - x0)*norm(r_right)
	return (force_center-force_right)/bob2.mass

t, dt = 0, 0.01
scene.waitfor("click")
while True:
	rate(1/dt)
	bob1.vel=bob1.vel+acc1()*dt
	bob1.pos=bob1.pos+bob1.vel*dt
	bob2.vel=bob2.vel+acc2()*dt
	bob2.pos=bob2.pos+bob2.vel*dt   
	spring_center.pos=bob1.pos
	spring_right.pos=bob2.pos
	spring_left.axis=bob1.pos - wall_left.pos
	spring_center.axis=bob2.pos - bob1.pos
	spring_right.axis=wall_right.pos - bob2.pos
	t=t+dt
