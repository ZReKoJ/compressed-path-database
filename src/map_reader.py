from PIL import Image
import numpy as np

def imageToMatrix(image_path, width=None, height=None, threshold=128):

    image = Image.open(image_path)
    image_grey = image.convert('L')

    image_binary = image_grey.point(lambda point : point > threshold and 1)

    if (width is not None and height is not None):
        image_binary = image_binary.resize((width, height), Image.NEAREST)

    return np.array(image_binary)