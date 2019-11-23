import argparse
import pydicom
from skimage.morphology import square
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
    #radiation field detection and contouring
    _, threshold = cv2.threshold(input, 230, 255, 0)  # field
    threshold = threshold.astype('uint8')
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    for cnt in contours:
        for i in tqdm(np.arange(len(contours))):
            cv2.drawContours(threshold, [cnt], -1, (78, 55, -128), 1)
            M = cv2.moments(cnt)
            time.sleep(0.1)
        i = i + 1
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(threshold, (cX, cY), 2, (78, 55, -128), 1)
    cv2.putText(threshold, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.imshow("Field", threshold)
    cv2.moveWindow("Field", 300, 30)
    print("X-Coordinate: " + str(cX))
    print("Y-Coordinate: " + str(cY))
    cv2.waitKey(0)
    return threshold, cX, cY
    #Done


parser = argparse.ArgumentParser()
parser.add_argument('-input', dest='input', help='Winston-Lutz dicom path', type=str)
results = parser.parse_args()
Analyze(results.input)


