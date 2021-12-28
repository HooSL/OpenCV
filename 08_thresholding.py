import cv2
import numpy as np

image = cv2.imread('data/images/truth.png')

#구분 값을 먼저 설정
thresh = 255
#위의 특정값보다 큰 값들은 모두 255로 변경
maxValue = 255

cv2.imshow('Original',image)

#쓰레숄딩 적용된 이미지 만들기
th,dst = cv2.threshold(image,thresh,maxValue,cv2.THRESH_BINARY)

cv2.imshow('thresholded image',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()