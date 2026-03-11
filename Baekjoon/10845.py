# 큐 https://www.acmicpc.net/problem/10845
# collection deqeu 모듈
import sys
from collections import deque

# 명령어간소화변수 =sys.stdin.readline: 시스템모듈을 사용해서 표준입력을 받을건데 라인별로 받아보기
sys_input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.q = deque()
    def enqueue(self, x):
        self.q.append(x)
    def dequeue(self):
        if self.isempty():
            return -1
        else:
            return self.q.popleft()
       
    def isempty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    def size(self):
        return len(self.q)
    def front(self):
        if self.isempty() == 1:
            return -1
        else:
            return self.q[0]
    def rear(self):
        if self.isempty() == 1:
            return -1
        else:
            return self.q[-1]

queue = Queue()


n = int(sys_input())


for i in range(n):
    inp = sys_input().strip('\n').split(' ')
    # print(inp)
    if inp[0] == 'push':
        queue.enqueue(int(inp[1]))
    elif inp[0] == 'pop':
        print(queue.dequeue())
    elif  inp[0] == 'empty':
        print(queue.isempty())
    elif  inp[0] == 'size':
        print(queue.size())
    elif  inp[0] == 'front':
        print(queue.front())
    elif  inp[0] == 'back':
        print(queue.rear())






