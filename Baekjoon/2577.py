'''
숫자의 개수 https://www.acmicpc.net/problem/2577

문제)
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.


입력)
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

'''
a = int(input())
b = int(input())
c = int(input())
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(a, b,c)
# 곱셈은 숫자끼리
answer = str(a*b*c)
# num = 
# print(answer)
# 길이를 구하는 것은 문자로
# int -> str
for i in range(len(answer)):
    # print(answer[i])
    for j in range(len(num)):
        if answer[i] == num[j]:
            result[j] += 1
# print(result)

for i in range(len(result)):
    print(result[i])






















