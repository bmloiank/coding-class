# 최대힙 https://www.acmicpc.net/problem/11279

import sys
import heapq
input = sys.stdin.readline

n = int(input())
queue = []

for i in range(n):
    x = int(input()) * -1
    if x == 0:
        if len(queue) == 0:
            print(0)
        else : 
            print(heapq.heappop(queue) * -1)
    elif x != 0:
        heapq.heappush(queue, x)









