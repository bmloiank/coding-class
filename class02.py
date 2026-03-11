'''
💪 수업 준비사항 💻
1. 하우코딩 수업 NIS 로그인
＊ID: agent@nis.com
＊PW: python
2.  VSCode LiveShare 링크 준비
'''

# <복습>
# 1. print(내용): 해당 내용이 출력이되는 함수
# 2. 변수 : 이름을 붙여서 데이터를 저장하는 공간(=메모리 RAM)
# 변수이름 = 데이터
# '=' 기호 : 변수에 저장하다(절대 같는 아니다. ==)

# 3. 데이터타입 : 데이터의 종류
# 3-1) 숫자 Number타입
# - 연산이 가능해요 : +,-,*(곱하기),/(나누기),//(몫),%(나머지),**(제곱)

today = 17

# 예제) 5와 3의 나눈 몫을 구해달라
print(5/3)  # 나누기 계산
print(5//3) # 몫
print(5%3)  # 나머지


# 예제) 3의 배수를 구하여라 (3으로 나눴을 나머지가 0) => 조건문

# 예제) 반지름이 5인 원이 있다. 이때ㅢ 원의 넓이를 구해주라. (원주율 3.14로 계산)
r = 5
s = (r**2)*3.14
print(s) # 소수
print(int(s)) # 소수를 버려서 정수로 만들게된다.
print(float(r))

# *숫자 종류 - int() 정수(양의정수, 0, 음의정수)
#         - float() 유리수(분수, 소수)
# - 소수를 정수로 만들기 int(숫자)
# - 정수를 소수로 만들기 float(숫자)




# 3-2) 문자열 String타입  "", ''
# - 문자 : 숫자빼고 전부(알파벳, 한글, 특수문자!@#$%^&*(), 띄어쓰기 ' ', 줄바꿈\n)
# - 연산자 : 문자열+문자열(이어서 붙이기), 문자열*숫자(반복해서 이어붙이기)
# - 문자열을 문자가 여러개 이루어져있기때문에 길이(=크기, 갯수)를 구할수가 있습니다.
#   len(데이터) : 데이터의 길이를 출력해준다.

print("Hello World!")

#예제) 변수 "안녕하세요" 와 "좋은 아침입니다." 변수만들고 두 변수를 이어서 붙여주세요.
hello = "안녕하세요."
g = "좋은아침입니다."
print(hello + "\n" + g)
# 예제) "안녕하세요" 10번정도  반복해서 말해주세요.
print(hello * 10)
print(len(hello))

############################################
print("mission 01=============")
# 정상적인 512자 데이터를 찾기

file_a = 'ajkek__ihhfyfy7867gjk_,hi_bjfuky_gfu,hjkshfkyf_jgeu______,leieowry#ekh_iehkfejewjgdfe_48635ihf64___,guulhf_h,gdtj#gg#g65_ffy74764645v84djhf#uh8y__,h_jmehie##hejukjvd__,648fd7sgk4dl#k3_jhr82tej#223_______,___'
file_b = 'djhfaheu___wehiehrhlsfhouhewwehr1238364892hrehwfwhelhewlehrlewhiorhhf3824863___883@hre93734084fdfhieelwhfhiei#startmyg^efac^pohSkcans^tekram^ytisrevinu^erotStnemtraped^llaHytic^krap^tnaruatser^retaehTeivomend#hfdhsifohifeifhlk368537djs89hds83e____89fwgafg3dbsjhgdiutwfw823___t93g3%@iu3977e&egd37dheehdgsaioiowi'
file_c = 'asdfgwheu2963__jewjeyjkejeygey7627#36825h___,__d#ufigwfk,dfuigeuwke__,s324dfekd7he68___,jehkfk,fk73r#hkg743gjgu_,68fthk__#hfyu744ch_,ds##e_________####u#__,#j_#ab__,#nbu#_b_a_bb_b#bbbbrbby__##bb__bb##3#bb#1b_bb__,,bbbb#th_,64hdd##jdueh#hd72_,jey8___,37dek7dejebwjwkey1n_,ju,,_jeuwweejgeekeur_jege8363jfbdk'

print(len(file_a))
print(len(file_b))
print(len(file_c))
print(len(file_a + file_c))
# 조합한 데이터를 변수에 저장해서 출력해봅시다!
file = file_a + file_c
print(file)


#################################################
# 문자열 : 문자가 여러개구성되어 있다.
# - ⭐ 순서(=인덱스,0번부터 숫자를 센다.)가 존재합니다.
# - ⭐ 해당 인덱스번째의 문자를 뽑기 = 인덱싱 
#   ⭐ 문자열변수[인덱스]
# - 시작부터~ (끝-1)까지 잘라주세요.= 슬라이싱
#   문자열변수[시작인덱스:끝인덱스] 


alphabet = 'abcdefghijklmnopqrstuvwxyz'
# - 왼쪽부터 세면 0,1,2,3,4
# - 오른쪽부터 세면(제일마지막, -1번째다)-5-4-3-2-1 


# alphabet에서 0번째 문자를 뽑아봅시다. (결과 'a')
print(alphabet[0])
# alphabet에서 마지막 문자를 뽑아주세요. (결과 'e')
print(alphabet[-1])


# alphabet에서 4번부터 10번앞에서(9번까지) 자르고싶어요. => 슬라이싱
# 시작번호 : 4
# 끝번호 : 10(9번까지 나오게됩니다.)
print(alphabet[4:10])



print("mission 02=============")
# file에서 360~429번까지의 데이터를 뽑아줘
# 시작 인덱스 : 360
# 끝 인덱스 : 430
print(file[360:430])
# __,#j_#ab__,#nbu#_b_a_bb_b#bbbbrbby__##bb__bb##3#bb#1b_bb__,,bbbb#th_,




# print()
# len()
# 1 + 1
# a=1

