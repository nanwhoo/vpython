g=9.8
L=20
theta=10
theta=theta*pi/180
omega=0

omega1=0
alpha1=1
alpha1=alpha1*pi/180
pivot=vec(0,20,0)

bob=sphere(make_trail=True, pos=vec(L*sin(theta), pivot.y-L*cos(theta),0), radius=0.5, color=color.blue)

roof = box(pos = pivot , size = vec (10 ,0.5 , 10) , color = color.green)
rod = cylinder(pos = pivot, axis = bob.pos - pivot, radius = 0.1, color = color.red)

dt=0.01

scene.center=vec(0,12,0)
scene.waitfor('click')
while True: 
    rate(1000)
    alpha=-(g/L)*sin(theta)
    omega=omega+alpha*dt
    theta=theta+omega*dt 
    x = L*sin(theta)
    y = pivot.y - L*cos(theta)
    z = 0
    omega1=omega1+alpha1*dt
    x1 = cos(omega1)*x+sin(omega1)*z
    y1 = y
    z1 = -sin(omega1)*x+cos(omega1)*z
    bob.pos=vec(x1,y1,z1)
    rod.axis=bob.pos - pivot
