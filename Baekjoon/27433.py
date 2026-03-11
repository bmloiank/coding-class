# 팩토리얼2 https://www.acmicpc.net/problem/27433
# 10!(팩토리얼-수학 순열) = 10*9*8*7...*1
# 9!

n = int(input())

# nl = 1

# for i in range(n):
#     nl = nl*(i+1)
    
# print(nl)

def f(n):
    if n == 0:
        return 1
    return n * f(n-1)
    # n!*n-1!
    # n! = n*n-1*n-2*n-3...*1
    # n! = n * (n-1)!

print(f(n))



