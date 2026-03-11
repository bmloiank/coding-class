#data
string = [
   "0 0 1 0 0 0 0 0 0 0",
   "0 1 0 1 1 1 1 1 0 0",
   "4 1 3 0 0 0 0 1 0 0",
   "0 1 0 0 1 0 0 1 1 1",
   "0 1 1 1 1 0 0 0 0 3",
   "0 0 0 0 0 1 0 1 1 1",
   "1 1 1 1 0 0 0 0 0 0",
   "0 0 0 0 0 1 0 1 0 0",
   "1 1 0 0 1 1 1 1 0 1",
   "1 0 0 0 0 3 0 1 0 0",
]
 
map_data=[]
robot_list=[]
# 탐색 범위 리스트
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# n, m=map(int, input().split())
for i in range(len(string)):
    map_data.append(list(map(int, string[i].split(" "))))
   
for i in map_data:
    print(i)
print()

# bfs 만들어보기
def bfs(y, x):
    queue=[]
    # 0으로 채워진 2차원리스트
    visited = [[0 for j in range(len(map_data[i]))] for i in range(len(map_data))]
    
    queue.append((y, x))
    visited[y][x] += 1
    # 빌때까지 탐색을 한다. 
    # (1) 하나뽑기
    # (2) 0일때만 1올려서 방문처리하기
    while queue:
        # 변수 다중할당 - 리스트, 튜플 여러개를 변수에 바로 저장하
        py, px = queue.pop(0)
        # print("현재",(py,px))
        # TODO: 방문처리후 탐색이어서... 도전해보면 좋구 안되면 같이 하기~*^^* 
        # visited[py][px] += 1
        # 위/아래/좌/우을 체크하기
        for i in range(4):
            # 예정 좌표를 찾기
            # print((py + dy[i], px + dx[i]))
            # 해당좌표가 유효한지 체크하고 넣기
            ny = py + dy[i]
            nx = px + dx[i]
            if ny >= 0 and ny <= len(map_data)-1 and nx >= 0 and nx <= len(map_data)-1:
                if visited[ny][nx] == 0 and map_data[ny][nx] != 1 and map_data[py][px] != 4:
                    # print((ny,nx))
                    queue.append((ny,nx))
                    visited[ny][nx] = visited[py][px] + 1
    
    print(visited[2][0]-1)

    # for i in range(len(visited)):
    #     print(visited[i])

    
        



# 로봇이 독성 물질까지 가장 빠르게 도착하는 거리를 찾아라.
for i in range(len(map_data)):
    for j in range(len(map_data[i])):
        if map_data[i][j] == 3:
            y = i
            x = j
            print(y, x)
            bfs(y, x)


'''
# 아래,위,우,좌

(2,5)
'''






