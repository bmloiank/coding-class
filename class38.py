#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")

# https://prod.liveshare.vsengsaas.visualstudio.com/join?6FC875321ABAAC28E2EE80C19049BF2E6D87


#data
# 그래프 그리는 모듈
import matplotlib.pyplot as plt
import networkx as nx
import wizLib

# 데이터를 그래프로 그려주는 클래스 - 수정 안할거니깐 무시
class GraphVisualization:
    def __init__(self):
        self.visual=[]

    def addEdge(self, a, b):
        temp=[a, b]
        self.visual.append(temp)

    def visualize(self):
        G=nx.Graph()

        for item in self.visual:
            a, b = item
            G.add_edge(a, b)
        pos=nx.shell_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
        wizLib.showPlt(plt)

G=GraphVisualization()


# 연락처
phonebook = {1:'Sem',2:'Milan',3:'Sophie',4:'Evi',5:'Lars',6:'Joep',7:'Daan',8:'Dex',9:'Esmee',10:'Vera'}
# 노드 10개
# 인접리스트 10*10 =>11*11(0행, 0열은 무시)

class Graph:
    def __init__(self):
        # (1) 인적리스트 => 2차
        self.graph = []
        for i in range(11):
            self.graph.append([])
            for j in range(11):
                self.graph[i].append(0)
            
        # 리스트 축약형
        # print([[1 for j in range(11)] for i in range(11)])
        
    # 엣지를 추가할 메서드
    def edge(self, n1, n2):
        self.graph[n1][n2] = 1
        self.graph[n2][n1] = 1
    
    def printGraph(self):
        for i in range(11):
            for j in range(11):
                print(self.graph[i][j], end=' ')
            print()
        G.visualize()
        
        
graph = Graph()
graph.edge(1,4)
graph.edge(10,5)
graph.edge(7,6)
graph.edge(6,1)
graph.edge(2,7)
graph.edge(3,6)
graph.edge(7,8)
graph.edge(7,9)
graph.edge(9,3)
graph.edge(5,7)
graph.edge(10,6)
graph.edge(7,4)
graph.edge(9,10)
graph.edge(9,1)

print(graph.graph)
graph.printGraph()
for i in range(len(graph.graph)):
    print(i,sum(graph.graph[i]))
    sum(graph.graph[i])
 
   
          
 
    #     G.addEdge(start, end)
 

