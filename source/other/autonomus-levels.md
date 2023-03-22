# Levels of Autonomus 

The majority of autonomus programs in VEX can be placed into three categories.


## Motor Control
The first tier of autonomy consists of controlling the robot's motors via a PID loop or Motion Profiling. [V5 Smart Motors](https://www.vexrobotics.com/276-4840.html) includes a built-in PID with pre-tuned PID values. However, since these values have never been released, is it impossible to figure out a good starting point and/or the scale the default values are based on. Creating a PID loop that changes the voltage of the motors (such as through [move()](https://pros.cs.purdue.edu/v5/api/cpp/motors.html?highlight=move#move)) as an output is reccomended. 

## Odometry
The second tier of autonomy, odometry involves using various sensors to keep a live record of your robot's position for PID. Odometry in VEX usually comes in the form of tracking wheels and rotational encoders.

## Path Follower


