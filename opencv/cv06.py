import cv2 
import numpy as np

ss = cv2.imread('data/screenshot.png', cv2.IMREAD_GRAYSCALE)

# (1) 픽셀 모든 값이 100 더학
# for i in range(len(ss)):
#     for j in range(len(ss[i])):
#         ss[i][j] += 100


# (2) 흰색부분만 골라서 밝게 처리 하기
# => 마스크 필터링 
# => np 1로 채우기 np.ones((세로,가로),int)
# => 이미지 = ㅊ
mask = np.ones((10, 10),int)
image = cv2.dilate(ss, mask, iterations=2)
cv2.imshow('hhh', image)

cv2.imshow('원본',ss)


cv2.waitKey()
cv2.destroyAllWindows()


