from roboticstoolbox import DXform, Bicycle, VehicleIcon, RandomPath, LandmarkMap, RangeBearingSensor
from math import pi, atan2
import matplotlib.pyplot as plt
from scipy.io import loadmat


# Global Variables
x0 = (0, 0, 0)  # starting position
map = LandmarkMap(5, 500)  # no of obsticals = 5, gridsize = 500
map.plot()
image = mpimg.imread("map.png")
plt.imshow(image, extent=[-50, 50, -50, 50])
anim = VehicleIcon('/home/it/Desktop/robo.png', scale=75)

# Allows the robot to find the most efficent path
vars = loadmat(
    "/home/your_username/.local/lib/python3.6/site-packages/rtbdata/data/map1.mat")
map = vars['map']
dx = DXform(map)

# Recieves the robot's inital position
veh = Bicycle(
    animation=anim,
    control=RandomPath,
    dim=500,
    x0=(int(input('please input your x-value: ')), int(input('please input your y-value: ')),
        int(input('please input your theta-value: ')))
)
veh.init(plot=True)

# Recieves the robot's target position
T0 = (int(input('please input your Target x-value: ')),
      int(input('please input your Target y-value: ')))  # T0 = target
T0_marker_style = {
    'marker': 'D',
    'markersize': 6,
    'color': 'r',
}
plt.plot(T0[0], T0[1], **T0_marker_style)

# Allows robot to sense surroundings
sensor = RangeBearingSensor(robot=veh, map=map, animate=True)
print("Sensore Readings: ", sensor.h(veh.x))
veh._animation.update(veh.x)
map.plot()

# Sets rules for the robot's movment according to surroundings
run = True
while(run):
    T0_heading = atan2(
        T0[1] - veh.x[1],
        T0[0] - veh.x[0]
    )
    steer = T0_heading - veh.x[2]
    veh.step(2, steer)
    if((abs(T0[0]-veh.x[0]) > 0.2) or (abs(T0[1]-veh.x[1]) > 0.2)):
        run = True
    else:
        run = False
    veh._animation.update(veh.x)
    plt.pause(0.005)
plt.pause(100)

# Prints a path for the robot
dx.plan(T0)
p = dx.query(x0)
print(p)


dx.plot(path=p)
axes = plt.gca()
axes.set_xlim([0, 100])
axes.set_ylim([0, 100])
plt.pause(100)
