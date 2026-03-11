# 데이터분석전문가
# 데이터를 분석 => 차트, 도식화  

# 공공데이터 

# 주피터 노트북 jupyter ------------


'''
그래프 그리는 모듈
1. matplotlib (https://matplotlib.org/stable/index.html)


2. plotly


공공데이터포탈(https://www.data.go.kr/)
'''

# <설치>
# pip install matplotlib
# pip install numpy

import matplotlib.pyplot as plt
import numpy as np  # 수치

# 데이터
x = [1,2,3,4,5]
y = [1,2,3,4,5]
y2 = [2,3,4,5,1]

# 그래프 그리기 - 
# 기본그래프 선 그래프 plot
plt.plot(x,y, marker='o', color="red", linestyle=":", label="라벨")
plt.plot(x,y2, marker='o', color="blue", linestyle=":", label="라벨2")
# linestyle : 실선 -  파선-- 점선:
# marker o s ^ *
plt.title("차트제목")
plt.xlabel("x축라벨")
plt.xlim(left=0) #x축을 0부터 시작하겠다.
plt.ylabel("y축라벨")
plt.ylim(bottom=0) #y축을 0부터 시작하겠다.
plt.xticks(np.arange(0,12),labels=["1월","2월","3월","4월","5월",'6월',"7월","8월","9월","10월","11월","12월"])
plt.yticks(np.arange(0,5.4,0.5))

plt.legend()  # 범례 표시하기 
plt.grid(True) # 그리드 표시

plt.show()


# -------------------------
# y=2x+1
x = np.arange(0,255,0.1)

plt.scatter(x,2*x+1, s=x*20, c=x**2, alpha=0.5)
# 다음시간에

# -------------------------
# 막대르
x=["짱구","유리","철수","훈이","맹구"]
y=[50,60,100,30,75]
plt.bar(x,y, color="", edgecolor="", linewidth=2, width=10)

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False 


#----------------------
# 원형차트 pie
plt.pie(y,labels=x,colors=[red,orange,,,],shadow=10,  wedgeprops={'width':0.5}, explode=[0.1,0,0,0,0])



https://matplotlib.org/stable/index.html


from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import art3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
wire = ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# Retrive data from internal storage of plot_wireframe, then delete it
nx, ny, _  = np.shape(wire._segments3d)
wire_x = np.array(wire._segments3d)[:, :, 0].ravel()
wire_y = np.array(wire._segments3d)[:, :, 1].ravel()
wire_z = np.array(wire._segments3d)[:, :, 2].ravel()
wire.remove()

# create data for a LineCollection
wire_x1 = np.vstack([wire_x, np.roll(wire_x, 1)])
wire_y1 = np.vstack([wire_y, np.roll(wire_y, 1)])
wire_z1 = np.vstack([wire_z, np.roll(wire_z, 1)])
to_delete = np.arange(0, nx*ny, ny)
wire_x1 = np.delete(wire_x1, to_delete, axis=1)
wire_y1 = np.delete(wire_y1, to_delete, axis=1)
wire_z1 = np.delete(wire_z1, to_delete, axis=1)
scalars = np.delete(wire_z, to_delete)

segs = [list(zip(xl, yl, zl)) for xl, yl, zl in \
                 zip(wire_x1.T, wire_y1.T, wire_z1.T)]

# Plots the wireframe by a  a line3DCollection
my_wire = art3d.Line3DCollection(segs, cmap="hsv")
my_wire.set_array(scalars)
ax.add_collection(my_wire)

plt.colorbar(my_wire)
plt.show()



# pip install pandas
# 이차원리스트 데이터타입을 잘 다루기위한 모듈
import pandas as pd


# csv를 읽어오기
# 판다스에서는 이차원리스트 dataframe df

data = pd.read_csv('./sample.csv')

x = data['구분']
y = data['전체 인구수(외국인 제외)']
plt.figure(figsize=(width,height))
plt.plot(x,y)
plt.show()













