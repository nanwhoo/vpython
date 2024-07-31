k = 8.99e9  
q = 1e-9  

charge = sphere(pos=vec(0, 0, 0), radius=0.1, color=color.red)
            
for r in range(2, 10, 1):
    for phi in range (0, pi, pi/6):
        for theta in range(0, 2*pi, pi/6):
            R = vec(r*sin(phi)*cos(theta),r*sin(phi)*sin(theta), r*cos(phi))
            E = k * q * R / mag(R)**3
            arrow(pos=R, axis = E)