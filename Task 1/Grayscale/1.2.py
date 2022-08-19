
import numpy as np
from PIL import Image

img = np.asarray(Image.open("bees.jpg"));

red, green, blue = img[:, :, 0], img[:, :, 1], img[:, :, 2]

bwimage = 0.3333 * red + 0.3333 * green + 0.3333 * blue
bwimage=bwimage.astype(np.uint8);

Image.fromarray(bwimage).save("grayscale 1.2.jpg");