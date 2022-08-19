
import numpy as np
from PIL import Image

#grayscale
img = np.asarray(Image.open("flower.jpg"))

red, green, blue = img[:, :, 0], img[:, :, 1], img[:, :, 2]

bwimage = 0.3333 * red ** 0.9 + 0.3333 * green ** 0.9 + 0.3333 * blue ** 0.9
bwimage = bwimage.astype(np.uint8)
Image.fromarray(bwimage).save("grayscale 1.3.jpg")

#sobel
sobelX = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
sobelY = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
[rows, columns] = np.shape(bwimage)
finalImage = np.zeros(shape=(rows, columns))

for i in range(rows - 2):
    for j in range(columns - 2):
        xaxis = np.sum(np.multiply(sobelX, bwimage[i:i + 3, j:j + 3]))
        yaxis = np.sum(np.multiply(sobelY, bwimage[i:i + 3, j:j + 3]))
        finalImage[i + 1, j + 1] = np.sqrt(xaxis ** 2 + yaxis ** 2)
finalImage = finalImage.astype(np.uint8)
Image.fromarray(finalImage).save("sobel.jpg")
