g=9.8
n=5

L=[]
bobs = []
rods = []
thetas = []
omegas = []
alphas = []

pivot=vec(0,0.4,0)
roof=box(pos=pivot,size=vec(0.5,0.01,0.5),color=color.green)

for i in range(n):
    L[i] = 0.2*(i+1)
    thetas[i] = 20
    thetas[i] = thetas[i] * pi /180
    omegas[i] = 0
    bobs[i] = sphere(pos = vec(L[i]*sin(thetas[i]), pivot.y -L[i]*cos(thetas[i]), 0), radius = 0.05, color=color.blue)
    rods[i] = cylinder(pos = pivot, axis = bobs[i].pos - pivot, radius=0.01, color = color.red)

dt=0.001
scene.waitfor("click")
while True:
    rate(1/dt)
    for i in range(n):
        alphas[i] = - (g/L[i])*sin(thetas[i])
        omegas[i] = omegas[i] + alphas[i]*dt
        thetas[i] = thetas[i] + omegas[i]*dt
        bobs[i].pos = vec(L[i]*sin(thetas[i]), pivot.y-L[i]*cos(thetas[i]), 0)
        rods[i].axis = bobs[i].pos - pivot
