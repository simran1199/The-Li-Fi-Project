import base64
import pandas as pd
import numpy as np 
from numpy import asarray
import PIL
from PIL import Image



image = Image.open('download.png')
img1 =  image.resize((28,28))
im1= img1.save('res.png')

with open("res.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(str)
text_file = open("sample.txt", "wb")
n = text_file.write(str)
text_file.close()    