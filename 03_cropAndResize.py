import cv2
import numpy as np

#cv2.IMREAD_COLOR 랑 1은 같은 의미입니다
source = cv2.imread('data/images/sample.jpg',1)

print(cv2.IMREAD_COLOR)

#가로는 80%
#세로는 60%
#이미지 확대 / 축소

scaleX = 0.8
scaleY = 0.6 #확대는 1.6,1.2 이렇게 하면 된다.

scaleDown = cv2.resize(source,None,fx=scaleX,fy=scaleY,interpolation=cv2.INTER_LINEAR) #fx,fy는 바로 0.8,0.6으로 적어줘도 된다. , INTER_LINEAR 비어있는 데이터는 양옆 데이터의 평균으로 채워라

print(scaleDown)

cv2.imshow('Original',source)
cv2.imshow('Scaled Down',scaleDown)


#CROP 이미지 자르기

crop_img = source[10:200,100:250]

cv2.imshow('crop img',crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
