# 괄호 https://www.acmicpc.net/problem/9012

# (()()()()()())
# ((((())())()))

# 괄호가 정상적이다  (열려있으면 제때 )닫혀야한다.
# - )닫는거 부터 시작하면 안된다.
# - 마지막까지 다 안닫히면 안된다.

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


t = int(input())

for i in range(t):  
    inp = input()
    # inp = ['(','(',')',')','(',')',')']
    # (
    # (
    # )
    # )
    # (
    # )
    # )
    stack = Stack()
    answer = "YES"
    # 스택이 비어있을때, 입력 )
    for j in range(len(inp)):
        # ( "열린괄호" 
        # ) "닫힌괄호"
        # (1) 만약에 열린괄호가 나오면 / 스택에 넣어준다.
        # - :닫힌괄호가 나올때까지 스택에 들어가서 기다려기
        # (2) 만약에 닫힌 괄호가 나오면
        # - 스택안에 ')'괄호가 있는지 살펴보기
        # - 괄호가 없으면 "no" 괄호가 있으면 맨위에'열린괄호'가 있으면 빼기
        if inp[j] == '(':
            stack.push(inp[j])
        elif inp[j] == ')':
            if stack.isempty() == True:
                answer = 'NO'
                break
            else:
                if stack.top() == '(':
                    stack.pop()
          


    if not stack.isempty():
        answer="NO"
    print(answer)
