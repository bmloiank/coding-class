# 22. TODO: 배수와 약수 https://www.acmicpc.net/problem/5086 (나머지 생각)
# 짝수(2로 나눴을때 나머지가 0) : 2의 배수 (2로 나눴을대 나머지가 0)
# x 약수 나머지 0이 되는 나누는 수의 모음


# num = list(map(int, input().split(' ')))
# print(num)
# num1 = num[0]
# num2 = num[1]
# print(num1, num2) 
while True:
    num = list(map(int, input().split(' ')))
    num1 = num[0]
    num2 = num[1]
    if num == [0, 0]:
        break
    elif num2 % num1 == 0:
        print('factor')
    elif num1 % num2 == 0:
        print('multiple')
    else: print('neither')
