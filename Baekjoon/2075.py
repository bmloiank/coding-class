# N번째 큰수 https://www.acmicpc.net/problem/2075
# - 메모리가 작다 => 힌트) 저장을 많이 할수 없다.

# n = int(input())

# full = []
# for i in range(n):
#     row = list(map(int, input().split(' ')))
#     full.extend(row)
# print(full)

# print(sorted(full)[-1 * n])

# import heapq

# n = int(input())

# queue = []
# for i in range(n):
#     row = list(map(int, input().split(' ')))
#     for j in range(n):
#         heapq.heappush(queue, row[j])

# for i in range(n*n - n):
#     heapq.heappop(queue)
# print(heapq.heappop(queue))


# n = int(input())

# row1 = list(map(int, input().split(' ')))
# top = sorted(row1)[-1]
# # print(top)
# bigger = [top]
# for i in range(n-1):
#     row = list(map(int, input().split(' ')))
#     for j in range(n):
#         if row[j] > top:
#             bigger.append(row[j])
#             # print(bigger)

# print(sorted(bigger)[-1 * n])



import heapq

n = int(input())

row1 = list(map(int, input().split(' ')))
top = sorted(row1)[-1]
# print(top)
bigger = []
heapq.heappush(bigger, top)
for i in range(n-1):
    row = list(map(int, input().split(' ')))
    for j in range(n):
        if row[j] > top:
            heapq.heappush(bigger, row[j])
            # print(bigger)
            if len(bigger) > n:
                for k in range(len(bigger) - n):
                    heapq.heappop(bigger)
            # print(bigger)

print(sorted(bigger)[-1 * n])