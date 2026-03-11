# 팰린드롬 https://www.acmicpc.net/problem/10174
# 수박이박수 글자가 5개면 -> 체크는 2번
# 0     4
#  1  3
#    
n = int(input())

for i in range(n):
    case = input().lower()
    # 여기안에다가
    # print(case)
    answer = 'Yes'
    for j in range(len(case)//2):
        if case[j] != case[len(case)-j-1]:
            answer = 'No'
    print(answer)   
        # print(len(case)-j-1)
        










# 과제)
# 더하기 사이클 https://www.acmicpc.net/problem/1110
# 블랙잭 https://www.acmicpc.net/problem/2798
# 벌집 https://www.acmicpc.net/problem/2292



