import os
import HenonDecryption as hD
from PIL import ImageTk, Image

def decryptHenonManipulation(filename):
    resImage = hD.decryptHenonImage(filename)
    return resImage

absImg = decryptHenonManipulation("HenonTransformedImage.bmp")
print(absImg)