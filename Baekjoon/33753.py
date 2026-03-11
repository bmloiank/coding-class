# 주차요금 정산기 https://www.acmicpc.net/problem/33753

a, b, c = list(map(int,input().split(' ')))
# print(a)
t = int(input())
# print(c, t)

if t <= 30:
    print(a)
elif (t-30) % b != 0:
    time = (t-30) // b + 1
    # print(time)
    print(a+time*c)
else:
    time = (t-30) // b
    print(a+time*c)

