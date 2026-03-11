# 구간 합 구하기4 https://www.acmicpc.net/problem/11659

'''
5 3
5 4 3 2 1  # 공통된 숫자 리스트

# 누적합
5 9 12 14 15

1 3  1~3까지의 합 => 누적합의 3
2 4  2~4까지의 합 => 누적합 4-1
5 5  5~5까지의 합



'''


import sys
input = sys.stdin.readline 

n, m = list(map(int, input().split()))
deck = list(map(int, input().split()))
# print(m, n, deck)
# 0으로 n개 채우기
pile = [0]*n

# 시간초과 시 주의사항 이중for문
# 반복문 2개 != 이중for문
# 100+100 != 100*100

for k in range(n):
    if k == 0:
        pile[k] = deck[k]
    else:
        pile[k] = deck[k] + pile[k-1]
# print(pile)

for l in range(m):
    i, j = list(map(int, input().split()))
    i, j = i-1, j-1
    if i == 0:
        print(pile[j])
    else:
        print(pile[j] - pile[i-1])




# for k in range(m):
#     i, j = list(map(int, input().split()))
#     i, j = i-1, j-1
#     sum = 0
#     for l in range(j-i+1):
#         sum += deck[i+l]
#     print(sum)


