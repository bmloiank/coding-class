# 정렬 알고리즘

# (1) 기본 sort() : 원본을 바꾸기
# (2) sorted()   : 정렬된 리스트가 나온다.
# -> 기본 : 오름차순
# -> reverse= True : 내림차순로 변환하기 
lst = [1,-4,-5,16,-2,38,-24]
print(lst[1])
lst.sort()
print(lst[1])
print(lst)
lst.sort(reverse=True)
print(lst[1])
print(lst)
print()
lst = [1,-4,-5,16,-2,38,-24]
llst = sorted(lst,reverse=True)
print(lst,'--', llst)
print()

# 문자열 정렬 => 사전순(https://blog.kakaocdn.net/dna/bv2U5P/btqRVpHiKo4/AAAAAAAAAAAAAAAAAAAAAKFc9Z79Mx3giAfi7adckwP1Q87rBYRcuTbEDp_pT51l/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1759244399&allow_ip=&allow_referer=&signature=%2FRQ1lV5xrfzFWyPqG007Otc8l68%3D)
# 내용.sort(욥션)
# sorted(내용, key=, reverse=)
# - reverse = False : 내림차순 오름차순
# - key = 함수이름 (반드시, 매개변수 1개만 넣을 수 있는 값)
# 

alpha = ['aa','ab','ae','ac','ba','bc']
alp = sorted(alpha, reverse=True)
print(alpha, '--', alp)
alpha = ['가','갸','그','기','고','구']
alp = sorted(alpha, reverse=True)
print(alpha, '--', alp)


num = ['-11','1','-21','22','-123', '1234']
num1 = sorted(num)
print(num, '--', num1)

def customabs(n):
    return abs(n)
# 글자 갯수를 기준으로 정렬하고싶어. => 기준을 변경 key
# num.sort(key=len)
# 절대값이 큰 기준으로 정렬하고싶어. abs()

# lambda 매개변수: a  
num = list(map(int,num))
num.sort(key=customabs)
num.sort(key=lambda x:abs(x))
print(num)



# 복합정렬
people = [
    ("주하",268),
    ("철수",268),
    ("짱구",390),
    ("유리",387),
    ("훈이",179),
    ("맹구",179)
]

#점수로 오름차순으로 정렬하다가, 동점일경우 가나다라 순으로 정렬하고 싶다.
people.sort(key=lambda x: (x[1],x[0]))
print(people)








'''
iterable객체 : 반복가능한객체

for 반복변수 in 반복조건(iterable객체):
:반복조건이 하나씩 꺼내서 나올때까지 반복하는게 for문

(1) for i in range(숫자)
range(n) : 0-n-1까지의 연속된 정수의 모임

(2) 순서(인덱스)를 갖는 데이터타입 => 문자열, 리스트, 튜플
(3) 묶음(콜렉션) 데이터타입 => 리스트,range(), 딕셔너리,튜플,집합


while 조건표현식:
조건표현식 => true/false
(1)비교연산자
(2)논리연산자
(3)포함연산자

'''


print(list(range(10)))

text = 'python'


for i in text:
    print(i)
alpha = ['aa','ab','ae','ac','ba','bc']
for i in alpha:
    print(i)



d = {"key":'value',"key1":'value1',"key2":'value2',"key3":'value3'}

for i in d:
    print(i)
for k,v in d.items():
    print(k,v)






# 뒤집기
# 리스트.reverse()
# reversed(리스트)
lst = [1,-4,-5,16,-2,38,-24]

lst.reverse()
print(lst)

print(reversed(lst))
# print(lst)


# 문자열 뒤집기[::-1]
text = 'python'
print(text[::-1])


# 변수 : 데이터를 저장하는 공간(메모리)
# 파이썬 디테일한 데이터 개념상식
# mutable(변하기쉬운) immutable(변하지않는)
# (1)immutable(변하지않는)
# - 값을 바꿀수 없는 객체
# - 바꿀려고 하면 새로운 객체를 만들어야하는 것
# - int(), float(), str()


# (2)mutable 객체
# - 값을 바꿀수 있는 객체


# 컴퓨터 구조~~~~~
a=1
print(a, "메모리 id",id(a))
b=['a','b',3]
print(b, "메모리 id",id(b))
a=2
print(a, "메모리 id",id(a))
b[0]='c'
print(b, "메모리 id",id(b))
# print(a, "메모리 id",id(a))