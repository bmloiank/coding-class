# TODO 균형잡힌 세상 https://www.acmicpc.net/problem/4949

# 클래스
# : 속성= 변수,데이터 + 메서드=함수,행동


class Stack:
    def __init__(self):
        self.l = []
    def push(self, x):
        self.l.append(x)
    def pop(self):
        if self.isempty() :
            return None
        else:
            return self.l.pop()
    def size(self):
        return len(self.l)
    def isempty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def top(self):
        if self.isempty():
            return None
        else:
            return self.l[-1]

# 입력) .온점이 나오면 끝난다.
# => 몇번 입력받을 지 알아요몰라요? 
# => (1) 무한으로 (2)입력을 받아다가, (3)받은 입력값이 '.'이면 반복문 종료 break


# (1) So when I die (the [first] I will see in (heaven) is a score list).
# 2. [ first in ] ( first out ).
# 3. Half Moon tonight (At least it is better than no Moon at all].
# 4A rope may form )( a trail in a maze.
# 5Help( I[m being held prisoner in a fortune cookie factory)].
# 6([ (([( [ ] ) ( ) (( ))] )) ]).
# 7 .
# 8.

while True: # =>무한반복
    n = []
    inp = input()
    n.append(inp)
    if inp == ".":
        break

    #예시 : ([)] (X)
    # 소괄호 ()
    # 대괄호 []
    for j in range(len(n)):
        gh = Stack()
        s = []
        for k in range(len(n[j])):
            if n[j][k] == '(': # 열린괄호 - 대기
                gh.push(n[j][k])
            elif n[j][k] == '[': # 열린괄호
                gh.push(n[j][k])
            elif n[j][k] == ')':
                # 비어있지않고, 스택맨위(top)에 '('있으면 => 짝이 맞네
                # 스택 뽑기 
                if gh.top() == '(':
                    gh.pop()
                else:                
                    gh.push(')')
                    s.append('no')
                    break
                
            elif n[j][k] == ']':
                if gh.top() == '[':
                    gh.pop()
                else:             
                    gh.push(']')   
                    s.append('no')
                    break
        # in 사용 잘 안해요
        # => for if 체크
        
        if len(s) == 0 and gh.isempty() == True:      
            print('yes')
           
        else:
            print('no')


# https://solved.ac/profile/bmloiank
            




















# n = []

# for i in range(8):
#     inp = input()
#     n.append(inp)
# for j in range(len(n)):
#     small = Stack()
#     big = Stack()
#     s = []
#     b = []
#     for k in range(len(n[j])):
#         if n[j][k] == '(':
#             small.push(n[j][k])
#         elif n[j][k] == ')':
#             if small.isempty() == True:
#                 s.append('NO')
#                 break
#             else:
#                 if small.top() == '(':
#                     small.pop()
#         if n[j][k] == '[':
#             big.push(n[j][k])
#         elif n[j][k] == ']':
#             if big.isempty() == True:
#                 b.append('NO')
#                 break
#             else:
#                 if big.top() == '[':
#                     big.pop()
#     print(b, s)
#     s = []
#     b = []
#     small = Stack()
#     big = Stack()








