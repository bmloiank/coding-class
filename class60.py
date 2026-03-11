'''
인공지능(AI) : 인각의 학습을 모방해서 행위를 할수있도록 하는 기술
- 데이터를 전달받아
- 학습
- 새로운 발견

인공지능 > 머신러닝 > 딥러닝
# 1) 지도학습
# 2) 비지도학습
# 3) 강화학습
 


'''

# 인공지능과 연령에 따른 상관관계가 있느냐 없느냐
# 1212.csv
# import matplotlib.pyplot as plt
# import n
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


monti = pd.read_csv('data/1212.csv')
print(monti)
# (1) age 데이터프레임(표-딕셔너리)에서 '나이' 컬럼 가져오기
# => 배열(리스트)로 변경하기 np.array(데이터프레임)
# (2) '의존도'컬럼 가져오기

print(monti['나이'])
age = np.array(monti['나이'])
john = np.array(monti['의존도'])

# scatter 그래프
# plt.scatter(x,y)



# 오차함수 CostFunction => 중3 분산 : 편차(a*x+b-y)의 제곱의 합
def CostFunction(x,y,a,b):
    cost = 0
    for i in range(len(x)):
        cost += (a*x[i]+b-y[i])**2
    return cost/len(x)/2


#파일명 : 1212.csv
# 경사하강법
def Grad_a(x,y,a,b):
    return sum((a*x+b-y)*x)/len(y)

def Grad_b(x,y,a,b):
    return sum(a*x+b-y)/len(y)



def Train(x,y,Iteration,LearningRate):
    a,b=0,0
    for _ in range(Iteration):
        g_a=Grad_a(x,y,a,b)
        g_b=Grad_b(x,y,a,b)
        a-=LearningRate*g_a
        b-=LearningRate*g_b
    return [a,b]


a,b=Train(age,john,10000,0.000001)
# plot()
plt.scatter(age, john)
plt.plot([min(age),max(age)],np.array([min(age),max(age)])*a*b)
print(CostFunction(age, john, a, b))


plt.show()


# https://colab.google/
# 