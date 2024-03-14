# NOT WORK
import math
import numpy as np
import rospy
from std_msgs.msg import std_msgs
from plot_py.msg import INS_Data
import time
from matplotlib.animation import FuncAnimation
import os
from math import sin, cos, radians

a = 6378137.  # 长轴
f = 1 / 298.257223563  # 扁率
fle = open("gps.txt", mode='w')


def gps_to_cartesion(lat, lon, alt):
    lat = radians(lat)
    lon = radians(lon)
    print(lat, lon, alt)
    b = a * (1 - f)
    e = (a ** 2 - b ** 2) ** 0.5 / a
    N = a / (1 - e ** 2 * sin(lat) ** 2) ** 0.5

    # 计算XYZ坐标
    X = (N + alt) * cos(lat) * cos(lon)
    Y = (N + alt) * cos(lat) * sin(lon)
    Z = (N * (1 - e ** 2) + alt) * sin(lat)

    return X, Y, Z


def callback(data):
    x, y, z = gps_to_cartesion(data.latitude, data.longitude, data.altitude)
    stamp = data.header.stamp
    time = float(stamp.secs) + (stamp.nsecs / 1e+9)
    fle.write(str(time) + " " + str(x) + " " + str(y) + " " + str(z))
    fle.write(" 0. 0. 0. 0.\n")
    # print(x,y,z)
    print(str(time) + " " + str(x) + " " + str(y) + " " + str(z))
    print("\n")


def save_as_txt():
    rospy.init_node('GPS', anonymous=True)
    rospy.Subscriber("/gps/fix", INS_Data, callback)
    rospy.spin()
    fle.close()


save_as_txt()
