import sys
import os
#sys.path.insert(0,'/Users/dheenu/Desktop/Controls and Robotics/SLAM/Claus Brenner/Unit_A')
#from pathlib import Path #to get the file path

from pylab import *     #to plot

from lego_robot import LegoLogfile

if __name__== '__main__':
    
    #file_to_open = Path("/Users/dheenu/Desktop/Controls and Robotics/SLAM/Claus Brenner/Unit_A/robot4_motors.txt")

    f = open("robot4_motors.txt")

    left_list = []
    right_list = []

    for l in f:
        split = l.split()       #splits the text file as array

        left_list.append(int(split[2]))  #we are only interested in the second column of the text file (left motor)
        right_list.append(int(split[6]))

    #plot(left_list)
    #plot(right_list)
    #show()

    logfile = LegoLogfile()
    logfile.read("robot4_motors.txt")

    plot(logfile.motor_ticks)
    show()
