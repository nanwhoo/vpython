g=9.8
L=0.5

theta1=10
theta1=theta1*pi/180
omega1=0

pivot=vec(0,0.3,0)
roof=box(pos=pivot,size=vec(0.5,0.01,0.5),color=color.green)
bob1=sphere(pos=pivot + vec(L*sin(theta1),-L*cos(theta1),0), radius=0.05, color=color.blue)
rod1=cylinder(pos=pivot,axis=bob1.pos-pivot,radius=0.01, color=color.red)

dt=0.001
scene.waitfor("click")
while True:
  rate(1/dt)
  alpha1=-(g/L)*sin(theta1)
  omega1=omega1+alpha1*dt
  theta1=theta1+omega1*dt
  bob1.pos=pivot + vec(L*sin(theta1),-L*cos(theta1),0)
  rod1.axis=bob1.pos-pivot