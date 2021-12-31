import cv2
import numpy as np

image = cv2.imread('data/images/opening.png')

cv2.imshow('original',image)

openingSize = 3

element = cv2.getStructuringElement(cv2.MORPH_RECT,
                                    (2*openingSize,2*openingSize))

imageOpened = cv2.morphologyEx(image,cv2.MORPH_ELLIPSE,element,
                                iterations=5)

cv2.imshow('open',imageOpened)


cv2.waitKey(0)
cv2.destroyAllWindows()