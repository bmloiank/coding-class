'''
투 포인터(two-pointer)

(포인터)
a=1 1216283729749817 위치
포인터변수 = a의 위치(인덱스)를 저장하는 변수

슬라이딩 윈도우 : 저장을 따로 할필요성이 있을 때
원본  5 3 2 5 7 1 4
리스트= 구간 4 [ 5 3 2 5 ]
                [3 2 5 7]

투포인터 : 구간 자유로울 때~
원본  start 0 end 3
        start 1 end 4

'''
# 수들의 합2 https://www.acmicpc.net/problem/2003
'''
문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 
다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 
각각의 A[x]는 30,000을 넘지 않는 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다.


'''
n, m = list(map(int, input().split()))
deck = list(map(int, input().split()))
# print(n,m, deck)

# 10 5  # n=숫자갯수 m=5(합)
# 1 2 3 4 2 5 3 1 1 2
# 시작=0, 끝=0

# 1         합이 작으면 끝 1늘려
# 1 2       합이 커요 시작 1늘려 
# 1 2 3     
#   2 3     맞으면 카운트 늘려 end 1늘려
#   2 3 4   합이 커요 시작 1늘려 합게는 빠진 애를 빼
count = 0
start = 0
end = 0
total = deck[start]
while True:
    if total <= m:
        end += 1
        if total == m:
            count += 1
        if end == n:
            break
        total += deck[end]
    elif total > m:
        total -= deck[start]
        start += 1


# 리팩토링

print(count)