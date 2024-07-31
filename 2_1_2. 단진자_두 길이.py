g=9.8
L1=0.5
L2=1

theta1=10
theta1=theta1*pi/180
omega1=0

theta2=10
theta2=theta2*pi/180
omega2=0

pivot=vec(0,0.3,0)
roof=box(pos=pivot,size=vec(0.5,0.01,0.5),color=color.green)
bob1=sphere(pos=pivot + vec(L1*sin(theta1),-L1*cos(theta1),0), radius=0.05, color=color.blue)
rod1=cylinder(pos=pivot,axis=bob1.pos-pivot,radius=0.01, color=color.red)

bob2=sphere(pos=pivot + vec(L2*sin(theta2),-L2*cos(theta2),0), radius=0.05, color=color.blue)
rod2=cylinder(pos=pivot,axis=bob2.pos-pivot,radius=0.01, color=color.red)

dt=0.001
scene.waitfor("click")
while True:
  rate(1/dt)
  alpha1=-(g/L1)*sin(theta1)
  omega1=omega1+alpha1*dt
  theta1=theta1+omega1*dt
  bob1.pos=pivot + vec(L1*sin(theta1),-L1*cos(theta1),0)
  rod1.axis=bob1.pos-pivot

  alpha2=-(g/L2)*sin(theta2)
  omega2=omega2+alpha2*dt
  theta2=theta2+omega2*dt
  bob2.pos=pivot + vec(L2*sin(theta2),-L2*cos(theta2),0)
  rod2.axis=bob2.pos-pivot