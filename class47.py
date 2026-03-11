# # 함수 


# and 

# , end=''


# print(): 한줄에 한개씩 작성이 된다. 
# - 끝 마무리가 \n(줄바꿈) => 끝마무리를 변경가능 end=""
#
print("안녕하세요.",end="")
print("반갑습니다.")

'''
파이썬 데이터타입 => 객체

<수학>
+,-,*,/,//,%,**(제곱)
round(숫자) : 반올림
abs(숫자)   : 절대값
math.sqrt(숫자) : 제곱근(루트)  **0.5(고2)
math.ceil  : 올림
math.floor : 내림

#------
math.comb(n,k) : 경우의수 - 조합
maht.perb(n,k) : 경우의수 - 순열 => 팩토리얼


<문자열 내장메서드>
문자열.내장메서드

(1) 문자열.upper()/.lower()/.capitalize()/.title()/.swapcase() : 대문자/소문자/앞글자만대문자/단어당 앞글자/대소문자형태바꿈
(2) 문자열.strip(" ") : 양쪽의 문자열을 지우기
    문자열.rstrip(" ") 
    문자열.lstrip(" ") 
(3) 문자열.replace("찾는문자","바꿀문자) : 찾아서 바꾸기
(4) 문자열.find("찾는문자")  : 찾는문자의 인덱스를 출력해주는 함수 없으면 -1 
(5) 문자열.index("찾는문자") : 찾는문자의 인덱스를 출력해주는 함수 없으면 error (리스트)
(6) 문자열.count("찾는문자") : 찾는문자의 갯수가 나오게된다. (리스트도 가능)
(7) 문자열.split("찾는문자") : 
(8) "구분인자".join("찾는문자")
(9) "문자열".isalpha() : 문자열에서 알파벳으로만 이루어져있는가
    "문자열".isdigit()/.isdecimal()/.isnumberic() : 숫자로만 이루어져있는가?

(10) "문자열".zfill(갯수) : 0으로 채우기

# \0 => c언어 null 파이썬 보이지않는 문자열 공백
# \n , \t






'''

text = "         _____ 실제로 존재한다 ____     "
print(text.lstrip(' '))

s = "aaaabbb"
lst = ["a","a","a","a","a","b"]
print(s.index('b'))
print(s.find('b'))

print(s.count('a'))
print(lst.count('a'))
print(lst.index("b"))


print("안녕 \t 하세요.")
print("1".zfill(6))
print(f"{1:06}")


1+2
print(6 and 3    )




'''
#<문자열 포멧팅 TODO => 프로젝트성>

(1) f-string(파이썬 최신식 3.9버전 )

f"문자열 {변수}"



(2) % 포맷팅(최초의방식, c언어방식)
print("문자열 %포맷팅문자1 %포맷팅문자2 " % (변수1, 변수2) )
- %s : 문자열
- %d : 10진수(decimal)
- %f : 실수
- %b : 2진수
- %x : 16진수


(3) str.format() : 기존에 쓰던 python방식
print("문자열 {} 문자열 {} 문자열 {}".format(변수1,변수2,변수3))
print("문자열 {a} 문자열 {b} 문자열 {c}".format(b=변수1,a=변수2,c=변수3))



TIP) 자리수 맞추기
- 자리수가 5자리 & 채울문자를 0 -(공백)
- 숫자는 오른쪽 정렬
- 문자는 왼쪽정렬

정수 {변수:05d}
           실수 {변수:07.3f}  : 전체 7자리 / 소수점 아래3
             문자열 {변수:<5s}  < 왼쪽정렬 > 오른쪽정렬 ^ 가운데정렬

             

'''

text1 = "abcde"
text2 = 1
text3 = list("abcde")
text4 = {'k':'v'}
text5 = 0.5
print(f"알파벳은:{text4}")
print('text1 = %s text2 = %d text5 = %f' % (text1, text2, text5))
print("text1 = {a} text2 = {v}  text5 = {c}".format(a = text1, c = text5, v = text2))
h = 1
m = 1
s = 1
ms = 7.123456 #(소수점아래 3)
pm = "오후"
print(f'{pm:*^6s} {h:02d}시 {m:02d}분 {s:02d}초 {ms:-9.3f}')
print('{:*^6s} {:02d}시 {:02d}분 {:02d}초 {:-9.3f}'.format(pm, h, m, s, ms))
print('%02d 시 %02d 분 %02d 초 %09.3f' %( h, m, s, ms))