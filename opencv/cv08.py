# 
import cv2
import sys
# (1) 캠 = cv2.VideoCapture(0)
# (2) 캠.isOpened() 캠캠쳐 준비가 되어있는지?
# 
cam = cv2.VideoCapture(0)
if cam.isOpened():
    print('O')
else:
    print('X')
    sys.exit()

# (3) 프레임받아오기
# while True:
# 성공여부, 이미지 =캠.read()
while True:
    suc, image = cam.read()
    # 성공이 아니면 break
    if suc == False:
        print('X')
        break
    
    # cv2.imageShow


cam.release() # 사용한 자원 해제
cv2.destroyAllWindows()


https://076923.github.io/assets/posts/C-Sharp/OpenCvSharp2/lecture-29/1.webp