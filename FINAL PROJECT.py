from roboticstoolbox import Bicycle, VehicleIcon, RandomPath, LandmarkMap, RangeBearingSensor
from math import pi, atan2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.io import loadmat


def detect_obstacles(readings):
    for i in readings:
        if (i[0] < 4 and abs(i[1]) < pi/10):
            return False
    return True


def egry(x0, T0, veh, run, sensor):
    while(run):
        T0_heading = atan2(
        T0[1] - veh.x[1],
        T0[0] - veh.x[0]
        )
        steer = T0_heading - veh.x[2]
        veh.step(4, steer)
        if((abs(T0[0]-veh.x[0]) > 0.05) or (abs(T0[1]-veh.x[1]) > 0.05)):
            run = True
            if( not detect_obstacles(sensor.h(veh.x))):
                run = False
        else:
            run = False
        veh._animation.update(veh.x)
        plt.pause(0.005)


def goTo(x, y, veh, sensor):
    while True:
        goal_heading = atan2(
            y - veh.x[1],
            x - veh.x[0]
        )
        steer = goal_heading - veh.x[2]
        veh.step(4, steer)
        if((abs(x-veh.x[0]) > 0.5) or (abs(y-veh.x[1]) > 0.5)):
            if(not detect_obstacles(sensor.h(veh.x))):
                steer = (steer - 0.5) if steer >= 0 else (steer + 0.5)
                for _ in range(10):
                    veh.step(4, steer)
                    veh._animation.update(veh.x)
                    plt.pause(0.005)
            veh._animation.update(veh.x)
            plt.pause(0.005)
        else:
            break


# Global Variables
x0 = (int(input('please input your x-value: ')), int(input('please input your y-value: ')), int(input('please input your theta-value: '))) # x0 = start point
T0 = (int(input('please input your Target x-value: ')), int(input('please input your Target y-value: ')),int(input('please input your Target theta-value: ')) )  # T0 = target
T1 = (-10, -10)
T2 = (30, -10)
T3 = (30, -22.5)
T4 = (30, 10)
T5 = (-20, -25)
prin = False


anim = VehicleIcon('/home/it/Desktop/robo.png', scale=6)
veh = Bicycle(
    animation=anim,
    control=RandomPath,
    dim=50,
    x0=[x0[0], x0[1], x0[2]])
veh.init(plot=True)
map = LandmarkMap(100, 50)  # no of obsticals = 25, gridsize = 50
map.plot()
image = mpimg.imread("/home/it/Desktop/map.png")
plt.imshow(image, extent=[-50, 50, -50, 50])


# places target marker

T0_marker_style = {
    'marker': 'D',
    'markersize': 6,
    'color': 'r',
}
plt.plot(T0[0], T0[1], **T0_marker_style)

#draws the map

rectangle = plt.Rectangle((-50, -50), 5, 100, fc='red', ec="red")
rectangle1 = plt.Rectangle((0, -50), 50, 5, fc='red', ec="red")
rectangle2 = plt.Rectangle((-5, -50), 5, 33.25, fc='red', ec="red")
rectangle3 = plt.Rectangle((-5, -21.75), 25, 5, fc='red', ec="red")
rectangle4 = plt.Rectangle((-45, -21.75), 20, 5, fc='red', ec="red")
rectangle5 = plt.Rectangle((-45, 2.5), 65, 5, fc='red', ec="red")
rectangle6 = plt.Rectangle((40, -45), 5, 28.25, fc='red', ec="red")
rectangle7 = plt.Rectangle((45, -21.75), 5, 5, fc='red', ec="red")
rectangle8 = plt.Rectangle((-25, 45), 75, 5, fc='red', ec="red")
rectangle9 = plt.Rectangle((40, 2.5), 5, 42.5, fc='red', ec="red")
rectangle10 = plt.Rectangle((45, 2.5), 5, 5, fc='red', ec="red")
plt.gca().add_patch(rectangle)
plt.gca().add_patch(rectangle1)
plt.gca().add_patch(rectangle2)
plt.gca().add_patch(rectangle3)
plt.gca().add_patch(rectangle4)
plt.gca().add_patch(rectangle5)
plt.gca().add_patch(rectangle6)
plt.gca().add_patch(rectangle7)
plt.gca().add_patch(rectangle8)
plt.gca().add_patch(rectangle9)
plt.gca().add_patch(rectangle10)


# Allows robot to sense surrounding
# sensor = RangeBearingSensor(robot=veh, map=map, animate=True)
prin = input ("do you want to print the sensor readings? (True or False)")
if (prin = True):
    print('Sensor readings: ', sensor.h(veh.x))
veh._animation.update(veh.x)


# Sets rules for the robot's movment according to surroundings

# bottom left

# bottom left to top
run = True
if ((x0[0] < -10) and (x0[1] < -10) and (T0[0] < 40) and (T0[1] > 7.5)):
    goTo(T1[0], T1[1], veh, sensor)
    goTo(T2[0], T2[1], veh, sensor)
    goTo(T4[0], T4[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

# bottom left to bottom right

elif ((x0[0] < -10) and (x0[1] < -10) and (T0[0] < 40) and (T0[0] > 0) and (T0[1] < -22.5)):
    goTo(T1[0], T1[1], veh, sensor)
    goTo(T2[0], T2[1], veh, sensor)
    goTo(T3[0], T3[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

# bottom left to middle

elif ((x0[0] < -10) and (x0[1] < -10) and (T0[1] > -22.5) and (T0[1] < 5)):
    goTo(T1[0], T1[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

# bottom left to bottom left

elif ((x0[0] < -10) and (x0[1] < -10) and (T0[0] < -10) and (T0[1] < -10)):
    goTo(T0[0], T0[1], veh, sensor)

#-------------------------------------------------------------------------------------------------------------------------#

#top 

#top to top
elif ((x0[0] < 40) and (x0[1] > 7.5) and (T0[0] < 40) and (T0[1] > 7.5)):
    goTo(T0[0], T0[1], veh, sensor)

#top to bottom right

elif ((x0[0] < 40) and (x0[1] > 7.5) and (T0[0] < 40) and (T0[0] > 0) and (T0[1] < -22.5)):
    goTo(T4[0], T4[1], veh, sensor)
    goTo(T2[0], T2[1], veh, sensor)
    goTo(T3[0], T3[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

#top to middle

elif ((x0[0] < 40) and (x0[1] > 7.5) and (T0[1] > -22.5) and (T0[1] < 5)):
    goTo(T4[0], T4[1], veh, sensor)
    goTo(T2[0], T2[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

#top to bottom left

elif ((x0[0] < 40) and (x0[1] > 7.5) and (T0[0] < -10) and (T0[1] < -10)):
    goTo(T4[0], T4[1], veh, sensor)
    goTo(T2[0], T2[1], veh, sensor)
    goTo(T1[0], T1[1], veh, sensor)
    goTo(T5[0], T5[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

#-------------------------------------------------------------------------------------------------------------------------#

#bottom right

#bottom right to top

elif ((x0[0] < 40) and (x0[0] > 0) and (x0[1] < 22.5) and (T0[0] < 40) and (T0[1] > 7.5)):
    goTo(T3[0], T3[1], veh, sensor)
    goTo(T4[0], T4[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

#bottom right to bottom right

elif ((x0[0] < 40) and (x0[0] > 0) and (x0[1] < -22.5) and (T0[0] < 40) and (T0[0] > 0) and (T0[1] < -22.5)):
    goTo(T0[0], T0[1], veh, sensor)

#bottom right to middle

elif ((x0[0] < 40) and (x0[0] > 0) and (x0[1] < -22.5) and (T0[1] > -22.5) and (T0[1] < 5)):
    goTo(T3[0], T3[1], veh, sensor)
    goTo(T2[0], T2[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

#bottom right to bottom left

elif ((x0[0] < 40) and (x0[0] > 0) and (x0[1] < -22.5) and (T0[0] < -10) and (T0[1] < -10)):
    goTo(T3[0], T3[1], veh, sensor)
    goTo(T2[0], T2[1], veh, sensor)
    goTo(T1[0], T1[1], veh, sensor)
    goTo(T5[0], T5[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

#-------------------------------------------------------------------------------------------------------------------------#

#middle

#middle to top

elif ((x0[1] > -22.5) and (x0[1] < 5) and (T0[0] < 40) and (T0[1] > 7.5)):
    goTo(T2[0], T2[1], veh, sensor)
    goTo(T4[0], T4[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

#middle to bottom right

elif ((x0[1] > -22.5) and (x0[1] < 5) and (T0[0] < 40) and (T0[0] > 0) and (T0[1] < -22.5)):
    goTo(T2[0], T2[1], veh, sensor)
    goTo(T3[0], T3[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

#middle to middle

elif ((x0[1] > -22.5) and (x0[1] < 5) and (T0[1] > -22.5) and (T0[1] < 5)):
    goTo(T0[0], T0[1], veh, sensor)

#middle to bottom left

elif ((x0[1] > -22.5) and (x0[1] < 5) and (T0[0] < -10) and (T0[1] < -10)):
    goTo(T1[0], T1[1], veh, sensor)
    goTo(T5[0], T5[1], veh, sensor)
    goTo(T0[0], T0[1], veh, sensor)

#-------------------------------------------------------------------------------------------------------------------------#

# in case of any malfunction this should move the robot

else:
    egry(x0, T0, veh, run, sensor)

plt.pause(100)