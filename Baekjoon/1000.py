'''
A+B https://www.acmicpc.net/problem/1000

문제) 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력) 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
ex)
1 2

출력) 첫째 줄에 A+B를 출력한다.
'''

# print() : 콘솔(터미널)에 한줄 출력함수
# 변수 = input() : 콘솔에서 키보드로 한줄 입력받는 함수
# - 입력내용을 사용할려변 반드시 변수에 저장
# - input() 입력받은 데이터는 무조건 문자열이다.

# type(데이터) : 어떤 타입인지 알려주는 함수
# int(데이터) : 정수타입으로 변환하기

w = input()
# <class 'str'> : str타입이다.

# 문자열변수.split("구분인자") :  문자열 => 리스트
w = int(w.split(' '))

# a,b 변수 할당
# print(a, b)
a = int(w[0])
b = int(w[1])
# a = int(a)
# b = int(b)
print(a + b)
