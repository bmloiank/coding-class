# 알고리즘 => 머리 많이 쓰기, => 이공계(수학머리)

# 모듈 : 코드 블록 = 라이브러리
# - 특정 기능을 수행하는 코드 블록

# 수학모듈 math (https://docs.python.org/ko/3.13/library/math.html)
# +,-,*,/,%,**
# 제곱근(루트) 로그
# 올림, 내림

import math
import random
# math.변수이름
# math.함수이름()
# - 파이 pi 3.141592...

# (1) 반지름이 r인 원의 둘레를 구하시오
r=2 
l=2*math.pi*r
print(l)

# math.floor(데이터) : 소숫점을 버리고 싶다. 
print(math.floor(l))

# math.ceil(데이터) :소수점 올림
print(math.ceil(l))

# round(데이터,소수점 자리수)
print(round(l,5))



print("===랜덤모듈=======================")
# import random모듈 삽입하기 (https://docs.python.org/ko/3.13/library/random.html)

# (1) random.random() : 0~1 사이의 난수(random number)를 생성합니다. 
print(random.random())  # 0~9 => 1~10 i+1
# 0~9 정수 랜덤하게 나왔으면 좋겠는데 200~300
print(int(random.random()*100))
# 0~99 정수 랜덤하게 나왔으면 좋겠는데 3~30까지 랜덤

#(2) random.randrange(시작, 끝) 범위내에서 랜덤하게 뽑기
# 3~30까지 랜덤한 숫자를 뽑아주기
print(random.randrange(3, 30))

# 0~5까지(6개)) 랜덤한 숫자를 뽑고 선물주기
gift = ["a선물",'b선물','c선물','d선물','e선물','f선물']
for i in range(0,10):
    print(gift[random.randrange(0,6)])

# (3) random.choice(리스트) : 리스트중에서 하나를 뽑기
print(random.choice(gift))


# (4)random.shuffle(리스트)
random.shuffle(gift)
print(gift)









