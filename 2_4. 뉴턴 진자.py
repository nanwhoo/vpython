ceiling = box(size=vec(0.8,0.005,0.8), color=color.green)
n = 5

g = 10
size, m = 0.02, 0.5
L, k = 0.5, 150000

x = [-0.08, -0.04, 0, 0.04, 0.08, 0.12]

dt = 0.001

balls = []
rods = []

for i in range(n):
    ball = sphere(radius = size, color = color.blue)
    ball.pos = vec(x[i], -L -m*g/k, 0)
    ball.v = vec(0, 0, 0)
    ball.m = m
    balls.append(ball)
    
    rod = cylinder(radius = 0.005, color=color.red)
    rod.pos = vec(x[i], 0, 0)
    rod.axis = ball.pos - rod.pos
    rods.append(rod)

balls[1].v = vec(-1,0,0)
balls[2].v = vec(-1,0,0)

def af_col_v(m1, m2, v1, v2, x1, x2):
    v1_prime = v1 + 2*(m2/(m1+m2))*(v2-v1)
    v2_prime = v2 + 2*(m1/(m1+m2))*(v1-v2)
    return (v1_prime, v2_prime)
    
scene.center=vec(0,-0.15,0)
scene.waitfor("click")
while True:
    rate(1/dt)
    for i in range(n):
        rods[i].axis = balls[i].pos - rods[i].pos
        force = -k*(mag(rods[i].axis)-L)*rods[i].axis.norm()
        balls[i].a = vec(0, -g, 0) + force/m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
        for i in range(n-1):
            if (mag(balls[i].pos - balls[i+1].pos) < 2*size and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) < 0):
                balls[i].v, balls[i+1].v = af_col_v(balls[i].m, balls[i+1].m, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)
