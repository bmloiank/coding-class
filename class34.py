'''
Queue 큐
: FIFO(First In First Out)
    --------------------            =>enqueue(x)
<-front        <-          <-rear   =>dequeue()
    --------------------            => size()
                                    => isempty()
                                    => front()
                                    => rear()
'''

class Queue:
    def __init__(self):
        self.q == []
    def enqueue(self, x):
        self.q.append(x)
    def dequeue(self):
        if self.isempty():
            return None
        else:
            return self.q.pop(0)
       
    def isempty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.q)




# 스택의 경우 LIFO
# -> 마지막값을 꺼내죠. -> 리스트구조랑 크게 다르지 않습니다.
# 리스트.pop()
# 언제사용할지

# 큐의 경우 FIFO
# -> 첫번째 값을 꺼낸다. -> 리스트구조로 작업할경우, 성능이슈
# -> 큐를 빠르게 쓰는 모듈 
# 
# collections모듈 deque객체를 가져오기
# from 모듈 import 모듈내부클래스

from collections import deque
# (1) 데크, 덱, 디큐: double-ended queue
#     -------------------- 
#   <-                  <-
#   ->                  ->
#     --------------------     

# (1) deque(): 덱 생성하기
# (2) append(x) 오른쪽끝에서 추가
# (3) appendleft(x) : 왼쪽에서 추가
# (4) pop() : 오른쪽 끝에서 뽑기
# (5) popleft() : 왼쪽에서 뽑기
# tip) extend([]) : 여러개의 원소를 동시에 추가
dq = deque()
dq.append(1)
dq.appendleft(2)
dq.append(3)
print(dq)
print(dq.popleft())
print(dq.popleft())
print(dq.popleft())
print(dq)
# ['a','b','c','d']
dq.extend(['a','b','c','d'])
dq.extendleft(['a','b','c','d'])
print(dq)
