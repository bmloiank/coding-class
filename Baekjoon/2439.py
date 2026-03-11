'''
5. (2/27 과제) 별찍기-2 https://www.acmicpc.net/problem/2439
'''
s = input()
s = int(s)
for i in range(s):
    # 주의사항 : 반복변수를 직접적으로 바꾸는 반복에 영향을 줄수있다.
    # i 별의 갯수 
    star = i+1
    # n 공백의 갯수 4
    # n = s-i-1
    n = s-star
    print(str(star)+str(n))
    # if n >= 0:
    print(' ' * n + '*' * star)
    # elif n < 0:
    #     print('*' * s)

# # 주의사항
# print("내용","내용") # 두 문자열 사이에 띄어쓰기가 존재한다.
# print("내용"+"내용")  # 두 문자열을 이어서 새로운 문자열을 만들기

# s = input()
# s = int(s)
# for i in range(s):
#     i = i+1
#     n = s-i-1
#     print(' ' * n, '*' * i)

# s = input()
# s = int(s)
# for i in range(s):
#     i = i+1
#     n = s-i
#     print(' ' * n, '*' * i)




# s = input()
# s = int(s)
# for i in range(s):
#     i = i+1
#     # q = i+1
#     # a = i+2
#     # a = s-1
#     # s = s+1
#     # n = s/i
#     # n = int(s/i)
#     # n = s//i
#     # n = i[-1]
#     n = s-i
#     n = n-1
#     # n = s-i-1
#     # n = s-s
#     # n = a-q
#     # n = s-a
#     print(' ' * n, '*' * i)


#i가 뭘까.......?
# print(s-i)


# s = input()
# s = int(s)
# for i in range(s):
#     i = i+1
#     n = i[-1]
#     n = int(n)
#     print(' ' * n, '*' * i)


# print(' '*0, '.')

# for i in range(5):
#     i = 0
#     print(' ' * i, '.')






