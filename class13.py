'''
1. 내가 지금 사용하고 있는 데이터의 타입
2. 내가 뭐하고 싶으지를 잘 정리해보세요. => 함수
3. 갖고있는 타입과 하고싶은 함수의 타입 다른 경우
- 타입을 변경해줘야한다.

<타입변환>
0. type(데이터) : 해당데이터의 타입을 알려주는 함수 
1. int(데이터) : 데이터를 숫자로 변환
2. str() : 숫자를 문자로 변경
3. .split("구분인자") : 문자열 구분인자를 기준으로 쪼개서 리스트만들기 
4. "".join() : 리스트를 합쳐서 문자열로 만들기

'''

num1 = "1"
num2 = "3"

# 예제1)숫자 num1과 숫자 num2더한 결과를 받아고싶습니다.
# integer

num1 = int(num1)
num2 = int(num2)
print(num1 + num2)


# 예제2)주어진 숫자가 몇자리숫자인지 출력해주세요.
# str() : 숫자를 문자로 변경
num3 = 1897  # 4자리숫자
num3 = str(num3)
# a = int(len(num3))
print(len(num3))


# 리스트를 문자열로 바꾸고싶어요. 
# [1,2,3,4] => ['1','2','3','4']
# "".join() : 리스트를 문자열로 합쳐서 만드는 것 ['1','2','3','4'] => '1234'
print(type(['1','2','3','4']))



#########################################################

'''
<데이터타입>
-----단일데이터
1. 숫자
2. 문자열
3. bool
-----다중데이터
4. 리스트 []
0번 *순서* 찾으면 0번째값이 나옵니다.

5. 딕셔너리 dictionary 
형태 : {key:value, key1:value1, key2:value2}
"apple" *단어* 찾으면 "사과"나옵니다.
: key(찾는단어) - value(나오는 값)

'''

# 예제: 영어단어
# 과일이름 Key:영어단어 / value:한글단어
d = {'apple':'사과', 'banana':'바나나', 'cherry':'체리'}

# d딕셔너리에 'cherry' 뽑아보기  
# => (1) 인덱싱이랑 유사 : 딕셔너리변수[key] => 인덱스는 범위밖으로 벗어나면 Error
# => (2) 딕셔너리.get(key) => 없으면 없다고 정상적으로 처리
print(d['cherry'])
print(d['banana'])
print(d.get('apple'))
print(d.get('mango'))



############################################################
print("------------")
# 종류가 거래trade인

# log 리스트안에 딕셔너리가 있는 데이터타입
log = [
    {'time':'1014','ip':'89.149.233.0','type':'trade','item':'wiz asset','price':40000,'id':'502yo4'},
{'time':'1016','ip':'89.149.233.1','type':'download','item':'None','price':0,'id':'rtw1517'},
{'time':'1305','ip':'89.149.233.3','type':'trade','item':'star asset','price':10000,'id':'eop00'},
{'time':'1315','ip':'89.149.233.6','type':'trade','item':'q energy','price':10000,'id':'versit808'},
{'time':'1253','ip':'89.149.233.9','type':'trade','item':'ms ent','price':2700,'id':'vsf7'},
{'time':'1400','ip':'89.149.233.12','type':'trade','item':'wiz asset','price':10000,'id':'ge3298'},
{'time':'1253','ip':'89.149.233.10','type':'trade','item':'ms ent','price':2700,'id':'hdus8'},
{'time':'1253','ip':'89.149.233.17','type':'trade','item':'ms ent','price':2700,'id':'tau200'},
{'time':'1508','ip':'89.149.233.20','type':'trade','item':'wiz asset','price':45000,'id':'haha160'},
{'time':'1510','ip':'89.149.233.26','type':'download','item':'None','price':0,'id':'bus328'},
{'time':'1500','ip':'89.149.233.30','type':'trade','item':'wiz asset','price':5000,'id':'son1257'},
{'time':'1144','ip':'89.149.233.20','type':'trade','item':'q energy','price':10000,'id':'fury01'},
{'time':'1400','ip':'89.149.233.32','type':'download','item':'ms ent','price':9000,'id':'bew02'},
{'time':'1400','ip':'89.149.233.39','type':'trade','item':'wiz asset','price':10000,'id':'fightclub'},
{'time':'1122','ip':'89.149.233.42','type':'download','item':'None','price':0,'id':'young0'},
{'time':'1300','ip':'89.149.233.43','type':'trade','item':'q energy','price':10000,'id':'kywu1'},
{'time':'1020','ip':'89.149.233.45','type':'trade','item':'ms ent','price':2700,'id':'wyue1'},
{'time':'1400','ip':'89.149.233.42','type':'download','item':'None','price':0,'id':'terra133'},
{'time':'1300','ip':'89.149.233.55','type':'download','item':'None','price':0,'id':'sdyt2387'},
{'time':'1046','ip':'89.149.233.48','type':'trade','item':'star asset','price':1800,'id':'sdk547'},
{'time':'1000','ip':'89.149.233.52','type':'trade','item':'q energy','price':10000,'id':'jjkw4'},
{'time':'1048','ip':'89.149.233.3','type':'trade','item':'wiz asset','price':5000,'id':'wyre97'},
{'time':'1210','ip':'89.149.233.54','type':'trade','item':'star asset','price':40000,'id':'jaeh3'},
{'time':'1055','ip':'89.149.233.13','type':'trade','item':'ms ent','price':2700,'id':'tool2345'},
{'time':'1353','ip':'89.149.233.48','type':'trade','item':'wiz asset','price':5000,'id':'lala20'},
{'time':'1400','ip':'89.149.233.2','type':'download','item':'None','price':0,'id':'vnv379'}]

# 정답여러개 : 정답 리스트 만들어서 출려해주기
s = []
for i in range(len(log)):
    # 'type' 키
    #print(log[i])
    q = log[i] # q 딕셔너리
    #print(q['type'])
    if q['type'] == 'trade':
        #print(q)
        s.append(q)
print(s)



print("------------")
# 미션1의 정답(s)에서 종목이 'wiz asset' 인것 찾아보기
k = []
for i in range(len(s)):
    # print(s[i]) 
    x = s[i]
    if x['item'] == 'wiz asset':
        #print(x)
        k.append(x)
print(k)


print("------------")
# 정상적인거래 10000 아닌것들을 찾아라
j = []
for i in range(len(k)):
    y = k[i]
    if y['price'] != 10000:
        # print(y)
        j.append(y)
print(j)



# (1) 과자 이름과 가격을 저장하는 딕셔너리를 만들어주세요.
snack = {'포카칩':1550, '양파링':1480, '새우깡':1400, '포테토칩':1480, '오감자':1300}
# (2) 아이스크림 딕셔너리가 있다.
ex = {"메로나" : 1200, "탱크보이" : 1800, "빠삐코" : 800, "요맘때":1500}

# 빠삐코의 가격을 출력해보자
print(ex['빠삐코'])
# 탱크보이의 2개의 가격을 출력해보세요.
print(ex['탱크보이']*2)
# 캔디바의 가격을 출력해보세요. 
# => 인덱싱 : 항목이 반드시 있고, 일정할때
# => .get('key') : 어떨땐 있고, 어떨땐 없을수 잇는 key
# print(ex['캔디바'])
print(ex.get('캔디바'))