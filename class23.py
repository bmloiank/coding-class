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

# 각 지점별 연결지점과 걸리는 시간
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
road = ['afie', 'ace', 'abde', 'abdje', 'abgde', 'abgdje', 'ahgde', 'ahgdje']
time_list = []
for i in range(len(road)):
    # 하나의 경로
    print(road[i],"------------------")
    # 하나의 경로에 대해서 소요시간을 구하고 => 반복돌려서 모든 road에 대해서 진행할 예정
    road_one = road[i]
    # (1) 경로 도로의 갯수를 출력해주세요.
    # (2) 연결되어있는 도로를 모두 출력하기
    # a-f :도로의 출발(현재값) - 도로의 도착(다음값)
    # f-i
    # i-e 
    print(len(road_one)-1)
    time = 0
    for j in range(len(road_one)-1):
        # 반복할때마다 
        print("출발지점:",road_one[j],"도착지점",road_one[j+1])
        # 출발지점부터 도착지점까지의 걸리는 소요시간을 route에서 찾아 출력하기
        print(route.get(road_one[j]).get(road_one[j+1]))
        time = time + route.get(road_one[j]).get(road_one[j+1])
    #시간을 하나의 리스트로 모아주기
    # 경로별 최종 소요시간
    print(time)
    time_list.append(time)


print("\nmission 3==============")
print(time_list)
# 반복문을 뽑아줘야 비교가 가능합니다.

# 누적합계변수 num = 0
# 최소값 변수 : 서로들 중에서 가장 작은값
# 최소값 변구 맨처음에는 리스트의 아무값을 넣는다.
min_num = time_list[0] # 0번째값을 넣준다.
for i in range(len(time_list)):
    # min_num이랑 비교해서 만약에 
    if min_num > time_list[i]:
        min_num = time_list[i]
    print(time_list[i],"=>" ,min_num)

print("\n 최대값 구하는 방법")
# 최대값 구하는 방법
max_num = time_list[0] # 0번째값을 넣준다.
for i in range(len(time_list)):
    # min_num이랑 비교해서 만약에 
    if max_num < time_list[i]:
        max_num = time_list[i]
    print(time_list[i],"=>" ,max_num)


# <리스트 안에 요소가 num일때만 가능하다>
# => sum(리스트)
# => min(리스트), max(리스트)
[[160.5,"이름a"],[160.5,"이름b"]]


# <야매 최소값>
# - 리스트.sort():원본, sorted(리스트):새로운 정렬리스트 정렬을 시킵니다.  => 데이터가 많아지면 성능이 떨어진다.
# - 맨앞의 값을 가져오면 됩니다.
print(sorted(time_list))
print(sorted(time_list)[0], sorted(time_list)[-1])