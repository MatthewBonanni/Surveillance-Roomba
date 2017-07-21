import serial
import time

from commandlib import *

#Open serial connection
global ser
ser = serial.Serial('/dev/ttyUSB0', 115200)

def drive_seq(vel, rad):
    vel_high, vel_low = hex_split(vel)
    rad_high, rad_low = hex_split(rad)

    ser.write(DRIVE)
    ser.write(cmd_form(vel_high))
    ser.write(cmd_form(vel_low))
    ser.write(cmd_form(rad_high))
    ser.write(cmd_form(rad_low))

#Initialize Roomba
ser.write(START)
ser.write(SAFE)

#Demo commands
ser.write(CLEAN)
time.sleep(3)
ser.write(CLEAN)

drive_seq(200, STRAIGHT)
time.sleep(3)
drive_seq(0, STRAIGHT)

#Terminate
ser.write(STOP)
ser.close()
