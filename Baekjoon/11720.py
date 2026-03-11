'''
https://www.acmicpc.net/problem/11720
'''

# 그냥 list()

n = int(input())
num = input()


# 함수의 입력
# 입력 : 2개
# 결과 : 1개 




def plase(n, num):
    total = 0
    for i in range(n):
        total += int(num[i])
    print(total)

plase(n, num)