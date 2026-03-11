import cv2
import numpy as np
lenna = cv2.imread('data/Lenna.png')

# 이미지.shape 속성
# h,w,c
print(lenna.shape)

# cv2.rectangle(이미지,(시작x,시작y),(끝x,끝y), 색상(B,G,R), 두께
# 색상 : 0-255(256가지)
# cv2.circle(이미지,(중심x,y),반지름 색상(B,G,R), 두께)
# cv2.ellipse(이미지, (중심x,y),(긴축길이, 짧은축길이), 회전, 시작각도, 끝각도, 색상, 두께)
cv2.rectangle(lenna, (1,30),(100, 100), (0, 0, 100), 2)
cv2.circle(lenna, (250, 250), 100, (200, 0, 0), 2)
cv2.ellipse(lenna, (250, 250), (150, 90), 0, 0, 360, (0, 200, 200), 2)

# 선 line(이미지,(시작x,시작y),(끝x,끝y), 색상(B,G,R), 두께)
# 다각형선 polylines(이미지, [점3개이상 리스트], 닫힌True/열린False , 색상, 두께)
# 다각형채우기 fillPoly(이미지, [점3개이상 리스트], 색상, 두께)
cv2.line(lenna, (0,100), (512,100),(255, 200, 255), 2)
# numpy배열 np.array(리스트)
t = np.array([(100,100), (0,200), (200,200)])
cv2.polylines(lenna, [t], False, (150, 230, 0), 2)
cv2.fillPoly(lenna, [t], (150, 230, 100))




# 마우스로 찍은 위치를 기준으로 다각형을 그리기
# 마우스 처리용함수 => 이벤트 
# 함수(event,x,y,flag,param)
drawing = False
left_x = 0
left_y = 0
right_x = 0
right_y = 0

def destroy(event, x, y, flags, param):
    # global 변수 처리 => 전역변수
    # global 변수이름,변수,변수,변수
    global left_x, left_y, right_x, right_y, drawing, lenna
    # event가 cv2.EVENT_LBUTTONDOWN / EVENT_RBUTTONDOWN: 마우스 왼쪽버튼 클릭인가?
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽클릭', x, y)
        left_x, left_y = x, y
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('우클릭', x, y)
        right_x, right_y = x, y
        drawing = True
    
    if drawing == True:
        drawing = False
        print(left_x,left_y,right_x,right_y)
        cv2.rectangle(lenna, (left_x, left_y), (right_x, right_y), (200, 255, 120), 7)
        cv2.imshow('hhh', lenna)


# imshow("윈도우창이름",이미지)
cv2.imshow('hhh', lenna)
# cv2.setMouseCallback("윈도우창", 함수이름)
cv2.setMouseCallback('hhh', destroy)








cv2.waitKey()
cv2.destroyAllWindows()