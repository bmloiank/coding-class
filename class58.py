# 누리호 4차
# pandas
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('./data/cctv1.csv')
print(data)

# 주제가 각 cctv별 유동인구
# no :
# camera_code : cctv 번호
# camera_name : cctv 이름 => 위치
# 06-12 : 시간별 유동인구수
# 12-18(낮)
# 18-24(밤) 

# print(data[['camera_name', ]])
print(data[['camera_name', '12_18', '18_24']])

# 데이터프레임.sort_values(by="기준컬럼",ascending=T/F)
print(data.sort_values(by='12_18', ascending=False))
data1 = data.sort_values(by='12_18', ascending=False)

print(data1.head(3)['camera_name'])
print(data1.head(3)['camera_name'].tolist())

print('===============')
data2 = data.sort_values(by='18_24', ascending=False)
print(data2)
# 데이터프레임 -> 리스트 변환 : df.tolist()
print(data2.head(3)['camera_name'])
print(data2.head(3)['camera_name'].tolist())


# 두값의 평균을 새로운 컬럼으로 만들어서 비교하기
# (1) 평균 컬럼avg을 새로 만들어보기숫자는 0으로 넣어주세요.
# (2) 12-18 18-24의 값의 평균
data['avg'] = (data['12_18'] + data['18_24'])/2
# (3) 평균값으로 정렬된 상위 3개 출력
print(data.sort_values(by='avg',ascending=False))
l = data.sort_values(by='avg',ascending=False).head(3)['camera_name'].tolist()

for i in range(len(l)):
    print(l[i])



print("=========================================")
# 그림을 좌표 밑에 깔고, 그위에 그래프를 그릴다. 
# -> 산점도 

pile = pd.read_csv('./data/spotcover.csv')
print(pile)
x = pile['x']
y = pile['y']
size = pile['cover']

# 그래프에 이미지 배경을 깔기
# (1) 이미지르 읽어고 plt.imread("파일경로")
# (2) 이미지를 그래프에 보여주기 plt.imshow(이미지변수, extent=[x시작,x끝, y시작,y끝])
# - 0~1200 0 1100
img = plt.imread('./data/map.png')
plt.imshow(img, extent=[0,1200,0,1100])
# 산점도 plt.scatter(x,y, size, alpha=0-1)
plt.scatter(x, y, s=size, alpha=0.5)
plt.show()

# KATWIJKSTRAAT