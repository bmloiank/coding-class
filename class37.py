# 50230번 트럭 출발 시간을 계산하기

cargo_list=[]

import random
random.seed(20201216)
from datetime import datetime, timedelta
# collections 모듈에 deque객체를 가져오기
from collections import deque

# 첫 트럭이 출발시간 50년 2월 27일 10:00
departure_time=datetime(2050, 2, 27, 10, 00)


# cargo(화물)개
class Cargo:
    def __init__(self):
        # number속성 : 화물번호
        self.number=random.randint(10000, 99999)
        # truck_number속성 : 화물이 싣게될 트럭번호
        self.truck_number=random.randint(0, 9)
        # 화물의 출발시간 : => 수정 해야한다.
        self.departure_time=datetime(2050,2,27,10,00)

while len(cargo_list)!=100:
    cargo=Cargo()
    if cargo not in cargo_list:
        cargo_list.append(cargo)



# 객체 = Object 
# 화물리스트: Cargo 객체
# print(cargo_list)
# for i in range(len(cargo_list)):
#     print(cargo_list[i].number)

# 트럭이 몇바퀴 돌았는지를 리스트 => 10개
round_num_list=[0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0]
# 한바퀴 도는 데 몇분이 걸리는지 리스트 => 10개
time_per_round_list=[40, 50, 60, 30, 20, 25, 10, 5, 55, 25]
# 트럭은 총 10대 - 3개를 받을 수 있도록 이차원리스트 만들기
track = [[], [], [], [], [], [], [], [], [], []]
# print(len(track))


'''
화물 트럭 옮기기 시뮬레이터
(1) 모든 화물이 다 나갈때까지 계속해서 화물을 뽑기
(2) 뽑은 화물의 트럭번호를 찾고
(3) 트럽번호에 맞춰서 맞춰서 트럭에 추가해주기
(4) 내트럭이 3개가 되면 => 출발!
   - 트럭안 내용이 없어지기
   - 한바퀴가 추가

'''


# queue 구조 -> cargolist로 큐 만들기
# 변수이름 =deque(리스트)
queue = deque(cargo_list)
# 모든 화물이 다 나갈때까지 계속해서 화물을 뽑기
# true :1 "a" "123456" ["a","b"]
while queue:
    pop = queue.popleft()
    # print(pop)
    truck_num = pop.truck_number
    # print(truck_num)
    # print(track[truck_num])
    track[truck_num].append(pop)
    
    if len(track[truck_num]) == 3:
        time = round_num_list[truck_num]*time_per_round_list[truck_num]
        # 출발시간 10:00 time_per_round_list round_num_list
        # 날짜객체 + 흐른 시간을 더해주고싶어요! => timedelta(minutes="더할시간")
        # 각 화물별 departure_time 수정하기
        # print(truck_num, round_num_list,"-------")
        for i in range(3):
            c1 = track[truck_num].pop()
            c1.departure_time = c1.departure_time + timedelta(minutes = time)
            # print(c1.number,c1.departure_time)
            if c1.number == 50230:
                print(c1.number,c1.departure_time)
        round_num_list[truck_num] += 1

        
        