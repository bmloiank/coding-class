# TODO 연결 요소의 갯수 https://www.acmicpc.net/problem/11724

# dfs bfs : 그래프 탐색
'''
<그래프>
: 일직선으로 연결된 리스트
: 노드들로 거미줄 처럼 연결되는 구조  

1. 노드node : 연결점
2. 엣지edge : 연결선

3. 인접행렬 : 그래프의 연결관계를 표현하는 방법
(1) 이차원리스트형태 인접행렬 => 연습하기
-> 노드가 숫자

A - B, C
B - A, D, E
C - A
D - B, E
E - B, D

'''
'''
# 노드갯수 * 노드갯수 이차원리스트를 생성한다.
node_list = ["A","B",'C','D','E']
matrix= [
    [0,1,1,0,0],  # A
    [1,0,0,1,1],  # B
    [1,0,0,0,0],
    [0,1,0,0,1],
    [0,1,0,1,0],
]




# (2) 딕셔너리형태의 인접행렬
# -> 노드가 문자
{
    'A':['B', 'C'], 
    'B':['A', 'D', 'E'], 
    'C':['A'], 
    'D':['B', 'E'], 
    'E':['B', 'D']
}




# 과제) 연결요소의 갯수 https://www.acmicpc.net/problem/11724
# 과제) 단지번호 붙이기 https://www.acmicpc.net/problem/2667 (ok)


'''
import sys
from collections import deque

# input함수를 sys.stdin.readline 변경
input = sys.stdin.readline

n, m = list(map(int, input().split()))
connect = [[0 for l in range(n)] for k in range(n)]
# print(connect)


for i in range(m):
    n1, n2 = list(map(int, input().split()))
    connect[n1-1][n2-1] += 1
    connect[n2-1][n1-1] += 1
# print(connect)

q = deque()
count = 0
visited = [0]*n # 노드 방문완 이차원리스트 하면 시간초과가 뜨기때문에
for i in range(n):
    if visited[i] != 0:    
        continue
    
    count += 1
    q.append(i)
    while q:
        now = q.popleft()
        # 
        if visited[now] != 1:
            visited[now] = 1
            for j in range(n):
                if connect[now][j] == 1:
                    connect[now][j] = 2
                    connect[j][now] = 2
                    q.append(j)
    
        # print(connect, q, count)
    # print('---')

print(count)






