'''
< 데이터분석 > 
https://pandas.pydata.org/
pandas : 파이썬에서 데이터를 처리하기위한 라이브러리

테이블
데이터베이스 DB => excel 
- 테이블 형태로 저장되어 있습다.
<학생테이블>
--------------------------
|이름 | 반 | 번호| 핸드폰번호 |
--------------------------
박주하 | 10 | 13 | 01012345
홍길동 | 1 | 1   | 0101223456
신짱구 | 2 | 2 | 1023456


https://docs.google.com/spreadsheets/d/1kDbqRcxraANwIYaqgKadOYur8yn0WsTpJNRShlV6B28/edit?usp=sharing
'''

import pandas as pd

# (1) csv 읽어오기
# 변수 = pd.read_csv("파일경로")
# - 상대경로 : 현재 파일 기준을 파일을 탐색  
#   => ./(현재위치)  ../(부모위치)
#   => ./디렉토리명/파일이름.확장자
# - 절대경로 : 프로젝트 최상위경로(/)를 기준으로 파일을 탐색

# (2) Pandas 핵심 자료구조 DataFrame df : 엑셀의 테이블처럼 바라보는 데이터형식 2차원리스트 
sample_student = pd.read_csv('./data/sample_student.csv')
print(sample_student)

# (3) dataframe의 columns 찾기
print(sample_student.columns)

# (4) df에서 컬럼으로 데이터 뽑기
# - 한컬럽 뽑기 df['컬럼명']
# - 여러컬럼뽑기 df[['컬럼1','컬럼2']]
print(sample_student[['이름',"학년", '핸드폰번호']])


# (5) df의 values 찾기
print(sample_student.values)


# (6) 상위 5개 뽑기 head() / 하위 5개 뽑기 tail()
print(sample_student.head())
print(sample_student.tail())


# (7) df의 데이터구조 info()
print(sample_student.info())

# (8) df의 통계 describe()
print(sample_student.describe())


# (7) 해당 행번호를 선택해서 뽑기 loc[번호]
print(sample_student)
print(sample_student.loc[3])

print("-----")
# df객체 직접만들어보기
# pd.DataFrame({
#   "컬럼1명" : [해당컬럼에 들어갈 데이터],
#   "컬럼2명" : [해당컬럼에 들어갈 데이터],
# },index=[])
# 이름 나이 연봉(만)
player=pd.DataFrame({
    '이름' : ["누구야", '1루수', '2루수'],
    '나이' : [3,7,10],
    '연봉' : [100000, 60000, 3]
    }, index=[4, 7, 11])
print(player)

# loc => 인덱스 라벨로 찾기
# iloc => 기본 행순서(db의 인덱스)로 찾기
# print(player.iloc[2])
# print(player.loc[4])

## 1.  데이터프레임에 값을 추가하기 
# 데이터프레임이름.loc[새로운 행 인덱스] = {"컬럼명":~, "컬럼명":~ }
player.loc[27] = {'이름' : '몰라', '나이' : 15, '연봉' : 100}

print(player)

# pandas의 데이터객체
# - 데이터프레임 : 이차원리스트 [[],[],[],[],[],[],]
# - 시리즈 : 1차원리스트 => [] => 하나의 행데이터
# pd.Series(데이터)
a = pd.Series({'이름' : '몰라', '나이' : 15, '연봉' : 100})

#  pd.concat([데이터프레임이름,시리즈이름.to_frame().T],ignore_index=True)
print(a)
player1 = pd.concat([player, a.to_frame().T], ignore_index=True)
print(player)
print(player1)


# 삭제 drop(행인덱스 혹은 컬럼이름, axis=0(행에서찾을거다)/1(열기준))
player1 = player1.drop(3)
# player1 = player1.drop('나이', axis=1)
player1 = player1.drop(['나이','연봉'], axis=1)
print(player1)


# 데이터 수정 loc 2루수의 연봉을 30
# df.loc[행인덱스,'열이름'] = 새로운값
# df.iloc[테이블순서상의 행인덱스,열인덱스]
print(player)
player.loc[11, '연봉'] = 300
print(player)
player.iloc[0, 2] = 1000000
print(player)

print("----------- 필터링 -----------------")
# 이름이 누구야를 빼고 연봉을 50 빼기
# (1) 이름이 누구야인것을 찾아라
# df.loc[df['컬럼이름'] == 찾는값]
print(player.loc[player['이름'] == '누구야'])
# (2) 이름이 누구야 아닌것을 찾아라
print(player.loc[player['이름'] != '누구야'])
# (3) 이름이 누구야가 아닌것들 중에서 '연봉' 컬럼만 출력하기
# df.loc[행필터, 열필터]
print(player.loc[player['이름'] != '누구야', ['연봉','이름']])
# (4) 이름이 누구야가 아닌것들 중에서 '연봉' 컬럼aks 50을 동시에 빼기
# => 찾은 데이터들을 모두 변경이 됩니다.
# df.loc[행필터, 열필터] = 변경할 데이터
player.loc[player['이름'] != '누구야', '연봉'] -= 50
print(player)


#-sql(데이터베이스)--------------------------------------
# 컬럼 추가하기
# df['컬럼명']
# <null : 값이 없음>
# - null
# - 숫자에서 없음 NaN(숫자가 아님 Not a number)
# - 파이썬 none

player['몸무게'] = None  # <- dtype object가 들어가는 컬럼
player.loc[4,'키'] = 1  # <- 숫자가 들어가겠금, float
player.loc[4,'몸무게'] = 2

print(player.isnull().sum())
print(player)

# # 빈값 채우기 fillna("값")
# print(player.fillna(0))













