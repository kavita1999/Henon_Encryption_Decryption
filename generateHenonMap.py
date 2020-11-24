from PIL import Image

def getImageMatrix(image):
    im = Image.open(image)  
    pix = im.load()
    image_size = im.size #Get the width and height of the image for iterating 
    print("Image Size : ",image_size)
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
           try:
               #Getting only the blue pixels
                row.append((pix[width,height]))
           except:
                row=[pix[width, height]]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]
    # Not able to perform file operations when imported into another module
    #file = open("ImageMatrix.csv","w")
    #file.write(str(image_matrix))
    #file.close()
    #USE TO SAVE IF THE IMAGE MATRIX SHOULD BE USED FOR NEXT MAPS
    return image_matrix


def dec(bitSequence):
    decimal = 0
    for bit in bitSequence:
        decimal = decimal * 2 + int(bit)
    return decimal


#Takes size of the image as an input
def genTransformationMatrix(m):
    #Replace Hardcoded Pixel Values
    #Serves as the initial Parameter and also the symmetric secret key
    x = 0.1
    y = 0.1
    sequenceSize = m * m * 8 #Total Number of bitSequence produced
    bitSequence = []    #Each bitSequence contains 8 bits
    byteArray = []      #Each byteArray contains m( i.e 512 in this case) bitSequence
    TImageMatrix = []   #Each TImageMatrix contains m*n byteArray( i.e 512 byteArray in this case)
    for i in range(sequenceSize):
        #Henon Map formula
        xN = y + 1 - 1.4 * x**2
        yN = 0.3 * x

        # New x = xN and y = yN
        x = xN
        y = yN

        # Each Value of xN is converted into 0 or 1 based on the threshold value
        if xN <= 0.3992:
            bit = 0
        else:
            bit = 1
        #bits are inserted into bitSequence
        try:
            bitSequence.append(bit)
        except:
            bitSequence = [bit]
        #Each bitSequence is converted into a decimal number
        #This decimal number is inserted into byteArray
        if i % 8 == 7:
            decimal = dec(bitSequence)
            try:
                byteArray.append(decimal)
            except:
                byteArray = [decimal]
            print(bitSequence,decimal)
            bitSequence = []
        #ByteArray is inserted into TImageMatrix
        byteArraySize = m*8
        if i % byteArraySize == byteArraySize-1:
            print(byteArray)
            try:
                TImageMatrix.append(byteArray)
            except:
                TImageMatrix = [byteArray]
            print(len(byteArray),byteArray)
            byteArray = []
            
    return TImageMatrix

