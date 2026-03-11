# 약수 구하기 https://www.acmicpc.net/problem/2501

n, k = list(map(int, input().split(' ')))

pile = []


for j in range(n):
    j = j+1
    # print(a[i], j)
    if n % j == 0 and j not in pile:
        # print(j)
        pile.append(j)
# print(pile2)

# print(pile)
if k > len(pile):
    print(0)
else:
    print(pile[k-1])