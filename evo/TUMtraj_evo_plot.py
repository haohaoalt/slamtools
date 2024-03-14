# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt

from evo.tools import file_interface
from evo.core.trajectory import PoseTrajectory3D

###########################
# data loading

# file_path = os.path.join(os.path.dirname(__file__), "..", "..", "devel", "lib", "orb_slam2_ros")
file_path = os.path.join(os.path.dirname(__file__))

file_one = "C-5f.txt"
# file_two = "B-1f.txt"

file_path_one = os.path.join(file_path, file_one)
# file_path_two = os.path.join(file_path, file_two)

poses = file_interface.read_tum_trajectory_file(file_path_one)

# [:, 0]，[:, 1]，[:, 2]是numpy数组的切片操作。:表示选取所有行，0，1，2分别表示选取第0，1，2列
x = poses.positions_xyz[:, 0]
y = poses.positions_xyz[:, 1]  # Change to y-axis
z = poses.positions_xyz[:, 2]

#############################
# configure plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.plot(x,y, z,color="#0065BD", linewidth=2)

leg = plt.legend([file_one])

ax.set_xlabel("x in m")
ax.set_ylabel("y in m")
ax.set_zlabel("z in m")

ax.set_xlim(-50, 50)
ax.set_ylim(-100, 100)
ax.set_zlim(-50, 50)

# 取消背景的格子
ax.grid(False)

plt.show()
