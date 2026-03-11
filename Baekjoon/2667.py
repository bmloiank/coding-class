  # 과제) 단지번호 붙이기 https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())

m = []
for i in range(n):
    m.append(list(map(int, list(input()))))
# print(m)

my = [-1,1,0,0]
mx = [0,0,-1,1]

q = deque()
total = []

for i in range(n):
    for j in range(n):
        
        if m[i][j] == 1:
            count = 1
            m[i][j] = 5
            q.append((i,j))
            while q:
                ny, nx = q.popleft()
                for k in range(4):
                    if 0 <= ny+my[k] < n and 0 <= nx+mx[k] < n and m[ny+my[k]][nx+mx[k]] == 1:
                        count += 1
                        m[ny+my[k]][nx+mx[k]] = 5
                        q.append((ny+my[k], nx+mx[k]))
            total.append(count)    

            # for i in range(len(m)):
            #     print(m[i])
            # print('----', total)

print(len(total))
total.sort()
for i in range(len(total)):
    print(total[i])






