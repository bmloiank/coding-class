# 16. (6/2 과제) 중복 빼고 정렬하기 https://www.acmicpc.net/problem/10867

n = int(input())
num = input().split()
answer =[]

for i in range(n):
    answer.append(int(num[i]))
# print(answer)

answer = list(set(answer))
answer = sorted(answer)

# 리스트의 요소에 함수를 적용하는 함수
# map(함수이름만,리스트)
answer_str = list(map(str, answer))
# print(answer_str)
# answer_str = []
# for i in range(len(answer)):
#     answer_str.append(str(answer[i]))
    
print(' '.join(answer_str))


