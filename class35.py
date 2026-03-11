# 16번컨테이너를 찾기

# 선박(배):스택구조로 물건을 쌓기
#cargoship


# cargo(화물번)
import random
random.seed(66)
cargolist = [10, 35, 1, 2, 31, 5, 18, 19, 20, 21, 22, 4, 23, 15, 16, 17, 34, 7, 8, 30, 3, 24, 9, 36, 37, 38, 39, 14, 27, 28, 29, 25, 26, 6, 11, 12, 13, 33, 32]
random.shuffle(cargolist)

print(cargolist)


# 객체(데이터+기능)
# - 객체 정의(클래스, 틀을 어떻게 만들지)
# - 실물 객체(인스턴스)

# 객체: 속성(데이터) + 메서드(기능)
# 메서드 안에 (보통은 init, 다른 메서드)
# - self.속성명 (변수)
# 메서드 def ()

# <__main__.Stack object at 저장된 메모리 주소(0x0000023B35036E40)>


class Stack:
    # __(언더스코어) : 비밀스러운(private) 변수/함수
    # (1)생성자 : 생성할때 실행하는 메서드 => 속성의 초기값(맨처음값)을 겟팅
    def __init__(self, x):
        # l속성에는 리스트
        self.l = x

    # (2)__str__ : (사람용)객체를 문자열로 표현할때 요방식으로 표현하시오.를 지정하는 메서드
    def __str__(self):
        return " ".join(self.l)

    # (3)__repr__ : (컴퓨터시스템적으로 디버깅용) 문자열
    # -> 회사들어가서 쓰기^^
    def __repr__(self):
        return " "




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
        

# 화물(cargolist)을 내리기
# => 마지막값을 먼저내리기 => LIFO => 스택




# 1. cargolist를 스택으로 만들어주기
cg = Stack(cargolist)

# 2. 시뮬레이터
# (1) 맨 마지막값을 뽑아서
# (2) 소형화물선에 넣기로 했다. => stack
# (3) 소형화물선을 5개가 차면 출발합니다.
#     => 내용을 비우기, 다음번호로
#    
# (4) 16번 컨테이너(뽑은 값 = 컨테이너)가 몇번 소형화물선에 있는가?


sship = Stack([])
snum = 1
while cg.isempty() == False:
    pop = cg.pop()
    # 뽑았어
    sship.push(pop)
    if pop == 16:
        print(snum)
    # 현재까지 5개 되었어 => 비워내용
    # print(snum, sship.l)
    if sship.size() == 5:
        sship = Stack([])
        snum = snum + 1




cg.push("hi")
print("인스턴스(객체=데이터+메서드)",cg)
print("인스턴스의 l속성을 가져와라",cg.l)

    







