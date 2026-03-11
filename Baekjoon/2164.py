# 카드2 https://www.acmicpc.net/problem/2164

from collections import deque

n = int(input())

pile = deque()
for i in range(n):
    pile.append(i+1)
    
for i in range(n-1):
    pile.popleft()
    spot = pile.popleft()
    pile.append(spot)
print(pile[0])