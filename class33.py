# 7단계 - 자료구조
# - 파이썬 자체에서 지원하는게 많아서 자료구조가 크게 어렵지 않다.
# - C언어로 배웠으면... 매우 어렵다.

# 회원 :  
# - 엔트리 : 네이버(웹사이트, 동물농장), 야후
# - 네이버: 4000만~
# - 당근유저: 1000만원 


#(1) Stack 구조 => LIFO구조
# : 나중에 들어온 데이터가 먼저 나간다.
# |       | => push(데이터) : 넣는데이터
# |       | => pop() : 마지막 값을 뽑아준다. 결과로 반환한다.
# |       | => isempty() : 비어있는지 체크하기 => 비어있으면 True 아니면 False
# |       | => size() :들어가있는 요소 갯수 체크
# |       | => top() : 맨 위의 값을 출력하기
# |_______|


# (1) 스택 객체를 생성하기
# 함수 -> 메서드 / 데이터,변수-> 속성
# def __init__() <- 생성메서드(함수), 생성자
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


stack = Stack()

# 코딩 - 게으른 얘들....
#   귀찮아서.. 2번학서 잔머리굴려서 1번할려고 노력을 함ㅎㅎㅎ 15줄 자리는 1줄에 
#   => 천재지만 최악의 개발자동료 => 나중에 다시짰다.
#   => 최적화 

# 'A'pus
stack.push('a')
stack.push('b')
stack.push('c')
print(stack.l)
stack.pop()
print(stack.l)
stack.pop()
print(stack.l)
stack.pop()
print(stack.l)
stack.pop()
print(stack.l)








