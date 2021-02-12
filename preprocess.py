#!/usr/bin/env python3

import cv2
import numpy as np

def preprocess_image(image_path):
    img1 = cv2.imread(image_path)
    a = np.double(img1)
    b = a + 15
    img2 = np.uint8(b)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(img2, -1, sharpen_kernel)

    cv2.imshow('sharpen', sharpen)
    try:
        image_split = image_path.split(".")
        image_path_new = image_split[:-2]+"pp."+image_split[-1]
        cv2.imwrite(image_path_new, sharpen)
    except:
        image_path_new = image_path
        cv2.imwrite(image_path, sharpen)

    return image_path_new
