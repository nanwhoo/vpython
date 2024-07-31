scene = canvas(width=500, height=500, center=vec(0,0.1,0), background=color.white)

g=9.8
L1=1
L2=1

theta1=10
theta1=theta1*pi/180
omega1=0

theta2=0
theta2=theta2*pi/180
omega2=0

#case1. theta1=10, theta2=10
#case2. theta1=10, theta2=-10
#case3. theta1=10, theta2=0. 두 진자 사이의 에너지 교환

ceiling=box(pos=vec(0,1,0), size=vec(2,0.01,2),color=vec(0,1,0))

pivot1=vec(-0.5,1,0)
bob1=sphere(pos=pivot1 + vec(L1*sin(theta1),-L1*cos(theta1),0),radius=0.1,color=color.blue)
bob1.m=1

pivot2=vec(0.5,1,0)
bob2=sphere(pos=pivot2 + vec(L2*sin(theta2),-L2*cos(theta2),0),radius=0.1,color=color.blue)
bob2.m=1

rod1=cylinder(pos=pivot1,axis=bob1.pos-pivot1,radius=0.01,color=color.red)
rod2=cylinder(pos=pivot2,axis=bob2.pos-pivot2,radius=0.01,color=color.red)

spring=helix(pos=bob1.pos,axis=bob2.pos-bob1.pos,coils=10,thickness=0.02,radius=0.05,color=color.red)
spring.const=2
spring.l=1


dt=0.001

scene.waitfor("click")
while True:
 rate(1/dt)
 x = bob2.pos.x - bob1.pos.x
 spring.force = spring.const*(x - spring.l)

 alpha1=-(g/L1)*sin(theta1) + (spring.force/bob1.m*L1)
 omega1=omega1+alpha1*dt
 theta1=theta1+omega1*dt

 bob1.pos=pivot1 + vec(L1*sin(theta1),-L1*cos(theta1),0)
 rod1.axis=bob1.pos-pivot1

 alpha2=-(g/L2)*sin(theta2) - (spring.force/bob2.m*L2)
 omega2=omega2+alpha2*dt
 theta2=theta2+omega2*dt

 bob2.pos=pivot2 + vec(L2*sin(theta2),-L2*cos(theta2),0)
 rod2.axis=bob2.pos-pivot2
 
 spring.pos=bob1.pos
 spring.axis=bob2.pos-bob1.pos