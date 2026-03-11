# 15. (5/28 과졔) 나머지 https://www.acmicpc.net/problem/3052

answer = []
for i in range(10):
    num = int(input())
    answer.append(num % 42)
    
result = 0
answer_set = set(answer)
# for j in range(len(answer)):
#     # (1) 어떤값이 리스트안에 있냐없냐?  in, not in 
#     # (2) 어떤값이 리스트의 뭔가와 비교하고 싶다. => 반복문 돌리기
#     # (3) 중복제거 => 중복제거알고리즘/set()
#     if answer[i]  :
#         result += 1

print(len(answer_set))






















