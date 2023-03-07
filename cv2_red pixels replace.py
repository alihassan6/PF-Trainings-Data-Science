import cv2
import numpy as np
from PIL import Image

im_array = cv2.imread('imagee.png')
display(Image.fromarray(cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB)))

hsv = cv2.cvtColor(im_array, cv2.COLOR_BGR2HSV)

red_lower_range = np.array([0, 100, 100])
red_upper_range = np.array([9, 255, 255])

mask_0 = cv2.inRange(hsv, red_lower_range, red_upper_range)

red_lower_range = np.array([160, 100, 100])
red_upper_range = np.array([179, 255, 255])

mask_1 = cv2.inRange(hsv, red_lower_range, red_upper_range)
mask_2 = mask_0 + mask_1

for i in range(im_array.shape[0]):
    for j in range(im_array.shape[1]):
        if mask_2[i, j] == 255:
            im_array[i, j] = [0, 0, 0]


display(Image.fromarray(cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB)))
