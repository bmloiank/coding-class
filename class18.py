# 정보올림피아드(https://koi.or.kr/) : 5월 
# - 온라인 : 
# - 3시간 4문제 다맞으면 - 취업 납치 / 3문제 맞으면  / 2문제 잘하네 / 1문제 기본있다 
# => 코딩테스트
# => 
 
'''
함수형 프로그래밍 

함수 : 코드 묶음 => 하나의 기능
=> 재사용성

<정의단계 : 함수를 만들기>
def 함수이름():
    코드

    
<호출단계 : 함수를 사용하기>
함수이름()

'''

# "안녕하세요" 출력하는 hello 함수를 만들기
def hello():
    print('안녕하세요')
    
hello()


#   \ 입력:5  /
#  -         -----------
# |   ㅁ + 3 =          |
# |                    |
# --------------
#                / 결과:8 \   

'''
<정의단계 : 함수를 만들기>
- 매개변수 : 함수에서 입력받은 데이터를 저장하는 변수
- return : (1) 결과를 내보내주기
           (2) 함수를 종료
def 함수이름(매개변수):
    코드
    return 결과값

    
<호출단계 : 함수를 사용하기>
- 인수 : 함수 사용시 넣을 데이터
함수이름(인수)


'''

int("12")


# 숫자를 입력하면 +3을 계산하는 plusThree함수를 만들어보기
def plusthree(num):
    print(num + 3)
print(plusthree(5))

# x^2+3x+2 함수 값을 구하라 
def second(x):
    return x**2 + 3*x + 2
print(second(1)+3)

print("missin 1 ===========")
account_details =[
    {'date':'0201','type':'withdraw','account':'211-854-6681','amount':132500,'memo':'-..', 'atmSection':'PA1101'},
{'date':'0205','type':'withdraw','account':'121-554-1820','amount':106000,'memo':'--', 'atmSection':'FG1001'},
{'date':'0205','type':'withdraw','account':'211-157-3580','amount':130000,'memo':'---', 'atmSection':'HT1010'},
{'date':'0207','type':'deposit','account':'202-3207-8819','amount':50000, 'memo':'Jovia'},
{'date':'0201','type':'pay','account':'554-6280-7772','amount':100000,'memo':'Emily'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':123000,'memo':'-.', 'atmSection':'PA1101'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':167000,'memo':'.-', 'atmSection':'FG1001'},
{'date':'0204','type':'deposit','account':'260-415-2919','amount':16000,'memo':'John'},
{'date':'0204','type':'withdraw','account':'211-854-6720','amount':180000,'memo':'..-.', 'atmSection':'HT1010'},
{'date':'0201','type':'withdraw','account':'115-854-1280','amount':230000,'memo':'..', 'atmSection':'PA1101'},
{'date':'0202','type':'withdraw','account':'131-555-6000','amount':251000,'memo':'-.', 'atmSection':'FG1001'},
{'date':'0203','type':'deposit','account':'243-31-5325','amount':15000,'memo':'Nugu'},
{'date':'0204','type':'deposit','account':'463-433-0205','amount':7050,'memo':'Samuel'},
{'date':'0201','type':'withdraw','account':'221-554-6880','amount':300000,'memo':'-..', 'atmSection':'HT1010'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':113700,'memo':'--', 'atmSection':'PA1101'},
{'date':'0204','type':'deposit','account':'206-415-2919','amount':16000,'memo':'Harry'},
{'date':'0201','type':'withdraw','account':'628-7490-5471','amount':213700,'memo':'---', 'atmSection':'FG1001'},
{'date':'0201','type':'withdraw','account':'128-2196-5471','amount':113700,'memo':'-.', 'atmSection':'HT1010'},
{'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-', 'atmSection':'PA1101'},
{'date':'0204','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..-.', 'atmSection':'FG1001'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..', 'atmSection':'HT1010'},
{'date':'0202','type':'withdraw','account':'131-554-6000','amount':221000,'memo':'-.', 'atmSection':'PA1101'},
{'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},
{'date':'0204','type':'deposit','account':'2463-433-0205','amount':7050,'memo':'Samuel'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':300000,'memo':'-..', 'atmSection':'FG1001'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':313700,'memo':'--', 'atmSection':'HT1010'},
{'date':'0204','type':'deposit','account':'2060-415-2919','amount':16000,'memo':'Ann'},
{'date':'0204','type':'withdraw','account':'111-554-6880','amount':320000,'memo':'---', 'atmSection':'PA1101'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':24000,'memo':'Betty'},
{'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Norman'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':371200,'memo':'-.', 'atmSection':'FG1001'},
{'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-', 'atmSection':'HT1010'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Betty'},
{'date':'0202','type':'withdraw','account':'131-554-6000','amount':1000,'memo':'DrFisher'},
{'date':'0204','type':'withdraw','account':'2463-433-0205','amount':7050,'memo':'Samuel'},
{'date':'0204','type':'withdraw','account':'111-554-6880','amount':530000,'memo':'..-.', 'atmSection':'PA1101'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':130000,'memo':'..', 'atmSection':'FG1001'},
{'date':'0202','type':'withdraw','account':'131-554-6000','amount':109400,'memo':'-.', 'atmSection':'HT1010'}]

# 모스부호를 뽑기
# - 영어가 아닌 .isalpha()
# 


# print(type(account_details))
mor = []
for i in range(len(account_details)):
    # print(account_details[i])
    memo = account_details[i].get('memo')
    #print(memo)
    if memo.isalpha() == False:
        mor.append(memo)
print(mor)

# 모스부호 리스ㅌ 해독하는 함수 morse_list
# - 입력 : 모스부호(리스트)
# - 결과 : 알파벳(리스트)

# <딕셔너리에서 값을 뽑는 방법> 
# (1) 인덱스 처럼 뽑기 : 딕셔너리이름[key]
# - key값가 없으면 Error
# (2) .get(key)
# - key값이 없으면 None

def decode(morse_list):
    # Key: 모스부호 , value : 알파벳
    morse_dict = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'}
    reject = []
    for i in range(len(morse_list)):
        # print(morse_list[i])
        k = morse_list[i]
        print(morse_dict.get(k))
        reject.append(morse_dict.get(k))
    return reject
print(decode(mor))   





