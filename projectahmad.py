def init():
    get input from user
    define map, vehicle, sensor
    connect all of them

def find_best_path(readings)
    return steer

def read_sensor()
    return readings # x, y coordinates

def should_stop(T0, veh)
    if((abs(T0[0]-veh.x[0]) >0.2) or (abs(T0[1]-veh.x[1]) > 0.2)):
        return True
    else:
        return False

def run(T0, veh):
    run = True
    while(run)
    steer = (find_best_path(read_sensor()))
    veh.step(8,steer)
    if should_stop(T0, veh):
        return True
    veh._animation.update(veh.x)
    plt.pause(0.005)

T0, veh = init()
run(T0, veh)
    keep running untill target achieved
    start from initial point
    veh.step
    check sensor for obstacle check_obstacle()
        if found:
        avoid_obstacle()
        else:
        keep 
