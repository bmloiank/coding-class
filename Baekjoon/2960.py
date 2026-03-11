# 에라토스테네스의 체 https://www.acmicpc.net/problem/2960

'''
에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

이 알고리즘은 다음과 같다.

1. 2부터 N까지 모든 정수를 적는다.
2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
4.아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.


<시뮬레이션>
   0 3  0  5
0  7  0  9  0
11 0 13 0 15
16 17 18 19 20

'''
n, k = list(map(int, input().split()))

# (1) 2~부터 n까지의 리스트가 필요하다.
chat = []
for i in range(2, n+1):
    chat.append(i)

count = 0

# (2) 모든 수에 대해서 소수인지 아닌지
for i in range(n-1):
    # 소수 위치부터 끝까지 반복을 돌리면서 소수의 배수를 삭제 합니다. 
    #  - 직접 삭제 대신에 지워졌다는 것 0으로 표시할 예정
    p = chat[i]
    if p == 0:
        continue
    for j in range(i, n-1):
        if chat[j] != 0 and chat[j] % p == 0:
            count += 1
            if count == k:
                print(chat[j])
            chat[j] = 0





        # print(chat)
# print(count)    
# start = 2

# while count != k:
#     for i in range(1, n+1):
#         if start*i > n+1:
#             break
#         if chat[start*i] != '*':
#             chat[start*i] = '*'
#             count += 1
# print(count)        





