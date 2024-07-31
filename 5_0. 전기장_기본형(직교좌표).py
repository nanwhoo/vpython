k = 8.99e9  
q = 1e-9  

charge = sphere(pos=vec(0, 0, 0), radius=0.1, color=color.red)

for x in range(-7, 7, 2):
    for y in range(-7, 7, 2):
        for z in range(-7, 7, 2):
            r = vec(x, y, z)
            E = k * q * r / mag(r)**3
            arrow(pos=r, axis = E)