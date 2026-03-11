'''
피보나치수열5 https://www.acmicpc.net/problem/10870
=> 재귀함수를 통해서 
a[n] = a[n-1]+a[n-2](N>=2)

(종료조건)
a[0] =0
a[1] =1
fibonacci

'''

n = int(input())
# print(n)

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # print(a)
    return f(n-1) +  f(n-2)


print(f(n))



# 팩토리얼2 https://www.acmicpc.net/problem/27433
# 10!(팩토리얼-수학 순열) = 10*9*8*7...*1
# 9!

# 재귀의귀재 https://www.acmicpc.net/problem/25501







