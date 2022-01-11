import cv2

image = cv2.imread('data/images/book2.jpg')

print(image.shape)

cv2.imshow('original',image)

#회전시킬 이미지를 만들기 위한 정보 세팅
center = (image.shape[1]/2,image.shape[0]/2)#1은 x 좌표, 0은 y 좌표
rotationAngle = 70
scaleFactor = 1

#회전 시킬수 있는 행렬을 먼저 얻어와야한다.
matrix = cv2.getRotationMatrix2D(center,rotationAngle,scaleFactor)

print(matrix)

#회전시킬수 있는 행렬을 얻어왔으니, 이 행렬로 변환하라는 함수를 호출하면 된다
result = cv2.warpAffine(image,matrix,(image.shape[1],image.shape[0]))
cv2.imshow('rotation',result)

cv2.waitKey(0)
cv2.destroyAllWindows()