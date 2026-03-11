# 팩토리얼 https://www.acmicpc.net/problem/10872
# 5! = 5*4*3*2*1
#    = 5*4!
# n! = n * (n-1)!  => 점화식(고2)
# 0! = 1

n = int(input())
def feel(n):
    if n == 1 or n==0:
        return 1
    return n*feel(n-1)
print(feel(n))



# feel(5)
# 5*feel(4)
#     4*feel(3)
#         3*feel(2)
#             2*feel(1)









