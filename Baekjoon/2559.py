# 수열 https://www.acmicpc.net/problem/2559


''' 
열흘 : 연속적으로 며칠동안 온도의 합을 구해야 최대온도가 되냐?
        3 -2 -4 -9 0 3 7 13 8 -3

2틀 연속 => 최대값
3일 연속 => 최대값
4일 연속 => 최대값
5일 연속 => 최대값
.
.
최대값 들 중에서도 가장 큰거

'''

n, k = list(map(int, input().split()))
t = list(map(int, input().split()))
t_sum = [0]*n
for i in range(n):
    if i == 0:
        t_sum[i] = t[i]
    else:
        t_sum[i] = t_sum[i-1] + t[i]



# 최대값들 중에서 가장 큰 놈
# total 기본값이... : 첫날부터 끝날까지의 합
total = t_sum[k-1]

for j in range(n-k+1):
    # 차이변수
    diff = t_sum[j+k-1] - t_sum[j-1]

    # 최대값 구하는 알고리즘
    if j != 0 and diff > total:
        total = diff
print(total)
    

# 인간-컴퓨터 상호작용 https://www.acmicpc.net/problem/16139
# 점수를 최대로 https://www.acmicpc.net/problem/29767