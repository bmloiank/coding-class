'''
노이즈 만들기 - 가우시안 노이즈

'''
# (1) cv2.imread("경로")
import cv2
import numpy as np
lenna = cv2.imread('data/Lenna.png', cv2.IMREAD_GRAYSCALE)
h, w = lenna.shape

def noise_maker(h,w,p):
    # 가우시안 난수 생성해서 : 이미지사이즈와 같이 난수 생성
    # np.zeros((행,열))zero로 채워진 numpy
    noise = np.zeros([h, w])
    # 가로 세로에따라서 노이즈를 랜덤하게 지정하기
    for i in range(h):
            # noise[행]
        for j in range(w):
            noise[i][j] = np.random.normal(0, p)
            lenna[i][j] += noise[i][j]
            # noise[i][j] += lenna[i][j]
            # print(noise[i][j],lenna[i][j])
            # 노이즈필터를 lenna 적용 => 픽셀값을 바꾸겠단 소리


noise_maker(h,w,20)

#  노이즈 제거 ------------------
# (1) 블러 처리 cv2.blur(이미지,(블러사이즈h,w))
lenna_blue = cv2.blur(lenna, (5, 5))
# (2) 가우시안 블러  cv2.GaussianBlur(이미지, (사이즈), 강도)
lenna_blue1 = cv2.GaussianBlur(lenna, (5, 5), 3)
# (3) 미디언 블러 cv2.medianBlur(이미지, 평균)
lenna_blue2 = cv2.medianBlur(lenna, 5)
# (4) 양방향 필터 cv2.bilateralFilter(이미지, 강도, 밝기, 범위 )
lenna_blue3 = cv2.bilateralFilter(lenna, 5, 75, 75)


cv2.imshow('hhh1', lenna)
cv2.imshow("blur",lenna_blue)
cv2.imshow("ggg",lenna_blue1)
cv2.imshow("mmm",lenna_blue2)
cv2.imshow("bbb",lenna_blue3)
# cv2.imshow('hhh2', noise)
cv2.waitKey()
cv2.destroyAllWindows()


