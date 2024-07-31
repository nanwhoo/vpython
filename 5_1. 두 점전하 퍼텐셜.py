k = 9e9
q1 = sphere(pos=vec(3,0,0), radius=0.5, q = 1, color=color.red)
q2 = sphere(pos=vec(-3,0,0), radius=0.5, q = -1, color=color.cyan)

def V(Q, ro) :
    r = ro - Q.pos
    V = k* Q.q/mag(r)
    return(V)
    
for x in range(-10, 10, 0.15):
    for y in range(-10, 10, 0.15):
        r = vec(x, y, 0)
        Vt = V(q1,r) + V(q2,r)
        arrow(pos = r, axis=vec(0,0,1e-10*Vt), shaftwidth=0.1)