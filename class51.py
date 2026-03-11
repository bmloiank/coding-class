# cctv 여러개 존재하고 그중에서 사각지대를 찾기


#data
#initial condition
camera_list=[]
map_data=[]
# 0 : 빈 공간
# 1~ 5: 카메라 위치
# - 1 : 위아래 감시
# - 2 : 좌우 감시
# - 3 : 우상좌하 감시
# - 4 : 좌상우하 감시
# - 5 : 모든방향
# 6 : 벽 
# => 탐색가능한 지역은 7번으로 변경

map_string=[
    "2 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 6 6 6 6",
    "6 6 6 6 6 6 6 6 6 6 6 6 6 0 6 0 6 0 0 0",
    "1 0 0 0 0 0 0 6 0 0 0 0 6 0 6 0 0 0 5 0",
    "0 6 5 0 0 5 0 6 0 5 0 0 6 0 6 0 6 0 0 0",
    "0 6 0 0 0 0 0 6 0 0 0 1 6 0 6 0 6 2 0 0",
    "0 6 0 0 0 0 0 6 2 0 0 0 6 0 6 0 6 6 6 6",
    "0 6 6 6 6 6 6 6 0 0 0 0 6 0 6 0 0 0 0 2",
    "0 0 0 0 0 0 0 0 0 0 0 2 6 0 0 0 6 6 6 6",
    "0 0 5 0 0 5 0 0 0 5 0 0 6 0 6 0 6 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 6 0 6 0 6 0 5 0",
    "6 6 6 6 0 0 6 6 6 6 6 6 6 0 0 0 6 0 0 0",
    "0 5 0 6 0 0 6 0 0 0 2 0 0 0 6 0 6 0 5 0",
    "0 0 0 0 0 0 6 4 0 0 0 0 0 0 6 0 6 0 0 0",
    "0 5 0 0 0 0 6 0 0 0 0 5 0 0 6 2 0 0 0 0",
    "0 0 0 6 0 0 6 0 5 0 0 0 0 0 6 0 6 0 5 0",
    "3 0 0 6 0 1 6 0 0 0 4 0 0 3 6 1 6 0 0 0"
]

# 리스트 축약형 => for문 쓰시고 append사용하면 된다.
# 변수이름 = [넣을값 for 반복조건]
map2 = [list(map(int, map_string[i].split(' '))) for i in range(len(map_string))]


# 조건문 if문 + match ~ case:
# match(변수): 하나의 변수기준으로 경우 3.10버전기준으로 생겼다.
# match 변수조건:
#     case 조건1:
#         코드
#     case 조건2:
#         코드


# 함수로 만들기
# - 캠위치(행,열, 캠번호) 받았을때,
# - map2 에 감시가능한 위치를 7로 변경하기

def direction(i, j, cam_num):
    # 카메라 번호를 기준으로 7을 만들어주기
    match cam_num:
        case 1:
            # (1-1)위체크
            up(i, j)
            # (1-2)아래체크 
            down(i, j)
            
        case 2:
            # (2-1) 좌체크
            left(i, j)
            # (2-2) 우체크
            right(i,j)
        case 3:
            # y=x그래프^^
            # (3-1) 
            upright(i,j)
            # (3-2) 왼쪽아래대각서 
            downleft(i,j)
            
        case 4: 
            # y=-x그래프^^
            # (4-1) 왼쪽위대각선
            upleft(i,j)
            # (4-2) 오른쪽아래대각서 
            downright(i,j)
            
        case 5: 
            # (1-1)
            up(i, j)
            # (1-2)
            down(i, j)
            # (2-1)
            left(i, j)
            # (2-2)
            right(i,j)
            # (3-1)
            upright(i,j)
            # (3-2)
            downleft(i,j)
            # (4-1)
            upleft(i,j)
            # (4-2)
            downright(i,j)
            
    



# (1-1) 
def up(i, j):
    # - (i,j)값이 6이 아니면 타고 올라기
    # - 행번호 i>0 크면 타고 올라가기
    # - 카메라가 나오면 넘어가기 

    while i >= 0 and map2[i][j] != 6 :
        # (i,j) 값이 카메라번호가 아니라면 7로 바꾸기
        # if not ( 1 <= map2[i][j] <= 5 ):
        if map2[i][j] not in list(range(1,6)):
            map2[i][j] = 7
        i = i-1

# (1-2)
def down(i, j):
    # - (i,j)값이 6이 아니면 타고 올라기
    # - 행번호 마지막 인덱스번호10 일때까지 가능
    # - 카메라가 나오면 넘어가기 
    while i <= len(map2)-1 and map2[i][j] != 6:
        if map2[i][j] not in list(range(1,6)):
            map2[i][j] = 7
        i = i+1

# (2-1) 
def left(i, j):
    while j >= 0 and map2[i][j] != 6 :
        if map2[i][j] not in list(range(1,6)):
            map2[i][j] = 7
        j = j-1

# (2-1) 
def right(i, j):
    while j <= len(map2[i])-1 and map2[i][j] != 6 :
        if map2[i][j] not in list(range(1,6)):
            map2[i][j] = 7
        j = j+1


# (3-1)
def upright(i, j):
    while i >= 0 and j <= len(map2[i])-1 and map2[i][j] != 6 :
        if map2[i][j] not in list(range(1,6)):
            map2[i][j] = 7
        i = i-1
        j = j+1

# (3-2)
def downleft(i, j):
    while i <= len(map2)-1 and j >= 0 and map2[i][j] != 6 :
        if map2[i][j] not in list(range(1,6)):
            map2[i][j] = 7
        i = i+1
        j = j-1

# (4-1)
def upleft(i, j):
    while i >= 0 and j >= 0 and map2[i][j] != 6 :
        if map2[i][j] not in list(range(1,6)):
            map2[i][j] = 7
        i = i-1
        j = j-1

# (4-2)
def downright(i, j):
    while i <= len(map2)-1 and j <= len(map2[i])-1 and map2[i][j] != 6 :
        if map2[i][j] not in list(range(1,6)):
            map2[i][j] = 7
        i = i+1
        j = j+1





#--------- 실행 함수 -------------------
for i in range(len(map2)):
    for j in range(len(map2[i])):
        # print(row[j],end="")
        if 1 <= map2[i][j] <= 5:
            direction(i, j, map2[i][j])
        

for i in range(len(map2)):
    print(map2[i])


count = 0
for i in range(len(map2)):
    for j in range(len(map2[i])):
        if map2[i][j] == 0:
            count = count+1

print(count)




