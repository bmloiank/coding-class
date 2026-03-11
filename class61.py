'''
Dynamic Programming 다이나믹 프로그래밍(=동적계획법)
: 문제 크게보고 작은 문제로 쪼개서 푸는 방법

누적합
- 공통적으로 같이 사용하는 자원
- 공통으로 주어지는 자원을 먼저 정리(누적합) => 필요한큼 계산하기


점화식 문제 : 피보나치수열(고2 1학기)
# 1 2 3 5 8 13 21 34 ...


'''


'''
슬라이딩 윈도우 
: 특정구간의 합계나 평균을 구할때 보통 사용하기

'''
# 12일 동안의 하루 평균 물건 판매량
# = 5일 평균 판매량 (구간간격 5)
num_list = [5,3,2,5,7,1,4,8,4,3,8,2]
'''
            5,3,2,5,7
        (앞지우고)3,2,5,7,1(뒤에 추가)
'''






# 이진탐색 / 이분탐색 Binary Search
# 72 번이 있는지 
# (1) 정렬한다음
# (2) 중앙값 : len()//2     50 
# 0 1 2 3 4 5 6 7 ..... 98 99 100
# start          mid=50              end

# #  51~100사이에서 탐색
# # start -> mid => 새로운 mid 75
# # 찾는값이 왼쪽에 있으면 end-> mid  50~75

# 49 50

# 이분 탐색 함수 binary_search(리스트, 찾는값)
# (1) 리스트를 정렬
# (2) start, end 초기화
# (3) 반복하면서 체크할건데 start end 자리가 바뀌면 탐색 종료
# (3-1) 중앙 = 평균 

# 0 100 50
# 50 100 25 75 

# 72
# 0 1 2 3 4 5 6 7 ..... 98 99 100
# start          mid=50              end
# 만약에 50보다 찾는값이 크면 start = 50(조건문에서 검증한 숫자가 포함이 된다.)
# 50 -100
# mid =75
# 50- 75  mid 62 start 62
# 62-75   mid 68 start 68
# 68-75   mid 143 start 71
# 71-75   mid 73 end 73
# 71-73   mid 72 end 72
# 71-72   mid 71 start 71


def binary_search(lst, f):
    lst.sort()
    start = 0
    end = len(lst)
    while start < end:
        mid = (end + start)//2
        if f > lst[mid]:
            start = mid+1
        else:
            end = mid
        print("start",start,"end",end)
binary_search(list(range(0,100)),72)