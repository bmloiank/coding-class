'''
파이썬 : 데이터를 잘 다루는 특화된 프로그래밍언어


컴퓨터 비전 computer vision => opencv
이미지나 비디오를 다루는 방법

1. cv2 모듈을 설치
pip install opencv-python

import cv2
print(cv2.__version__)


2. 


'''
import cv2
print(cv2.__version__)

# (1) 이미지 읽어오기
# 이미지 = cv2.imread("파일경로", 옵션)
# 옵션 : 원본 cv2.IMREAD_UNCHANGED(기본값)
#       그레이스케일(흑백) cv2.IMREAD_GRAYSCALE  
#       RGB 스케일 줄이기 cv2.IMREAD_REDUCED_COLOR_2
#       cv2.IMREAD_ANYDEPTH
# cv2.imshow("창이름",이미지)

image = cv2.imread('data/opensea.jpg',cv2.IMREAD_GRAYSCALE)


# (2) 이미지 정보
# - 높이,너비,채널 이미지.shape
# 색의 삼원색 => 물감
# 빛의 삼원색 => 모니터 RGB => 채널
# h,w,c = image.shape
# FF/FF/FF : 흰색(RGB 가장 잘 ) 16*16 = 0-255(256개)
# 000000 : 검은색(빛이 없음)





# Red변경하기 : 
# cvtColor(이미지, cv2.COLOR_BGR2HSV)
# 
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# image 컬러를 직접변경하기 RGB
# 이미지이름[:,:,0]=0 # Blue
# 이미지이름[:,:,1]=0 # Green
image[:,:,0]=0
# image[:,:,1]=0
image[:,:,2]=0
cv2.imshow('심해', image)
print(image.shape)


# cv2.waitKey() : 창유지
# cv2.destroyAllWindows() : 키보드누르면 종료
cv2.waitKey(10000)
cv2.destroyAllWindows()