import os
import ImageTransformation as iT
from PIL import ImageTk, Image

def performHenonManipulation(filename):
    resImage = iT.pixelManipulation(512, filename)
    return resImage

absImg = performHenonManipulation("ztest.bmp")
print(absImg)