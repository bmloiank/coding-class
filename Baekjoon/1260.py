# 그래프 탐색>

# (1)BFS(너비우선탐색)

# (2)DFS(깊이우선탐색)


# DFS와 BFS https://www.acmicpc.net/problem/1260
# *변수의 다중할당 : 리스트의 요소 갯수만큼 변수를 할당하고싶다.
# 변수1,변수2,변수3.. = 리스트

# n 노드(node)의 갯수 / m: 엣지의 갯수 / v 시작번호
# map(변환함수이름, 데이터)

# 1. 그래프초기화 : 그래프를 생성하고, 연결상태 초기화
# - n+1*n+1 이차원리스트를 0으로 채워서 만들어주기 => 리스트의 축약형
# - 변수이름 = [넣을 값 for i in range(조건)]
# 2. 그래프 엣지를 체크하기 : 연결되면 1 안되면 0으로 표시해보기

from collections import deque

n, m, v = list(map(int, input().split(' ')))
graph = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    # 두  노드가 나옵니다.
    n1, n2 = list(map(int, input().split(' ')))
    graph[n1][n2] = 1
    graph[n2][n1] = 1



# <BFS 함수>
# - 필요한 데이터 : 그래프, 시작노드
# 1. 탐색예정노드를 저장할 큐를 생성합니다.
# 2. 방문완료노드를 저장할 리스트 생성합니다.
# 3. 시작노드를 큐에 추가하기
# 4. 탐때까지 탐색을 시작해서 큐가 빌색한다.
#  (1) 하나를 뽑는다.
#  (2) 방문완료노드에 없으면 추가해준다.
#  (3) 없으면 해당 노드와 연결된 노드를 큐 추가한다.

def bfs(graph, start):
    queue = deque()
    visited = []
    queue.append(start)
    while queue:
        sea = queue.popleft()
        if sea not in visited:
            visited.append(sea)
            for i in range(len(graph[sea])):
                if graph[sea][i] == 1 and i not in visited:
                    queue.append(i)
    # print(queue, visited)
    # return 결과
    # "구분인자".join(리스트)
    return ' '.join(map(str, visited))

    
# print(bfs(graph, v))

# <DFS 함수> - stack구조로 만들기 LIFO 맨뒤에서
# - 필요한 데이터 : 그래프, 시작노드
# 1. 탐색예정노드를 저장할 스택(리스트) 생성하고
# 2. 방문완료노드를 저장할 리스트를 생성합니다.
# 3. 시작노드를 스택에 추가하기
# 4. 탐색이 끝날때까지 스택을 뽑기
#  (1) 하나뽑고
#  (2) 방문 안했으면 추가
#  (3) 없으면 연결된 노드 중에서 방문안한것만 스택에 추가
#    - 추가시 방향 조심(왼쪽부터방문할수 있도록)
def dfs(graph, v):
    stack = []
    visited = []
    stack.append(v)
    while stack:
        no = stack.pop()
        # print("\n뽑힌노드", no)
        if no not in visited:
            visited.append(no)
            # print(graph[v])
            for i in range(len(graph[no])):
                # 여기다가
                new_no = len(graph[no]) - i - 1
                if graph[no][new_no] == 1:
                    # print("--",new_no)
                    if new_no not in visited:
                        stack.append(new_no)
        # print(stack, visited)
    return ' '.join(map(str, visited))

print(dfs(graph,v))
print(bfs(graph, v))
