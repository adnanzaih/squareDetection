import argparse
import pydicom
from skimage.morphology import square, disk
from skimage.morphology import white_tophat
from skimage.filters.rank import bottomhat, tophat
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

    input = input.astype('uint8')
    input = tophat(input, disk(1))
    smoothing = gaussian_kernel(size=10)
    edge = cv2.filter2D(input, -1, smoothing)
    cv2.imshow('Field', edge)
    cv2.waitKey(0)
    return


def gaussian_kernel(size, sigma=5):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g


parser = argparse.ArgumentParser()
parser.add_argument('-input', dest='input', help='Winston-Lutz dicom path', type=str)
results = parser.parse_args()
Analyze(results.input)


