# 동전O https://www.acmicpc.net/problem/11047

# 그리디 알고리즘(=탐욕법)
# - 사람 기준으로도 최대한 좋은 선택을 반복하는 것

'''
문제)
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.


# 입력)
10 4200
1
5
10
50
100   2장
500
1000  4장
5000
10000
50000

'''
# sys input사용할것
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
value = []
for i in range(n):
    value.append(int(input()))


total = 0
for i in range(n):
    coin = value[n-1-i]
    if coin <= k:
        total+= k // coin
        k = k % coin
print(total)






# # 과제~~!
# total = 0
# w = 0
# for i in range(n//2+1):
#     for j in range(n):
#         if value[n-j-1] - k < 0:
#             w = value[n-j-1]
#             break
#     total += k//w
#     # print(k//w, '--')
#     k = k - w*(k//w)
# print(total)
