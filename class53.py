#data
from math import atan2, sqrt
from math import pi
import matplotlib.pyplot as plt

 # 드론의 위치
point_list=[
    (-2, 2), (1, 1), (3, 3), (4, 2), (6, 4), (7, 3), (-1, -1), (1, -1), (2, -3), (5, -2)
]
 

 
for point in point_list:
    plt.scatter(point[0], point[1], color='black')
 
# 반시계인지 체크하는 함수
def isCounterclockwise(x1, y1, x2, y2, x3, y3):
    temp=x1*y2+x2*y3+x3*y1
    temp=temp-(x2*y1+x3*y2+x1*y3)
    if temp>0 :#반시계방향 회전
        return True
    elif temp<0 :#시계방향 회전
        return False
    else:#일직선
        return False
 
def find_origin(point_list_t):
    minIndex=[0]
    for i in range(1, len(point_list_t)):
        if point_list_t[i][1]<point_list_t[minIndex[0]][1]:
            minIndex.clear()
            minIndex.append(i)
        elif point_list_t[i][1]==point_list_t[minIndex[0]][1]:
            minIndex.append(i)
 
    if len(minIndex)==1:
        return minIndex[0], point_list_t[minIndex[0]]
    #y값이 같은게 있으면 그 중 x 값이 제일 작은 것을 return
    else:
        index=0
        for i in range(1, len(minIndex)):
            if point_list_t[i][0]<point_list_t[index][0]:
                index=i
        return index, point_list_t[index]
 
# point_list_t : 좌표순서쌍
# point_stack : stack
def draw_present_status(point_list_t, point_stack):
    x_values=[]
    y_values=[]
    for point in point_list_t:
        plt.scatter(point[0], point[1], color='black')
 
    for point in point_stack:
        x_values.append(point[0])
        y_values.append(point[1])
    plt.plot(x_values, y_values, color='green')
    plt.show()
 
#각도 구하기
angle_list=[]
 
#시작 좌표 찾기
origin_index, origin_point=find_origin(point_list)
for i in range(len(point_list)):
    dy=point_list[i][1]-origin_point[1]
    dx=point_list[i][0]-origin_point[0]
    angle_list.append(atan2(dy, dx)*180/pi)
 
 
#각도에 따라 포인트 정렬된 리스트 sorted_point_list
zipped_list=zip(angle_list, point_list)
sorted_zipped_list=sorted(zipped_list)
sorted_point_list=[element for _, element in sorted_zipped_list]



# 1. 각도순으로 정렬하기
# - 기울기를 통해 정렬 완료
# print("각도", angle_list)
# print("좌표", point_list)
# print(sorted_point_list)


# 2. 반시계로 돌아가면서 다각형을 만들기
# -> 스택에 넣어주기
# -> 초기스택은 점 2개를 넣고 
stack = [sorted_point_list[0], sorted_point_list[1]]

for i in range(2,len(sorted_point_list)):
    # 반시계인지 아닌지를 체크해야할 꼭짓점
    print(i, "꼭짓점",sorted_point_list[i])
    # 필요한 꼭짓점은 3개 => isCounterclockwise
    while True:
        spot1 = stack.pop()
        spot0 = stack.pop() # 먼저들어간 값
        isClock = isCounterclockwise(spot0[0], spot0[1], spot1[0], spot1[1], sorted_point_list[i][0], sorted_point_list[i][1])
        print(isClock)
        if isClock == True:
            stack.append(spot0)
            stack.append(spot1)
            stack.append(sorted_point_list[i])
            print(stack)
            break
        else :
            # 반시계가 아니면 spot1 날리고, spot0저장하다음에 다시 3꼭짓점의 반시계 여부를 체크
            stack.append(spot0)
           
# 시작점을 연결하기
stack.append(sorted_point_list[0])
print(stack)



