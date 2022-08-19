from PIL import Image
import numpy as np

img = np.asarray(Image.open("Arrow_2.jpg"))
height, width = img.shape[0], img.shape[1]
minX = 0
maxX = width - 1
minY = 0
maxY = height - 1
maxFound = False

def isInRange(x, y):
    return x, y >= 0 and y < height and x < width


def isWhite(y, x):
    for i in range(0, 3):
        if (img[y, x, i] > 250):
            return True
        return False


for x in range(0, width):
    isPxWhite = False
    for y in range(0, height):
        if (isWhite(y, x)):
            isPxWhite = True
            break
    if (maxFound and isPxWhite):
        maxX = x + 1
    if ((not maxFound) and (not isPxWhite)):
        minX = x+1
    if ((not maxFound) and isPxWhite):
        maxFound = True

maxFound = False

for y in range(0, height):
    isPxWhite = False

    for x in range(0, width):
        if (isWhite(y, x)):
            isPxWhite = True
            break

    if (maxFound and isPxWhite):
        maxY = y + 1
    if ((not maxFound) and (not isPxWhite)):
        minY = y+1

    if ((not maxFound) and isPxWhite):
        maxFound = True


maxFound = False
x = 0
y = 0
northMin, northMax, westMin, westMax, eastMin, eastMax, southMin, southMax = 0, 0, 0, 0, 0, 0, 0, 0

LookingForEnd = False;
for x in range (minX, maxX):
    white = isWhite(minY, x)
    if (white):
        if (not LookingForEnd):
            LookingForEnd = True;
            northMin = x;
    if ((not white) and LookingForEnd):
        LookingForEnd = True;
        northMax = x;
        break;

LookingForEnd = False;
for x in range (minX, maxX):
    white = isWhite(maxY - 1, x)
    if (white):
        if (not LookingForEnd):
            LookingForEnd = True;
            southMin = x;
    if ((not white) and LookingForEnd):
        LookingForEnd = True;
        southMax = x;
        break;

LookingForEnd = False;
for y in range (minY, maxY):
    white = isWhite(y, minX)
    if (white):
        if (not LookingForEnd):
            LookingForEnd = True;
            westMin = y;
    if ((not white) and LookingForEnd):
        LookingForEnd = True;
        westMax = y;
        break;

LookingForEnd = False;
for y in range (minY, maxY):
    white = isWhite(y, maxX - 1)
    if (white):
        if (not LookingForEnd):
            LookingForEnd = True;
            eastMin = y;
    if ((not white) and LookingForEnd):
        LookingForEnd = True;
        eastMax = y;
        break;

north=abs(northMin-northMax)
south=abs(southMin-southMax)
east=abs(eastMin-eastMax)
west=abs(westMin-westMax)

if north > max(south,west,east):
    print("South")
elif south > max(north,west,east):
    print("North")
elif east > max(north,west,south):
    print("West")
elif west > max(north,east,south):
    print("East")