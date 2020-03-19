import serial
import time
import numpy as np
import base64

#ser = serial.Serial('COM7',baudrate = 9600,timeout = 5)


while 1:

    data = open('Cool5.txt','rb')
    d_r = data.read()
    #d_r = ser.readline()
    #print(d_r)
    decode = base64.decodebytes(d_r)
    image_result = open('img_dec56.png','wb')
    image_result.write(decode)
    image_result.close()
    # data = base64.b64encode(data)
    # fh = open("imageToSave.png", "wb")
    # fh.write(data.decode('base64'))
    # fh.close()
