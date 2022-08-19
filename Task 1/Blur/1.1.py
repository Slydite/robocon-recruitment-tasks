from PIL import Image
import numpy as np

img = np.asarray(Image.open("hills.jpg"));
h = img.shape[0];
w = img.shape[1];

finalImage = np.arange(h * w * 3).reshape(h, w, 3).astype(np.uint8);

def isInRange(x, y):
    return y >= 0 and x >= 0 and y < h and x < w;

for x in range (0, w):
    for y in range (0, h):
        r = g = b = 0;
        k = 0;
        for i in range (-3, 4):
            for j in range (-3, 4):
                if (isInRange(x + j, y + i)):
                    r += img[y + i , x + j][0];
                    g += img[y + i , x + j][1];
                    b += img[y + i , x + j][2];
                    k += 1;
        r = r / k;
        g = g / k;
        b = b / k;
        
        finalImage[y, x] = [r,g, b];
#finalImage=finalImage;
Image.fromarray(finalImage.astype(np.uint8)).save("blurred.jpg");