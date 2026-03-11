# 섬의 갯수 https://www.acmicpc.net/problem/4963
# 재귀 깊이를 조정하기
# import sys
# sys.setrecursionlimit(10**4)
import sys
sys.setrecursionlimit(10**4)


m = []
# 8방위:  위,아래,좌,우,상 좌, 상 우, 하 좌, 하 우
my = [-1,1,0,0,-1,-1,1,1]
mx = [0,0,-1,1,-1,1,-1,1]
# 탐색예정 -> stack 재귀함수
# 방문완료 -> map 제3의 숫자로 변경할것 - 5
def dfs(y, x):
    if m[y][x] != 1:
        return 
    # 탐색 그만조건 => map 1 아닐조건
    m[y][x] = 5
    
    for i in range(8):
        ny = y + my[i]
        nx = x + mx[i]
        # 리스트 범위에 대한것
        # 탐색가능 데이터에 대한 1일때만 넣기
        if 0 <= ny < h and 0 <= nx < w and  m[ny][nx] == 1:
        # 0~ 끝번호 포함사이에  
        # 현재꺼에서 판단할거면 포함X => 다음거 nx,ny
            dfs(ny, nx)


# 0 0 이 나올때까지 반복해서 지도의 사이즈/지도 내용을 받을 겁니다.
while True:
    w, h = list(map(int, input().split()))
    if (w, h) == (0, 0):
        break
    m = []
    for i in range(h):
        m.append(list(map(int, input().split())))
    
    count = 0
    # 1을 발견 하면 탐색시작하기
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                y = i
                x = j
                dfs(y, x)
                count += 1
    print(count)
    
    

# 숫자 타자연습 1월목표 - 열손가락 화면보면서 치기
# - 한타 200타(애국가)
# - 영타 ABC송 (열손가락 100타)

