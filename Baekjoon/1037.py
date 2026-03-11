# 약수 https://www.acmicpc.net/problem/1037

'''
문제)
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

[ ]의 약수 
1 2 3 4 6 12

찐약수 : 2 4 6 3 
=> 제일 작은수 * 제일 큰수 

'''


# 약수의 갯수
n = int(input())  
# 찐약수
a = sorted(map(int, input().split(' ')))
# print(n, a)

print(a[0] * a[-1])












