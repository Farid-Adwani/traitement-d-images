from math import floor
import matplotlib.pyplot as plt

import numpy as np
from numpy import array, int32
import random
def show_img(image):
    plt.imshow(image)
    plt.show()
def im_read(path):
    with open(path, 'rb') as pgmf:
        im = plt.imread(pgmf)
    return im

pepper = im_read('./peppers.ppm')
