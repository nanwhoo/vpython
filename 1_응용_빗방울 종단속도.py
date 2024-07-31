g, rho_air, rho_water = 10, 1.225, 1000  
Cd = 0.47  

rain = sphere(radius=0.001, color=color.blue)
rain.mass = (4/3) * pi * rain.radius**3 * rho_water  
rain.area = pi * rain.radius**2

rain.pos = vec(0,10,0)
rain.vel = vec(0,0,0)
rain.acc = vec(0,-g,0)
attach_arrow(rain,"vel")

g_v = graph(title="v-t", xtitle="t(s)", ytitle="v(m/s)")
v_t = gcurve(color=color.red)

v, t, dt = 0, 0, 0.01
scene.waitfor('click')
while t<5:  
    rate(100)
    Fd = 0.5 * rho_air * mag2(rain.vel) * Cd * rain.area
    Fnet = - rain.mass * g + Fd
    rain.acc.y = Fnet / rain.mass
    rain.vel.y += rain.acc.y * dt
    rain.pos.y += rain.vel.y * dt
    v_t.plot(t, rain.vel.y)
    t += dt

print("terminal velocity=",rain.vel.y,"(m/s)")