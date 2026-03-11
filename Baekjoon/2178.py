# 미로탐색 : https://www.acmicpc.net/problem/2178
# 목적지까지 가는게 걸리는 거리는?
from collections import deque

n, m = list(map(int, input().split()))
map = []
for i in range(n):
    map.append(list(input()))

# print(n, m, map)
i, j = 0, 0
# print(x, y)



# (0) 셋팅
q = deque()
q.append((i,j))
distance = [[0 for l in range(m)] for k in range(n)] 
# print(distance)
distance[0][0] = 1

# print(q)
# (1) 탐색시작 q
# - 탐색할 값 뽑기
# (2) 탐색조건 만족하면 =>  탐색예정에 넣기
# - 위, 아래, 좌, 우
# - i>0 / i < 마지막행인덱스값 / j>0 / j<마지막열인덱스값    
# print(distance)
while q:
    nowi, nowj = q.popleft()
    if nowi > 0:
        if map[nowi-1][nowj] == '1' and distance[nowi-1][nowj] == 0 and (nowi-1, nowj) not in q:
            distance[nowi-1][nowj] = distance[nowi][nowj] + 1
            q.append((nowi-1, nowj))
            # print(distance)
    if nowi < (n-1):
        if map[nowi+1][nowj] == '1' and distance[nowi+1][nowj] == 0 and (nowi+1, nowj) not in q:
            distance[nowi+1][nowj] = distance[nowi][nowj] + 1
            q.append((nowi+1, nowj))  
    if nowj > 0:
        if map[nowi][nowj-1] == '1' and distance[nowi][nowj-1] == 0 and (nowi, nowj-1) not in q:
            distance[nowi][nowj-1] = distance[nowi][nowj]  + 1
            q.append((nowi, nowj-1))
    if nowj < (m-1):
        if map[nowi][nowj+1] == '1' and distance[nowi][nowj+1] == 0 and (nowi, nowj+1) not in q:
            distance[nowi][nowj+1] = distance[nowi][nowj] + 1
            q.append((nowi, nowj+1))
    # print(q)
   

# for i in range(len(distance)):
#     print(distance[i])

print(distance[n-1][m-1])




# 4 6
# 110110
# 110110
# 111111
# 111101