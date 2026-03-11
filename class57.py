#파일명 : data/test2.csv

import pandas as pd
import matplotlib.pyplot as plt
pile = pd.read_csv('./data/test2.csv')
print(pile)

# 범죄율 = 범죄/인구수
# (1) 범죄값 뽑아보기
print(pile['범죄'])
print(pile['인구'])
print(pile['범죄'] / pile['인구'])

pile["범죄율"] = pile['범죄'] / pile['인구']
print(pile)


# 정렬 df.sort_values("컬럼명", asceding=False)  asceding=False 내림차순
pile = pile.sort_values('범죄율', ascending=False)
# 정렬된 얘의 맨위의 구역을 출력하기
print(pile)
print(pile.loc[0, '구역'])




#-----------------------------
data = pd.read_csv('./data/crime.csv')
print(data)

# 그래프
# x축 년도 y축 숫자
# y5개 그래프 범죄유형
x = data['연도']
print(data['연도'])
y1 = data['강도']
y2 = data['절도']
y3 = data['사기']
y4 = data['테러']
y5 = data['폭행']
print(y1, y2, y3, y4, y5)


# 선그래프 plot
plt.plot(x, y1, label='Robbery')
plt.plot(x, y2, label='Burglary')
plt.plot(x, y3, label='Fraud')
plt.plot(x, y4, label='Terror')
plt.plot(x, y5, label='Assault')

plt.legend()
plt.grid(True)
plt.show()