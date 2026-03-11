# 카메라
import cv2


# 카메라와 연결 시도
# 캠 = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam = cv2.VideoCapture(0, cv2.CAP_ANY)
# 캠의 해상도를 낮추기
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cam.set(cv2.CAP_PROP_FPS, 30)

# 만약에 캠이 열려있지 않으면 print()
# cam.isOpened() : 캠이 열려있는지 체크
if not cam.isOpened():
    print('X')
    exit()



while True:
    # 상태, 프레임 = 캠.read()
    # 상태 : 정상이면 True 아니면 Fals 
    # cv2.imshow("윈도우창이름", 프레임)
    flag, frame = cam.read()
    print(flag)
    # cv2.imshow('hhh', frame)



    # 키보드 누름 기다림 키= cv2.waitKey(1)
    # 만약에 key가 있으면 break;
    key = cv2.waitKey(1)
    if key != -1:
        break



# cv2.waitKey()
# cam.release()
# cv2.destoryAllWindows()

cam.release()
cv2.destroyAllWindows()





