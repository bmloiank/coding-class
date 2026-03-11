'''
<딕셔너리에서 값을 뽑는 방법> 
(1) 인덱스 처럼 뽑기 : 딕셔너리이름[key]
- key값가 없으면 Error
(2) .get(key)
- key값이 없으면 None


<딕셔너리의 특별한 접근 => 리스트만들고싶다.>
(1) .keys()   : 딕셔너리의 모든 key값들만 뽑아서 리스트만들고싶어
(2) .values() : 딕셔너리의 모든 value값들만 뽑아서 리스트만들고싶어
(3) .items()  : 딕셔너리의 모든 key-value값들만 뽑아서 리스트만들고싶어
=> 딕셔너리의 반복

<딕셔너리의 반복>
for k,v in 딕셔너리.items():
    k: key값
    v: value값
'''


text = '1234'
# 문자열변수.isalpha() : 문자열이 알파벳으로만 이루어져있냐?
# 문자열변수.isdigit() : 문자열이 숫자로만 이루어져있는가?
print(text.isalpha())
print(text.isdigit())

print("mission1 ========")
# 범인의 수상한 거래내역을 고르시오
# -> memo 에 모스부호가 들어간 데이터를 뽑아보기
# -> memo에 들어간값이 영어가 아니면 => 모스부호
a_list = []
account_details =[
    {'date':'0201','type':'withdraw','account':'211-854-6681','amount':132500,'memo':'-..'},
    {'date':'0205','type':'withdraw','account':'121-554-1820','amount':106000,'memo':'--'},
    {'date':'0205','type':'withdraw','account':'211-157-3580','amount':130000,'memo':'---'},
    {'date':'0207','type':'deposit','account':'202-3207-8819','amount':50000, 'memo':'Jovia'},
    {'date':'0201','type':'pay','account':'554-6280-7772','amount':100000,'memo':'Emily'},
    {'date':'0201','type':'withdraw','account':'111-554-6880','amount':123000,'memo':'-.'},
    {'date':'0201','type':'withdraw','account':'428-7190-5471','amount':167000,'memo':'.-'},
    {'date':'0204','type':'deposit','account':'260-415-2919','amount':16000,'memo':'John'},
    {'date':'0204','type':'withdraw','account':'211-854-6720','amount':180000,'memo':'..-.'},
    {'date':'0201','type':'withdraw','account':'115-854-1280','amount':230000,'memo':'..'},{'date':'0202','type':'withdraw','account':'131-555-6000','amount':251000,'memo':'-.'},{'date':'0203','type':'deposit','account':'243-31-5325','amount':15000,'memo':'Nugu'},{'date':'0204','type':'deposit','account':'463-433-0205','amount':7050,'memo':'Samuel'},{'date':'0201','type':'withdraw','account':'221-554-6880','amount':300000,'memo':'-..'},{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':113700,'memo':'--'},{'date':'0204','type':'deposit','account':'206-415-2919','amount':16000,'memo':'Harry'},{'date':'0201','type':'withdraw','account':'628-7490-5471','amount':213700,'memo':'---'},{'date':'0201','type':'withdraw','account':'128-2196-5471','amount':113700,'memo':'-.'},{'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-'},{'date':'0204','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..-.'},{'date':'0201','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..'},{'date':'0202','type':'withdraw','account':'131-554-6000','amount':221000,'memo':'-.'},{'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},{'date':'0204','type':'deposit','account':'2463-433-0205','amount':7050,'memo':'Samuel'},{'date':'0201','type':'withdraw','account':'111-554-6880','amount':300000,'memo':'-..'},{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':313700,'memo':'--'},{'date':'0204','type':'deposit','account':'2060-415-2919','amount':16000,'memo':'Ann'},{'date':'0204','type':'withdraw','account':'111-554-6880','amount':320000,'memo':'---'},{'date':'0201','type':'withdraw','account':'111-554-6880','amount':24000,'memo':'Betty'},{'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},{'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Norman'},{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':371200,'memo':'-.'},{'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-'},{'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Betty'},{'date':'0202','type':'withdraw','account':'131-554-6000','amount':1000,'memo':'DrFisher'},{'date':'0204','type':'withdraw','account':'2463-433-0205','amount':7050,'memo':'Samuel'},{'date':'0204','type':'withdraw','account':'111-554-6880','amount':530000,'memo':'..-.'},{'date':'0201','type':'withdraw','account':'111-554-6880','amount':130000,'memo':'..'},{'date':'0202','type':'withdraw','account':'131-554-6000','amount':109400,'memo':'-.'}]

# 정답이 많으니깐 리스트로 만들어보자.

for i in range(len(account_details)):
    a = account_details[i]
    a_memo = a.get('memo')
    if a_memo.isalpha() == False:
        print(a)
        a_list.append(a_memo)

print(a_list)


print("mission2 ========")
# 딕셔너리에서 추가,수정,삭제
# 딕셔너리['key'] = 데이터 
# - key 원래 없었어 => 새로 추가하기
# - key 원래 있으면 => 수정

# 모스부호 사전 리스트 두개로 딕셔너리 만들기
# ".-" => "A"
morse_dic = {}
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(len(morse_code))
print(len(alphabet))
for i in range(len(morse_code)):
    print(morse_code[i])
    print(alphabet[i])
    morse_dic[morse_code[i]] = alphabet[i]
print(morse_dic)    



print("mission3 ========")
# mission1 a_list를 morse_dic을 사용해서 해독해라.
# 문자열로 하나로 합치기
decode = []
for i in range(len(a_list)):
    # 문자열 str
    # 문장 txt
    # 문자 char, c
    c = morse_dic.get(a_list[i])
    decode.append(c)
# "구분인자".join(리)
print(''.join(decode))


# 5. 딕셔너리 {}
# 6. 튜플 () -> 딕셔너리.items()
# - 리스트랑 거의 동일합니다.
# - 수정할수없는 데이터. 고정

# 7. 집합 {} - 고등1 수학내용

alpha = ('a','b','c','d','e')
# print(alpha.append('f'))
# 0번째값을 'f'수정하기
alpha[0] = 'f'
print(alpha)