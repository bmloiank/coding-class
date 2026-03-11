# 최대 최소 https://www.acmicpc.net/problem/10818

n = input()
number = list(map(int, input().split(' ')))

print(number)

'''
최대최소 구하기
(1) 최대값구하는 함수 max(리스트)
    최소값구하는 함수 min(리스트)

    # print(max(number), min(number))

(2) 정렬해서 구하기 => 리스트.sort() sorted(리스트)
    최대값은 -1번째
    최소값은 0번째

    number.sort(reverse=True)
    print(number)

(3) 최대값최소값구하는 알고리즘
'''

# 최대값을 저장할 변수 
# - 내부에 잇는 아무값으로 초기설정해주기(보통은 0번째값으로 셋팅)
maxn = number[0]
for i in range(len(number)):
    if maxn < number[i]:
        maxn = number[i]
print(maxn)

minn = number[0]
for i in range(len(number)):
    if minn > number[i]:
        minn = number[i]
print(minn)