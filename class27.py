'''
객체지향프로그래밍(OOP, Object-Oriented Programming)
프로그램 설게방법 이론

절차형 프로그래밍(함수형태로 순서대로, 설계할때 순서)
객체지향프로그래밍(대상을 기준으로 하는 프로그래밍)

* 객체(Object)?
: 속성(데이터,변수)와 메서드(기능,함수)을 동시에 갖는 대상
- 문자열 메서드=> 문자열변수.upper() 


class 클래스 : 객체의 틀, 레시피, 설계도                => def
instance 인스턴스 : 클래스를 사용해서 만들어진 실물객체     => 호출

'''

text="객체지향프로그래밍"
print(type(text))


# class 클래스이름:        # 이름규칙 PascalCase
#   생성자: __init__메서드 
#   - 객체를 생성할때 첫 실행하 내용을 적는 메서드
#   - 보통은 초기값 셋팅
#   메서드 주의사항
#   - 첫번째 매개변수에는 무조건 self(나 자신) : self 클래스 내부 속성과 메서드를 접근하기
#   속성만들때 주의사항
#   - self.속성명 = 데이터 : 클래스 내부 사용할 데이터는 속성으로 저장할것
#   - 그렇지 않는 데이터는 일반 변수에 담아준다.

# 사람 객체를 만들어보기
# - 이름 :
# - 성별 :
# - 나이 :
# - 키:

class Human2:
    def __init__(self):
        self.name = '박주하'
        self.gender = '여'
        self.old = 15

class Human:
    # 생성할데이터를 받고자하면 매개변수에 추가
    def __init__(self, name, gender, old):
        self.myname = name
        self.mygender = gender
        self.myold = old

    # 자기소개 메서드 : "내 이름은 ____이고 내 나이는___살이야."
    def intro(self):
        # f-string:  문자랑 변수를 같이 쓸때 포멧을 편하게
        # f"문자열 {변수}"
        print(f"내 이름은 {self.myname}이고 내 나이는 {self.myold}살이야.")
        # print('내 이름은', self.myname + '이고 내 나이는', self.myold + '살이야.')

    # 나이를 한살먹는 메서드
    def grow(self):
        self.myold += 1
    

# 인스턴스 생성
# 인스턴스명=클래스이름()
juha = Human2()
juhapark = Human('박주하', '여', 15)
hj=Human('이현지',"여",20)
jjang=Human('신짱구',"남",5)

# 인스턴스이름.속성명 / 인스턴스이름.메서드()
print(juha.name)
print(juhapark.myname)
print(jjang.myold)
juhapark.intro()
jjang.intro()
jjang.grow()
jjang.intro()


################## 과제 ########################
# =============================================
# Calculator 클래스 설계
# ---------------------------------------------
# ✅ 클래스 이름: Calculator
#
# ✅ 속성 (Attributes):
# - value: 현재 계산된 값 (초기값은 0)

# ✅ 메서드 (Methods):
# - add(x): 현재 값에 x를 더함
# - subtract(x): 현재 값에서 x를 뺌
# - multiply(x): 현재 값에 x를 곱함
# - divide(x): 현재 값을 x로 나눔 (0으로 나누기 예외 처리)
# - clear(): 현재 값을 0으로 초기화
# - get_value(): 현재 값을 결과로 내보내기 = return

class Calculator:
    def __init__(self):
        self.value = 0
        # self.x = x
    def add(self, x):
        # 굳이 모든 데이터에 대해서 속성으로 다룰필요는 없다.
        self.x = x
        self.value += self.x
        # print(self.value)
    def subtract(self, x):
        self.x = x
        self.value = self.value - self.x
        # print(self.value)
    def multiply(self, x):
        self.x = x
        self.value = self.value * self.x
        # print(self.value)
    def divide(self, x):
        self.x = x
        if self.x != 0:
            self.value = self.value / self.x
        # print(self.value)
    def clear(self):
        self.value = 0
        # print(self.value)
    def get_value(self):
        print(self.value)
        return self.value
kk = Calculator()
kk.add(2)
kk.subtract(4)
kk.multiply(2)
kk.divide(2)
kk.get_value()




