import serial
import time
import string
import numpy as np
ser = serial.Serial('COM52',baudrate = 19200, timeout= 5)
while 1:
    #data = ser.readline().decode("ascii")
    #a=np.savetxt("rcv.txt",data,delimiter=", ")
    #print(data) */
    c=open("rcv.txt","r")
    print(c.read())