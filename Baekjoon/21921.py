# 블로그 https://www.acmicpc.net/problem/21921
'''
찬솔이는 
$X$일 동안 가장 많이 들어온 방문자 수와 그 기간들을 알고 싶다.

찬솔이를 대신해서 
$X$일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해주자.

입력)
첫째 줄에 블로그를 시작하고 지난 일수 $N$와 $X$가 공백으로 구분되어 주어진다.
둘째 줄에는 블로그 시작 $1$일차부터 $N$일차까지 하루 방문자 수가 공백으로 구분되어 주어진다.

출력
첫째 줄에 
$X$일 동안 가장 많이 들어온 방문자 수를 출력한다. 만약 최대 방문자 수가 0명이라면 SAD를 출력한다.

만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력한다.
'''

n, x = list(map(int, input().split()))
human = list(map(int, input().split()))

# (1) 윈도우 : X칸짜리
# - human있는 숫자를 앞에서부터 x칸씩 넣어
# (2) 윈도우 탐색
window = human[:x]
# print(window)
max_n = sum(window)
last_n = sum(window)
same = 1
# [1, 4] => 5
# [4, 2] => 합 5-1+2
# [2, 5]
# [5, 1]
for i in range(x,n):
    last = window.pop(0)
    window.append(human[i])
    last_n = last_n - last + human[i]
    if last_n > max_n:
        max_n = last_n
        same = 1
    elif last_n == max_n:
        # print('같다!!')
        same += 1
if max_n == 0:
    print('SAD')
else:
    print(max_n)
    print(same)





# 과제)
# 인간-컴퓨터 상호작용 https://www.acmicpc.net/problem/16139
# 선택1)좋은친구 https://www.acmicpc.net/problem/3078
# 선택2)DNA https://www.acmicpc.net/problem/12891

