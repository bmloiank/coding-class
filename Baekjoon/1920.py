# 수 찾기 https://www.acmicpc.net/problem/1920

'''
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.


#
5 
4 1 5 2 3

5
1 3 7 9 5


# 예제 출력
1
1
0
0
1

'''




# 1 2 3 4 5 6 7 8 9 10
# (s)    (e)
# 13


import sys
input = sys.stdin.readline

n = int(input())
chat_n = list(map(int, input().split()))
m = int(input())
chat_m = list(map(int, input().split()))
chat_n.sort()

def binary_search(lst, f):
    # lst.sort()
    start = 0
    end = len(lst)
    while start < end:
        mid = (end + start)//2
        if lst[mid] == f:
            return 1
        if f > lst[mid]:
            start = mid+1
        else:
            end = mid
        # print("start",start,"end",end)
    return 0

for i in range(m):
    print(binary_search(chat_n, chat_m[i]))
   


# for i in range(m):
#     count = 0 # 초기화 - 위치 반복문 안에서 초기화 하시면 하면 의미없음.
#     for j in range(n):
#         if chat_m[i] == chat_n[j]:
#             count = 1
#     print(count)
















