from PIL import Image
import pytesseract
import cv2
import numpy as np

def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    gearImage = cv2.imread('testImage.png')

    hsv = cv2.cvtColor(gearImage, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 0, 60])
    upper = np.array([0, 0, 255])

    result = cv2.inRange(hsv, lower, upper)

    cv2.imshow('mask', result)
    cv2.waitKey(0)


    result = pytesseract.image_to_string(result)
    
    print(result)

main()
