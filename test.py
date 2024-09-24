import sys
sys.path.append("./src")

import serial
from uservo import UartServoManager


SERVO_PORT_NAME = "COM3"

SERVO_BAUDRATE = 115200

uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
                     parity=serial.PARITY_NONE, stopbits=1,\
                     bytesize=8,timeout=0)

uservo = UartServoManager(uart)

def ping(servo_id:int):
    
    while servo_id < 5:
        is_online = uservo.ping(servo_id)
        print("舵机ID={} 是否在线: {}".format(servo_id, is_online))
        servo_id += 1

servo_id = int(input("舵机编号:"))
ping(servo_id)
