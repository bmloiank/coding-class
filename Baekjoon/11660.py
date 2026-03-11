# 과제) 구간 합 구하기 5 https://www.acmicpc.net/problem/11660

n, m = list(map(int, input().split()))
chat = []
pile = [[0 for j in range(n)]for i in range(n)]
for i in range(n):
    chat.append(list(map(int, input().split())))
# print(pile)
for i in range(n):
    for j in range(n):
        if j == 0:
            pile[i][j] = chat[i][j]
        else:
            pile[i][j] = chat[i][j] + pile[i][j-1]
    # print(chat, pile)


for i in range(m):
    x1, y1, x2, y2 = list(map(int, input().split()))
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    count = 0
    for j in range(x2-x1+1):
        if y1 == 0:
            count += pile[x1+j][y2]
        else:
            count += pile[x1+j][y2] - pile[x1+j][y1-1]
    print(count)


