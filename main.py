import argparse
import pydicom
from skimage.filters.rank import bottomhat
import cv2
from tqdm import tqdm
import numpy as np
import time


def Analyze(input):
    filename = pydicom.read_file(input)
    detectField(filename.pixel_array)


def detectField(input):
    #radiation field detection and contouring
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    output = bottomhat(input, kernal)  # disk(30))
    blur = cv2.GaussianBlur(output, (5, 5), 0)
    _, threshold = cv2.threshold(blur, 230, 255, 0)  # field
    threshold = threshold.astype('uint8')
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        for i in tqdm(np.arange(len(contours))):
        # Shortlisting the regions based on there area.
            if cv2.contourArea(cnt) > 2000:
                print(cv2.contourArea(cnt))
                approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
                # Checking if the no. of sides of the selected region is 4.
                cv2.drawContours(threshold, [approx], -1, (78, 55, -128), 1)
                M = cv2.moments(cnt)
                time.sleep(0.1)
        i = i + 1
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print (cX, cY)
    cv2.circle(threshold, (cX, cY), 2, (78, 55, -128), 1)
    cv2.putText(threshold, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.imshow("Image", threshold)
    cv2.waitKey(0)


parser = argparse.ArgumentParser()
parser.add_argument('-input', dest='input', help='path to dicom', type=str)
results = parser.parse_args()
Analyze(results.input)
