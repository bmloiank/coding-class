# https://www.acmicpc.net/problem/11653

# 36
# 작은 숫자부터 차근차근 나눠줍니다.
# - 한개의 숫자를 나머지가 0이면 나누고, 아니면 다음숫자로 넘어가기
# 36보다 작아야한다. 나누어지는 수가 1이되면 종료

# 36/2 = 18
# 18/2 = 9
# 9/3 = 


num = int(input())
a=2
# print(num)
while True:
    # 종료 조건
    if num == 1:
        break

    if num % a == 0:
        # 나눈다
        print(a)
        num = num // a
        
    else:
        a = a+1
# 7