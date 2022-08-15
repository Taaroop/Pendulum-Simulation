import math
import matplotlib.pyplot as plt

length = 10
g = 9.8
theta = 30
velo = 0
sim_time = 100

dt = 0.1
t_elapsed = 0

li_time = [0]
li_angle = [theta]

while t_elapsed < sim_time:
    acc = g*math.sin((math.pi/180)*theta)
    velo = velo + (acc*dt)
    d_theta = (velo*dt)/length
    d_theta = d_theta*(180/math.pi)
    theta = theta-d_theta
    t_elapsed += dt
    
    li_time.append(t_elapsed)
    li_angle.append(theta)

plt.plot(li_time, li_angle)
