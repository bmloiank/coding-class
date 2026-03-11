'''
cv2 

(1) 이미지 읽기
cv2.imread("파일경로",옵션)
- cv2.IMREAD_UNCHANGED : 원본 사용
- cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
- cv2.IMREAD_COLOR : 3 채널, BGR 이미지 사용

(2) 이미지 출력하기
cv2.imshow("윈도우 이름",변수)
cv2.waitKey()
cv2.destroyAllWindows()

(3) 이미지 정보 출력
세로,가로,채널=이미지.shape

(4) 이미지 픽셀 한개 :픽셀 리스트[B,G,R] => 이차원리스트 i행 j열
# 100행 100열

색상하나 0-255 => 대학생 교양수업 카메라 
'''

import cv2

image = cv2.imread('data/opensea.jpg', cv2.IMREAD_COLOR)
print(image)

# 이미지 타입을 체크 type(데이터)
print(type(image))
# cv2.imshow('WINDOW', image)
print(image.shape)
# width
w,h,c = image.shape
# 배열 = 리스트
print(w,h,c)
print(image[:10][:10]) # [b97 g72 r30]


'''
(5) 확대/축소
cv2.pyrUp(이미지)  # 2배        # 업샘플링
cv2.pyrDown(이미지) # 1/2배 축소 # 다운샘플링-> 노이즈부분을 줄이면서 축소

cv2.resize(이미지,dsize=(원하는 절대사이즈 사이즈)) # 절대사이즈로 조절하기
cv2.resize(이미지,dsize=(0,0),fx=0.7, fy=0.6) # 비율로 조절하기
'''
print(image.shape)
image_sizeup = cv2.pyrUp(image)
# cv2.imshow("윈도우 이름",변수)
# cv2.imshow('window', image_sizeup)
print(image_sizeup.shape)
image_sizedown = cv2.pyrDown(image)
# cv2.imshow('window', image_sizedown)
print(image_sizedown.shape)
image_resize = cv2.resize(image, dsize=(500,500))
# cv2.imshow('window', image_resize)
image_resize = cv2.resize(image, dsize=(0,0), fx=0.7, fy=3)
# cv2.imshow('window', image_resize)

'''
(6) 이미지에 도형그려보기
# 사각형 그리기
cv2.rectagnle(이미지,(왼쪽상단x1,y1),(x2,y2), 컬러(B,G,R), 선두께)
x1y1        x2y1
x1,y2       x2y2

# 마우스로

'''
cv2.rectangle(image, (50,50), (500, 300), (0,0,225), 5)
cv2.imshow('window', image)

cv2.waitKey()
cv2.destroyAllWindows()