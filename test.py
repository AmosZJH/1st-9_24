import sys
sys.path.append("./src")

import serial
from uservo import UartServoManager


SERVO_PORT_NAME = "COM3"
SERVO_BAUDRATE = 115200

uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
                     parity=serial.PARITY_NONE, stopbits=1,\
                     bytesize=8,timeout=0)#初始化串口

uservo = UartServoManager(uart)
servo_id = int(input("舵机编号:"))
while servo_id < 5:
    is_online = uservo.ping(servo_id)#查询舵机是否在线
    print("舵机ID={} 是否在线: {}".format(servo_id, is_online))

    servo_angel = uservo.query_servo_angle(servo_id)#查询舵机角度
    print("舵机ID={} 角度: {}".format(servo_id, servo_angel))
    servo_id += 1


uservo.set_servo_angle(1, 30, False, None, 20, 20, 20, 0, 100.0)

uservo.set_servo_angle(2, 50, False, None, None, 20, 20, 0, 100.0)

uservo.set_servo_angle(3, 20, False, None, None, 20, 20, 0, 100.0)

uservo.set_servo_angle(4, 60, False, None, None, 20, 20, 0, 100.0)



    
   

