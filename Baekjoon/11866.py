# 요세푸스 문제 https://www.acmicpc.net/problem/11866 (큐 사용)

# <3 6 2 7 5 1 4> 

# 7 3
# 1 2 3 4 5 6 7
#     X     X
# 1 2 4 5 7
#   X     X
# 1 4 5
#     X
# 1 4
# X
# 4
# X

# 3, 6, 2, 7 , 5, 1, 4

# from collections import deque

inp = list(map(int, input().split(' ')))
n = inp[0] # 인원수 갯수
k = inp[1] # 

circle = [] # 남아있는 번호
for i in range(n):
    circle.append(i+1)

answer = [] # 빠진 애들을 순서대로 넣는 공간

# circle2 = [] # 의미 <= 적절하지 못하다.
# print(circle)
# print(answer)


# [1,2,'3',4,5,6,7]


# 디버깅: 버그를 찾는과정 => print()
# for l in range(n):
#     print("시작:",circle2)
#     if n % k != 0:
#         for i in range(n//k):
#             for j in range(k-1):
#                 circle2.append(circle.popleft())
#             answer.append(circle.popleft())
#     else:
#        for i in range(n//k-1):
#             for j in range(k-1):
#                 circle2.append(circle.popleft())
#             answer.append(circle.popleft() )
#     while circle:
#         circle2.append(circle.popleft())
#     circle = circle2
#     while circle2:
#         circle2.popleft()
#     print("반복끝:",circle2)
#     circle2.append(circle.popleft())
# print(answer)
# print(circle)

# point = 0
# for in range(n):
#     if circle[i] == 'X':
#         point += 1
# for i in range(n-point):
# while len(circle) == 0:
    # print(circle)


# (1) circle이 빌때까지 반복하기
x = 0 # 제거할 번호
while circle:
    x += k-1
    # print(x)
    # pop(인덱스)
    # 나머지
    # if x >= len(circle):
    x = x % len(circle)
    pop_num = circle.pop(x)
    answer.append(str(pop_num))
print('<'+', '.join(answer)+'>')



# x=2
# [1,2,"x",4,5,6,7]
# x=5
# [1,2,"x",4,5,"x",7]
# x=8 => 1
# [1,"x","x",4,5,"x",7]
# x=> 4  => 6번 조정


# 1, 2, x, 4, 5, 6, 7
#       x        x
#    x
# for i in range(len(circle)):
#     if circle[i]%k == 0:
#         circle[i] = 'X'
# for j in range(len(circle)):
#     if circle[j] != 'X':
#         circle2.append(circle[j])
# circle = circle2
# print(circle)



