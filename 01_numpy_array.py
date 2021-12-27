import cv2
import numpy as np

# 넘파이 복습
# 1차원 배열
arr = np.array([5,10,15])
print(arr)
print(arr.shape)
print(arr[0])
#데이터 변경
arr[1] = 50
print(arr)

# 2차원 배열
array_2d = np.array([5,6,1,2,9,10])
array_2d=array_2d.reshape(3,2)
print(array_2d)

# 2차원 배열의 데이터 엑세스
# 두번째행의 두번째열의 데이터를 엑세스
print(array_2d[1,1])

# 이미지 파일을 읽어오는 방법
img = cv2.imread('data/images/sample.jpg')
print(img)
print(img.shape)
print(img.ndim)

# 이미지 파일을 그레이스케일로 읽어오는 방법
img2 = cv2.imread('data/images/sample.jpg',0)
print(img2)
print(img2.shape)
print(img2.ndim)
