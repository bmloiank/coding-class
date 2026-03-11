#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")

# https://prod.liveshare.vsengsaas.visualstudio.com/join?365A20CC040A561A0A4F49BF108215615A13

# a에서부터 e가는 경로를 찾는게 최종목표
# route : 딕셔너리
# - key: 지점 
# - value : 딕셔너리 => b,c,f,h로 갈수 있는지점
# 딕셔너리 추가,수정,삭제
# 추가 = , 수정 =
# 삭제 .pop("key")


# 점선: f-c, f-e,c-d,h-d,h-j
route = {
    'a':{'b':1772,'c':5805,'f':5546,'h':730},
    'b':{'a':1772,'d':3010,'g':2562},
    'c':{'a':5805,'d':4111,'e':1081,'f':1621},
    'd':{'b':2010,'c':4111,'e':2892,'g':2908,'h':3092,'j':517},
    'e':{'c':1081,'d':2892,'f':4082,'i':506,'j':290},
    'f':{'a':5546,'c':1621,'e':4082,'i':627},
    'g':{'b':2562,'d':2908,'h':903},
    'h':{'a':730,'d':3092,'g':903,'j':3900},
    'i':{'f':627,'e':506},
    'j':{'d':517,'h':3900,'e':290}
}
# route.pop('d')
# 딕셔너리변수이름[key], .get(key)
print(route.get('d'))
print(route)
route.get('c').pop('d')
route.get('c').pop('f')
route.get('d').pop('c')
route.get('d').pop('h')
route.get('e').pop('f')
route.get('f').pop('c')
route.get('f').pop('e')
route.get('h').pop('d')
route.get('h').pop('j')
route.get('j').pop('h')
print(route)
print("\nmission 2==============")
# 출발지부터 도착지까지 가는 경로들의 리스트
road = ['afie', 'ace', 'abde', 'abdje', 'abgde', 'abgdje', 'ahgde', 'ahgdje']
# (1) 각경로를 출력하기
# - afie' 끝 -> 'ace'
for i in range(len(road)):
    path = road[i]
    print(path,'----')
    time = 0
    # 예제) afie
    # a-f / f-i / i-e
    # 도로road = 지점수-1
    # (2) 각 도로별 소요시간을 알고싶다.
    for j in range(len(path)-1):
        print("도로: ",path[j], "-",path[j+1])
        start = path[j]
        end = path[j+1]
        print("소요시간: ",route.get(start).get(end))
        # 도로별로 소요시간을 더하고 싶어다.
        time += route.get(start).get(end)
        
    
