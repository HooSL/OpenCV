import cv2
import numpy as np

image = cv2.imread('data/images/truth.png')

cv2.imshow('original',image)

#이미지 확장 : dilation

dilationSize = 6

element = cv2.getStructuringElement(cv2.MORPH_RECT,#사각형으로 키운다
                        (2*dilationSize,2*dilationSize))

imageDilate = cv2.dilate(image,element)

cv2.imshow('dilation',imageDilate)


cv2.waitKey(0)
cv2.destroyAllWindows()