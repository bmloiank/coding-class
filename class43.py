'''
다익스트라 알고리즘(Dijkstra algorithm)


'''



#data
import heapq
from collections import defaultdict
# import matplotlib.pyplot as plt
# import networkx as nx
# import wizLib
 
#data
myGraph=defaultdict(dict)
 
class GraphControl:
    def __init__(self):
        self.visual=[]
 
    def addEdges(self, start, end, dist):
        myGraph[start].update({end: dist})
        myGraph[end].update({start: dist})
        temp=[start, end, dist]
        self.visual.append(temp)
 
    def visualize(self):
        G=nx.Graph()
        for item in self.visual:
            u, v, weight = item
            G.add_edge(u, v, weight=weight)
        pos={
            'A': (1, 3),
            'B': (2, 2),
            'C': (3, 1),
            'D': (2, 5),
            'E': (3, 4),
            'F': (4, 3),
            'G': (3, 7),
            'H': (4, 6),
            'I': (5, 5),
            'J': (4.5, 7)
        }
        eLa=nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=eLa, font_size=10)
        wizLib.showPlt(plt)
 
G=GraphControl()
G.addEdges('A', 'D', 3)
G.addEdges('B', 'E', 2)
G.addEdges('C', 'F', 4)
G.addEdges('D', 'E', 4)
G.addEdges('E', 'F', 5)
G.addEdges('D', 'G', 1)
G.addEdges('G', 'E', 1)
G.addEdges('E', 'H', 2)
G.addEdges('G', 'H', 3)
G.addEdges('H', 'F', 4)
G.addEdges('F', 'I', 2)
G.addEdges('H', 'I', 1)
G.addEdges('G', 'J', 4)
G.addEdges('H', 'J', 5)
G.addEdges('I', 'J', 3)
# G.visualize()
print(myGraph)
# {'A': {'D': 3}, 
# 'D': {'A': 3, 'E': 4, 'G': 1}, 
# 'B': {'E': 2}, 
# 'E': {'B': 2, 'D': 4, 'F': 5, 'G': 1, 'H': 2}, 
# 'C': {'F': 4}, 
# 'F': {'C': 4, 'E': 5, 'H': 4, 'I': 2}, 
# 'G': {'D': 1, 'E': 1, 'H': 3, 'J': 4}, 
# 'H': {'E': 2, 'G': 3, 'F': 4, 'I': 1, 'J': 5}, 
# 'I': {'F': 2, 'H': 1, 'J': 3}, 
# 'J': {'G': 4, 'H': 5, 'I': 3}
# }

print()
# 다익스트라 알고리즘(Dijkstra algorithm)
# A,B,C 각각 구해보기 => 함수
# - myGraph, 시작, 도착
# - 탐색예정은 heapq
# - 코스트리스트 : 노드의 갯수만큼 float("inf")
# - 노드이름또한 리스트로 저장해놔야야 인덱스 체크 가능

def da(myGraph, start, end):
    queue = []                  # 탐색예정 큐 -> heapq
    cost_list = []              # 코스트관리 리스트
    visited = []                # 방문예정 
    # path = []                   # 최적경로: path

    # 코스트를 무한대로 초기화 & 문자열''로 초기화
    for i in range(len(myGraph)):
        cost_list.append(float("inf"))
        # path.append('')
    node_name = list(myGraph.keys())
    


    # (1) 시작노드는 코스트가 0번으로  탐색예정에 추가
    # - 노드 인덱스번호를 찾아야한다.  리스트.index('찾는데이터')
    cost_list[node_name.index(start)] = 0
    #print(node_name, "\n", cost_list, '\n', sep="")
    # path[node_name.index(start)] += start

    # 탐색예정에 추가하기 => heap
    # 1. 코스트, 2. 노드이름 3. 둘다=> (코스트,노드이름)
    # 
    heapq.heappush(queue, (cost_list[node_name.index(start)], start))

    #print(queue)
    # (2) 탐색시작
    # - (2-1) 탐색 빼기-> 우선순위가 작은것부터 빼기
    # - (2-2) 방문을 하지않아다면 방문완료 추가하기
    # - (2-3) 방문을 하지않았다면, 그래프에서 노드랑 연결되 노드들 찾기
    # - (2-4) 연결된 노드의 코스트와 노드에서 출발하느 코스트 중에서 더 작은값을 코스트에 저장하기
    # - (2-5) 연결되 노드가 방문하지않았따면 탐색예정에 추가해주기
    while len(queue):
        cost, node = heapq.heappop(queue)
        #print("----뽑힌 노드",node,"------")
        if node not in visited:
            visited.append(node)
            for k,v in myGraph[node].items():
                # k - 연결된 노드
                # v - 뽑은 노드에서의엣지 코스트  e-f-d-a-b : a의 코스트리스트랑 + 엣지의 가중치를 더하기 
                
                #print(k,v)
                
                c1 = cost_list[node_name.index(k)] # k의 자체코스트 : 코스트리스트
                c2 = v + cost
                # c1과 c2 중에서 작은거 교체 cost_list[node_name.index(k)] 를 교체
                if c1 > c2:
                    # K 코스트
                    cost_list[node_name.index(k)] = c2
                    ##### k가 node를 거쳐가겠다 (안바뀌면 기존 경로를 유지하겠다.)
                    ##### k 경로 = a의 경로+'본인노드'

                # 탐색 예정에 추가하기 cost_list[node_name.index(k)]
                heapq.heappush(queue, (cost_list[node_name.index(k)], k))  


            
            #print(cost_list)
        

    # & 경로 node이름을 추가하기고,
    # 
    # D 3
    # [0, 3, inf, inf, inf, inf, inf, inf, inf, inf]


    # 도착지점에서의 최단코스트를 알고싶은거
    return cost_list[node_name.index(end)]

# 출발지점 A,B,C
print(da(myGraph, 'A', 'J'))
print(da(myGraph, 'B', 'J'))
print(da(myGraph, 'C', 'J'))