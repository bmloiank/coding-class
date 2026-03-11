# 1. 스택 https://www.acmicpc.net/problem/10828

''''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

# input() : 입력받았을때, 객체로 씌워지고, 줄바꿈이 진행이됩니다.
# sys시스템에서 입력을 직접 받아보기 : 

import sys
# stdin(standard input): 표준입력
# 입력받기: sys.stdin.readline
# 출력하기: sys.stdout.write
# 나만의 입력함수이름 = sys.stdin.readline
ssr = sys.stdin.readline
ssw = sys.stdout.write
# class Stack:
#     def __init__(self):ghgyyktyutitt
#         self.l = []
#     def push(self, x):
#         self.l.append(x)
#     def pop(self):
#         if self.isempty() :
#             return -1
#         else:
#             return self.l.pop()
#     def size(self):
#         return len(self.l)
#     def isempty(self):
#         if self.size() == 0:
#             return 1
#         else:
#             return 0
#     def top(self):
#         if self.isempty():
#             return -1
#         else:
#             return self.l[-1]

# # (1)스택을 만들어라
# stack = Stack()

# # (2) 입력을 받아라
# n = int(ssr())
# for i in range(n):
#     ob_list = ssr().strip("\n").split(' ')
#     # print(ob_list)
#     if ob_list[0] == 'push':
#         ob_int = int(ob_list[1])
#         stack.push(ob_int)
#         # print(stack.l)
#     elif ob_list[0] == 'top':
#         ssw(str(stack.top()))
#         ssw("\n")
#     elif ob_list[0] == 'pop':
#         ssw(str(stack.pop()))
#         ssw("\n")
#     elif ob_list[0] == 'size':
#         ssw(str(stack.size()))
#         ssw("\n")
#     elif ob_list[0] == 'empty':
#         ssw(str(stack.isempty()))
#         ssw("\n")

# 문자열 포멧코드
# sys.stdout.write("문자열")
# %d : 정수
# %s : 문자열
# %f : 소수

# ssw("%d" %변수)
# sys.stdout.write("숫자를넣겠다")
# print("=======")
# num = 10
# sys.stdout.write('%d\n' %num)
# sys.stdout.write('%d\n' %num)
# sys.stdout.write('%d\n' %num)
# sys.stdout.write('%d\n' %num)




















