# https://www.acmicpc.net/problem/8958

n = int(input())
for i in range(n):
    ox = list(input())
    # print(ox)
    point = 0
    count_O = 0
    for j in range(len(ox)):
        if ox[j] == 'O' and count_O == 0:
            point += 1
            count_O += 1
        elif ox[j] == 'O' and count_O != 0:
            point = point + count_O + 1
            count_O += 1
        elif ox[j] == 'X':
            count_O = 0
    print(point)





