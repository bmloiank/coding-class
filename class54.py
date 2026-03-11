#data
string=[
    "0 0 1 0 0 0 0 0 0 0",
    "2 1 0 1 1 1 1 1 0 0",
    "0 1 0 0 1 0 0 1 0 0",
    "0 1 0 0 1 0 0 1 1 1",
    "1 1 0 2 1 0 0 0 0 0",
    "0 0 0 0 0 1 0 1 1 1",
    "1 1 1 0 1 0 0 0 0 0",
    "0 0 0 0 0 1 0 1 1 0",
    "1 1 1 0 1 1 1 1 0 1",
    "0 0 0 2 0 0 0 0 0 0",
]
 
data=[]
Polluted=3
for i in range(len(string)):
    data.append(list(map(int, string[i].split(" "))))
n=len(data)
m=len(data[0])
print(n, m)
 
print('--------초기 상태--------')
for i in data:
    print(i)
 
def find_safezone(map_data):
    count=0
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if(map_data[i][j]==0):
                count+=1
    return count
 
print(find_safezone(data))


# map->그래프로 해석적절하게 하기
# 0 빈공간
# 1 :환풍구(벽)
# 2 : 독성물질
# 3 : 오염구견


# (2) DFS탐색 => 함수
# - stack 구조 => 스택예제 ctrl+z / 이전페이지 / 재귀함수
# - node로 (i,j)순서상을 넣어주기
# - 입력 : 시작 2의 위치(i,j)

def dfs(node):
    # (1) 시작을 셋팅하기 - 초기 스택에 초기데이터를 넣어야한다.
    # x, y = node
    stack = []
    stack.append(node)
    # (2) stack이 빌때까지 반복해서 탐색을 진행한다.
    # - 방문여부 체크 : 0이 아닌걸로 체크
    # (2-1) 탐색한 애는 빼
    # (2-2) 뺀 노드의 위,아래,좌,우를 스택에 추가하기
    # - 0일때만 스택에 넣기
    
    while stack:
        x,y = stack.pop()
        # 내가 3이면 다음반복으로 넘어가기 
        if data[x][y] == 3:
            continue
        # 방문햇음 체크하기 3번으로 하기   
        if data[x][y] == 0:
            data[x][y] = 3
            
        # 위아래 좌우 탐색
        if x > 0 and data[x-1][y] == 0:
            stack.append((x-1, y))
        if x < len(data)-1 and data[x+1][y] == 0:
            stack.append((x+1, y))
        if y > 0 and data[x][y-1] == 0:
            stack.append((x, y-1))
        if y < len(data[i])-1 and data[x][y+1] == 0:
            stack.append((x, y+1))




# 독성물질이 어떻게 퍼질지 시뮬레이션 만들기
# (1) 각각의 2번 위치를 찾아라
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 2:
            print(i,j)
            dfs((i,j))
            # for a in data:
                #  print(a)
            # print("---")


# TODO: 재귀함수 바꾸기 => 과제


# def 함수(n):
#     if n<0:
#         return
#     자기이름(n-1)

#------------------------------------------------------

#data
string=[
    "0 0 1 0 0 0 0 0 0 0",
    "2 1 0 1 1 1 1 1 0 0",
    "0 1 0 0 1 0 0 1 0 0",
    "0 1 0 0 1 0 0 1 1 1",
    "1 1 0 2 1 0 0 0 0 0",
    "0 0 0 0 0 1 0 1 1 1",
    "1 1 1 0 1 0 0 0 0 0",
    "0 0 0 0 0 1 0 1 1 0",
    "1 1 1 0 1 1 1 1 0 1",
    "0 0 0 2 0 0 0 0 0 0",
]
 
data=[]
Polluted=3
for i in range(len(string)):
    data.append(list(map(int, string[i].split(" "))))
n=len(data)
m=len(data[0])
print(n, m)
for i in data:
    print(i)
 

# bfs:너비 우선 탑색 (가로)
# dfs:깊이 우선 탐색 (세로)
#  2 : 독성물질 기준으로 위,아래,좌,우 확산하기
# - 입력 : 행,열 좌표

def dfs(x,y):
    # 탈출조건1) 좌표 내에 있어야지만 되고, 좌표밖으로 나가면 그만... 탈출
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return
    # 탈출조건2) 벽(환풍기 1)전까지만 ... 탈출
    if data[x][y] == 1 or data[x][y] == 3:
        return
    if data[x][y] == 0:
        data[x][y] = 3

    print(x,y,data[x][y])
    dfs(x-1, y) # 위로
    dfs(x+1, y) # 아래로로
    dfs(x, y-1) # 왼쪽으로
    dfs(x, y+1) # 오른쪽으로



for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            x = i
            y = j
            print(x, y,"################")
            dfs(x,y)
            

for i in data:
    print(i)
 