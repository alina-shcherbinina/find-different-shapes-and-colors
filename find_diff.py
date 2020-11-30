# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:37:58 2020

@author: Alina Shcherbinina
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops
from skimage import color

image = plt.imread("balls_and_rects.png")

binary = image.copy()[:, :, 0]
binary[binary > 0] = 1

image = color.rgb2hsv(image)[:, :, 0]

def centroid(lb, label=1):
    pos = np.where(lb == label)

    cy = np.mean(pos[0])
    cx = np.mean(pos[1])

    if cy == cx:
        return 1
    return 0

def find_colors(arr):
    orange = 0
    yellow = 0
    green = 0
    blue = 0
    magenta = 0
    
    for c in arr:
        if c < 0.06:
            orange += 1
        if c > 0.06 and c < 0.2:
            yellow += 1
        if c > 0.2 and c < 0.42:
            green += 1
        if c > 0.42 and c < 0.62:
            blue += 1
        if c > 0.62:
            magenta += 1

    print("Orange:", orange, "Yellow:", yellow, "Green:", green, "Blue:", blue, "Magenta:", magenta)


labeled = label(binary)

# vars 
colors = []
balls = []
rects = []

for region in regionprops(labeled):
    circ = region.perimeter ** 2 / region.area
    
    bb = region.bbox
    val = np.max(image[bb[0]:bb[2], bb[1]:bb[3]])
    
    colors.append(val)
    
    if centroid(region.image) == 0:
        rects.append(val)
    else:
        balls.append(val)

colors.sort()
rects.sort()
balls.sort()

print("Balls:", len(balls))
find_colors(balls)

print("Rects:", len(rects))
find_colors(rects)

print("In total:", np.max(labeled))


