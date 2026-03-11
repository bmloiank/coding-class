'''
6. (2/27 과제) 과자 https://www.acmicpc.net/problem/10156

'''
# 과자 한 개의 가격 K, 사려고 하는 과자의 개수 N, 현재 동수가 가진 돈 M
q = input()
q = q.split(' ')
k = int(q[0])
n = int(q[1])
m = int(q[2])
# print(m)
if k*n > m:
    print(k*n-m)
elif k*n <= m:
    print(0)








