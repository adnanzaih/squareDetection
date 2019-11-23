import argparse
import pydicom
from skimage.morphology import square, disk
from skimage.morphology import white_tophat
from skimage.filters.rank import bottomhat
import cv2
from tqdm import tqdm
import numpy as np
import time


def Analyze(input):
    path = "/Users/adnanhafeez/Documents/Python Programming/PRACTICE1/wintson lutz results/Z20190312/RI.Z20190312.C0 G0 T0-2_1_19.dcm"
    filename = pydicom.read_file(input)
    img = filename.pixel_array
    detectField(img)


def detectField(input):

    output = bottomhat(input, square(50))
    blur = cv2.GaussianBlur(output, (5, 5), 0)
    _, threshold = cv2.threshold(blur, 230, 255, 0)
    threshold = threshold.astype('uint8')
    cv2.imshow('Field', threshold)
    cv2.waitKey(0)
    return threshold


parser = argparse.ArgumentParser()
parser.add_argument('-input', dest='input', help='Winston-Lutz dicom path', type=str)
results = parser.parse_args()
Analyze(results.input)


