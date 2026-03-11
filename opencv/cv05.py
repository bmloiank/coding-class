import cv2

lenna = cv2.imread('data/Lenna.png', cv2.IMREAD_GRAYSCALE)

# lenna = cv2.imread('data/Lenna.png')


# 컬러영상을 채널분리
# Red img BGR : 모든이진배열 다
# 이미지[:,:,2] 
# print(lenna)
# cv2.imshow(윈도우이름, 이미지)
cv2.imshow('hhh', lenna)

# 채널 - 컬러채널 RGB(0-255,0-255,0-255)
#     - 흑백채널 단일채널 0-255 숫자
# cv2.imshow('hhh', lenna[:, :, 0])

# 이진화 : 0 또는 1 => 오츄알고리즘
# 임계점, 이미지 = cv2.threshold(이미지,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
spot, image = cv2.threshold(lenna, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(spot)
cv2.imshow('hhh', image)















cv2.waitKey()
cv2.destroyAllWindows()