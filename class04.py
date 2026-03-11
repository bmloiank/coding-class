# ⭐인덱스 (순서, 값위치): 0번부터 시작하기
# - ⭐인덱싱 문자열변수[인덱스] : 1개 뽑기
# - 슬라이싱 문자열변수[시작인덱스 : 끝인덱스]
#   

# 문자열변수.index("찾는 단어나 문자") : 해당 인덱스 번호를 알려준다.

print("mission 1======")
# start문자 end문자 이 두문자 사이의 힌트가 있다고 합니다.
file_b ='djhfaheu___wehiehrhlsfhouhewwehr1238364892hrehwfwhelhewlehrlewhiorhhf3824863___883@hre93734084fdfhieelwhfhieistart#.redro lacitebahpla yb kcatta trats eW .yti@sr@@evinu,tna@lp rae@@lcun,llam@ gni@@ppoh@s,lla@h@ y@tic,tekr@am kcots,noi@tats eci@l@op,ret@aeht:secalp gniwollof fo eno si tegrat ehT#endhfdhsifohifeifhlk368537djs89hds83e____89fwgafg3dbsjhgdiutwfw823___t93g3%@iu3977e&egd37dheehdgsaioiowi'

# (1) file_b에서 "start"문자가 몇번 인덱스에 있는지 구해서 출력해보자. 
# => 앞으로 모든 데이터는 변수로 관리하기
# => 109 296
print(file_b.index('start#.'))
s = file_b.index('start')
e = file_b.index('end')
print(e)
print(file_b[s + len('start') : e])
# start#.redro lacitebahpla yb kcatta trats eW .yti@sr@@evinu,tna@lp rae@@lcun,llam@ gni@@ppoh@s,lla@h@ y@tic,tekr@am kcots,noi@tats eci@l@op,ret@aeht:secalp gniwolllof fo eno si tegrat ehT#


print("mission 2======")
# 뒤집혀져있다. reverse
# => 문자열변수[::-1] : 문자열을 뒤집는기능하는 함수

code = file_b[s + len('start') : e]
print(code[::-1])
code = code[::-1]   # 기존에 변수가 있따면 새로운 데이터로 덮어쓰기 형태가 됩니다.
a = code.index(':')
b = code.index('. ')
print(a,b)
# ":"(콜론) 다음부터 장소가 ". " 앞에까지 장소가 있습니다. 장소만 출력하게 해주세요. 
print(code[a + 1 : b])
code = code[a + 1 : b]

c = code.replace('@','')
print(c)

print("mission 3 ==================")
# 장소들을 알파벳순서대로 공격을 한다.
# 이때, 첫번째 장소를 찾아라.



# 데이터타입
# 1. 숫자타입 Number
# 2. 문자열타입 String
# 3. ⭐리스트타입 List [] : 여러개의 데이터(요소)를 저장하는 데이터타입
# [요소(숫자, 문자, 리스트),요소,요소,요소]


# 반 친구들 리스트만들기
# - 짱구 등장인물 : 짱구, 철수, 유리, 훈이, 맹구
# - 순서(=인덱스, 0번부터 시작하는)

d = ['짱구', '철수', '유리', '훈이', '맹구']
# d변수에서 4번째 맹구를 뽑아서 출력해보자
print(d[4])

# 이 문자열을 리스트로 바꿔주고 싶다.
# - ','문자를 구분인자로 해서 문자을 나눠서 리스트로 만들어볼래
# => ⭐ 문자열변수.split("구분인자")
# "theater,police station,stock market,city hall,shopping mall,nuclear plant,university"
e = c.split(',')
print(e)
# 리스트를 정렬( 리스트.sort()  / sorted(리스트))
# - 오름차순(작은것부터 큰순서대로, 1~~, a~~)
# - reverse=True 넣으면 내림차순도 가능하다.(큰수~ 작은순서대로, 100~1, z~)

print(e.sort()) # 원본이 바뀐다.
print(e)

# None <= 값이 없어.


f = ['theater', 'police station', 'stock market', 'city hall', 'shopping mall', 'nuclear plant', 'university']
sorted(f)
# print(sorted(f, reverse=True))
print(sorted(f))
print(e[0])


# 다음시간 : 프로그램을 제어할수 있는 문법
# - 조건문
# - 반복문