import cv2
import sys

# https://github.com/opencv/opencv/tree/master/data/haarcascades
# https://cdn.polinews.co.kr/news/photo/201903/384034_1.jpg


# (1)이미지 읽어오기
# (2) 학습모델일 가져오기 
# 모델명 = cv2.CascadeClassifier("경로")
face = cv2.imread('data/face.png')
family = cv2.imread('data/family.jpg')
mface = cv2.CascadeClassifier("data/haarcascade_frontalface_alt.xml")

# (3) 사람얼굴을 인식할려면 = > 그레이스케일로 변환
# cv2.cvtColor(이미지, cv2.COLOR_BGR2GRAY) 
face1 = cv2.cvtColor(family, cv2.COLOR_BGR2GRAY)

# (4) 얼굴감지
# 모델명.detectMultiScale(
#   그레이스케일이미지,
#   scaleFactor=1.05, # 숫자가 클수록 정확도가 낮음 속도가 빠름
#   minNeightbor=5,  # 얼굴 정확도 많으면 매우 정확
#   minSize=(30,30)
# )
face2 = mface.detectMultiScale(face1, scaleFactor=1.05, minNeighbors=9, minSize=(30,30))
print(face2)

# (x,y,가로,세로)
# cv2.rectangle(이미지, (x1,y1),(x2,y2))
for i in range(len(face2)):
    x, y, w, h = face2[i]
    cv2.rectangle(family, (x, y), (x+w, y+h), (0,0,225), 3)

cv2.imshow('hhh', family)


# (5) 비디오 읽기
# 영상 = cv2.VideoCapture("파일경로")
# 영상.isOpened() => False이면 print("x")
video = cv2.VideoCapture('data/sample.mp4')
if not video.isOpened():
     print('X')

# (6) 반복해서 프레임읽이
# while True :
# 성공여부, 프레임 = 비디오.read()
# 성공이 false break

while True:
    suc, frame = video.read()
    if not suc:  # 장면이 반복되다가 끝나면 false
        print('X')
        break
    print("O")
     # (7) 그레이스케일로 변환
     # (8) 얼굴탐지
     # (9) 사각형 씌워서 프레임 보여주기
    video2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face2 = mface.detectMultiScale(video2, scaleFactor=1.05, minNeighbors=9, minSize=(30,30))
    for i in range(len(face2)):
        x, y, w, h = face2[i]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,225), 3)
    cv2.imshow('fff', frame)
    

cv2.release()
cv2.destroyAllWindows()