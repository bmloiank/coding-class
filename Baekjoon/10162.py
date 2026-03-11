# 전자레인지 https://www.acmicpc.net/problem/10162

t = int(input())
value = [300, 60, 10]
a = []
for i in range(len(value)):
    if t // value[i] > 0:
        a.append(t // value[i])
        t -= t // value[i] * value[i]
    else:
        a.append(0)
# print(a)
if t == 0:
    a = ' '.join(list(map(str, a)))
    print(a)
else:
    print(-1)



