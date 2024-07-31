g=9.8
n=10

L=0.5
bobs = []
rods = []
thetas = []
omegas = []
alphas = []

pivot=vec(0,0.3,0)
roof=box(pos=pivot,size=vec(0.5,0.01,0.5),color=color.green)

for i in range(n):
  thetas[i] = 3 * i
  thetas[i] = thetas[i] * pi /180
  bobs[i] = sphere(pos = vec(L*sin(thetas[i]), pivot.y -L*cos(thetas[i]), 0), radius = 0.05, color=color.blue)
  rods[i] = cylinder(pos = pivot, axis = bobs[i].pos - pivot, radius=0.01, color = color.red)
  omegas[i] = 0

t = 0
dt = 0.01

scene.waitfor("click")
while True:
  rate(1/dt)
  for i in range(n):
    alphas[i] = - (g/L) * sin(thetas[i])
    omegas[i] = omegas[i] + alphas[i]*dt
    thetas[i] = thetas[i] + omegas[i]*dt
    bobs[i].pos = vec(L*sin(thetas[i]), pivot.y-L*cos(thetas[i]), 0)
    rods[i].axis = bobs[i].pos - pivot