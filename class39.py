#data
import random
random.seed(104)
 
class Graph:
    def __init__(self):
        # 딕셔너리 key=리스트의 인덱스
        self.graph = {}

        # 노드들의 리스트
        self.node_list = []
    # 노드 추가 - 노드를 추가하면 연결상태를 저장할 공간이 필요
    def addVertex(self, V):
        self.graph[V] = []
 
    def delVertex(self, V):
        if V in self.graph.keys():
            del self.graph[V]
 
    def addEdge(self, startV, endV):
        if endV not in self.graph[startV]:
            if startV != endV:
                self.graph[startV].append(endV)
                self.graph[endV].append(startV)
 
    def printNode(self):
        nodeList = self.graph.keys()
        num = 1
        for node in nodeList:
            print("Node[%d] : %s" % (num, node))
            num += 1
 
    def printGraph(self):
        for key in self.graph.keys():
            adj_list = self.graph[key]
            print(key, end=' : ')
            for i in range(len(adj_list)):
                print(adj_list[i], end=' ')
            print()
 
map_graph = Graph() # 그래프 인스턴스
# 대학생 동창명단
name_list = ['Melissa','Chen','Lewis','Lisa','Jeffrey','Miguel','Oscar','Angella','Leslie','Erik','Dana','Kristen','Roy','James','Allison','Robin','Margaret','Cynthia','Leonard','Natatsha','Oliver','Hudson','Ava','Jack','Rbecca','Graham','Jordan','Davis','Josha','Lance','Cindy','Laura']
for name in name_list:
  map_graph.node_list.append(name)
  map_graph.addVertex(name)
 

 
for i in range(len(map_graph.node_list)):
    map_graph.addEdge(map_graph.node_list[random.randint(0,  len(map_graph.node_list)-1)], map_graph.node_list[random.randint(0, len(map_graph.node_list)-1)])
map_graph.delVertex('Angella')


# map_graph.printGraph()
print(map_graph.node_list)
# ['Melissa', 'Chen', 'Lewis', 'Lisa', 'Jeffrey', 'Miguel', 'Oscar', 'Angella', 'Leslie', 'Erik', 'Dana', 'Kristen', 'Roy', 'James', 'Allison', 'Robin', 'Margaret', 'Cynthia', 'Leonard', 'Natatsha', 'Oliver', 'Hudson', 'Ava', 'Jack', 'Rbecca', 'Graham', 'Jordan', 'Davis', 'Josha', 'Lance', 'Cindy', 'Laura']
print(map_graph.graph)


# 엣지로 안젤라라 연결된 노드들을 알고싶다.

# {'Melissa': ['Hudson', 'Jeffrey'], 
# 'Chen': ['Roy', 'Leslie'], 
# 'Lewis': ['Jordan', 'Kristen', 'Oscar', 'Rbecca'], 
# 'Lisa': ['Jack', 'Erik'], 
# 'Jeffrey': ['Hudson', 'Melissa'], 
# 'Miguel': ['Josha'], 
# 'Oscar': ['Dana', 'Lewis'], 
# 'Leslie': ['Chen', 'Allison', 'Robin'], 
# 'Erik': ['Angella', 'Kristen', 'Lance', 'Lisa'], 
# 'Dana': ['Oscar', 'Natatsha', 'Angella', 'James'], 
# 'Kristen': ['Lewis', 'Erik'], 
# 'Roy': ['Chen', 'Margaret', 'Ava'], 
# 'James': ['Dana'], 
# 'Allison': ['Graham', 'Leslie'], 
# 'Robin': ['Margaret', 'Leslie'], 
# 'Margaret': ['Roy', 'Robin', 'Jordan'], 
# 'Cynthia': [], 
# 'Leonard': [], 
# 'Natatsha': ['Dana'], 
# 'Oliver': ['Graham'], 
# 'Hudson': ['Melissa', 'Jeffrey'], 
# 'Ava': ['Roy'], 
# 'Jack': ['Lisa'], 
# 'Rbecca': ['Lewis'], 
# 'Graham': ['Allison', 'Oliver'], 
# 'Jordan': ['Lewis', 'Margaret'], 'Davis': [], 'Josha': ['Lance', 'Miguel'], 'Lance': ['Josha', 'Cindy', 'Erik'], 'Cindy': ['Lance'], 'Laura': []}

print("\n\n\n\n안젤라와 연결된 친구들 목록을 가져오기 Angella")
# 딕셔너리
# {"key":"value"}
# print(map_graph.graph.values())

# 딕셔너리의 반복문
# key값으로만 접근 딕셔너리.keys()
# value값으로 values()
# key-value쌍으로 튜플로 접근 딕셔너리.items()
# for k, v in 딕셔너리.items():

# 변수의 다중할당 : 갯수만 같으면 된다.
# a, b = ["alpha1", "alpha2","alpha3", "alpha4"]
# 0번째는 a
# 1번째는 b


# a=변수[0]
# b=변수[1]

print(map_graph.graph.items())
# if map_graph.graph.items in 'Angella' (key,value)
# for i in range(숫자) 0~숫자-1
friends = []
for k, v in map_graph.graph.items():
    # print(k, v)
    if 'Angella' in v:
        friends.append(k)
print(friends)


