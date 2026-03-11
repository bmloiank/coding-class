# 카드게임 https://www.acmicpc.net/problem/10801

a = list(map(int, input().split()))
b = list(map(int, input().split()))
# print(a, b)
apoint = 0
bpoint = 0
for i in range(10):
    if a[i] > b[i]:
        apoint += 1
    elif a[i] < b[i]:
        bpoint += 1
if apoint > bpoint:
        print('A')
elif apoint < bpoint:
        print('B')
else:
    print('D')
