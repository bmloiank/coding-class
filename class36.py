# datetime 모듈 날짜와 시간을 다루는 모듈
# 수강신청할때 네이비즘

# <일반적인 모듈사용>
# import 모듈명
# <모듈에서 특정객체/함수만 사용가능>
# from 모듈명 import 객체/함수

from datetime import datetime, timedelta

# (1)오늘의 날짜를 가져오기 => datetime객체
# datetime.now()
today = datetime.now()
print(today)

# (2)기본적인 날짜형식(format): YYYY-mm-dd HH:MM:SS.ms
# =>.strftime("포멧패턴") 날짜포멧을 변경해서 문자열로 변환
# %Y: 년도 %m:월 %d:일 %H:시간 %M:분 %S:초 %p:am/pm %Z %A 요일
# 2025년 7월 7일
print(today.strftime('%Y년 %m월 %d일 %H시 %M분 %S초 %Z'))



# (3) 특정날짜를 지정할 수가 있습니다.
# datetime(년도,월,일,시간,분,초)
seven = datetime(7777, 7, 7)
print(seven)


# (4) 날짜 차이를 계산 => 디데이
# 특정날짜에서 오늘날짜를 빼기
print(seven - today)


# 특정날짜가 미래
# - 하루전 d-1
# - 당일 d-day
# 특정날짜가 과거
# - 하루다음 d+1


# (5) 오늘날짜에서 열흘뒤의 날짜
# 날짜의 연산 => timedelta 객체(days, hours, minutes seconds weeks)
# 날짜객체 + timedelta(days=추가할일)
print(today + timedelta(days = 10))


# (과제) 윤년 https://www.acmicpc.net/problem/2753



# (6)특정일자의 요일계산하기
# 날짜객체.weekday() 0: 월요일 ~ 6: 일요일
# 리스트
date = ['월', '화', '수', '목', '금', '토', '일']
print(date[seven.weekday()])
