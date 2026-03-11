#data
from collections import deque
import random
import datetime as dt
random.seed(20)

# 3730번 차량이 지나간 고속도로이름을 찾기
# IC 
class Interchange:
    def __init__(self, name):
        # 고속도로이름
        self.name=name
        # 지나간 차량 번호
        self.pass_list=[]
        
        for i in range(30):
            passtime=dt.datetime(year=2050, month=3, day=13, hour=random.randint(10, 18), minute=random.randint(0, 59))
            self.pass_list.append((random.randint(1000, 9999), passtime))
            if (self.name=='West Daventown' or self.name=='Katherineton Lake' or self.name=='Seanchester Ville') and i==15:
                self.pass_list.append((3730, passtime))
 
    def __str__(self):
        return '{}'.format(self.name)
 
#cityInterChange => IC 리스트와 현재 그래프 연결 상태를 담고 있는 클래스
# cityInterChange 데이터 : 인접리스트로 구현된 그래프
class CityInterChange:
    def __init__(self):
        self.graph={}
        # node_list => node ic를 의미한다.
        self.ic_list=[]
 
    def addVertex(self, V):
        self.graph[V]=[]
 
    def addEdge(self, startV, endV):
        if endV not in self.graph[startV]:
            if startV != endV:
                self.graph[startV].append(endV)
                self.graph[endV].append(startV)
 
    def printIC(self):
        for i in self.ic_list:
            print(i)
 
    def printConnection(self):
        for key in self.graph:
            print(key, ' :', end=' ')
            adj_list=self.graph[key]
            for i in range(len(adj_list)):
                print(adj_list[i], end=' ')
            print()
 
#데이터 초기화
ICs=CityInterChange()
# ic리스트
namelist = ['South Sarahton', 'West Daventown', 'New Romerochester', 'Johnstadburhg', 'East Roberstad', 'Portborough', 'South Gregory', 'Davisborough', 'Katherineton Lake', 'Seanchester Ville', 'Jerry Haven', 'Dorothytonbury', 'Port Reyesview', 'North Michaelbury', 'New Claireland', 'East Nicholsland']
 
for i in range(len(namelist)):
    newIC=Interchange(namelist[i])
    ICs.ic_list.append(newIC)
    ICs.addVertex(newIC)
 
for i in range(len(namelist)*3):
    ICs.addEdge(ICs.ic_list[random.randint(0, len(namelist)-1)], ICs.ic_list[random.randint(0, len(namelist)-1)])
# ICs.printConnection()

def sortByValue(dic) :
    sorted_values = sorted(dic.values()) # Sort the values
    sorted_dict = {}
    for i in sorted_values:
        for k in dic.keys():
            if dic[k] == i:
                sorted_dict[k] = dic[k]
                break
    return sorted_dict

# 인접행렬 {"노드이름":[연결된노드 리스트]}
# print(ICs.graph)

# bfs 탐색 => 차량번호
# - 필요한데이터 : 그래프, 시작노드, 찾는차량번호
# - (1) 탐색예정을 저장할 큐 리스트 => deque()
# - (2)
# - (3) 시작노드를 큐에 추가하기
# - (4) 모든 탐색을 다 완료할때까지 진행하기
#    - (4-1) 탐색예정인 노드를 하나 뽑기
#    - (4-2) 방문아직 안한상태이면 노드를 넣어주기
#    - (4-3) graph 연결된 노드를 찾아서
#


def bfs(graph, start, carnum):
    # [문자열]
    queue = deque()
    visited = []
    queue.append(start)

    while queue:
        pop_node = queue.popleft()
        if pop_node not in visited:
            visited.append(pop_node)
            # print(pop_node)
            # 딕셔너리의 반복
            # for k in graph:
            #     v= graph[k]
            #     print(k,v)

            # for k, v in graph.items():
                # print("인스턴스",k, type(k))
            # if pop_node == graph.keys:
            queue.extend(graph[pop_node])

            #-------------미션------------
            # 탐색한 고속도로에서 3730이 지나갔냐?
            # 차량번호 지난시간
            # (7538, datetime.datetime(2050, 3, 13, 16, 22))
            # print(pop_node.pass_list)
            pass_car = pop_node.pass_list
            for i in range(len(pass_car)):
                if 3730 == pass_car[i][0]:
                    # 고속도로이름, 시간
                    print(pop_node.name, pass_car[i][1])


    

                    

# West Daventown 2050-03-13 12:41:00
# Katherineton Lake 2050-03-13 13:05:00
# Seanchester Ville 2050-03-13 17:03:00
print(bfs(ICs.graph, ICs.ic_list[0], 3730))  
namelist[0] # 문자열




# #######
# 리스트.appned("추가할데이터1개") # 리스트 적으면 통으로 들어가기

# 리스트.extend([추가할리스트])

# lst = ['a']
# # lst.append(['b','c','d'])
# print(lst, len(lst))
# lst.extend(['b','c','d'])
# print(lst, len(lst))
