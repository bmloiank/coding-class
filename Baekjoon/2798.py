# 블랙잭 https://www.acmicpc.net/problem/2798

n, m = map(int, input().split(' '))
deck = list(map(int, input().split(' ')))
# deck_sort = sorted(deck)
# print(n,m,deck)

# m보다 크지않는 최대값
# 모든 경우를 구해야해.(3장) => 반복으로

# 5 6 7 8 9
# 3개 고르기 (0~3번앞) 
# 첫번째 숫자 5~7
# 두번째 숫자 6~8 (첫번째숫자의 다음숫자부터)
# 세번째 숫자 7~9 (두번째숫자의 다음숫자부터)
#(1)
# 56 (7~9)
# 5 7(8~9)
# 5 8 9

# 67(8~9)
# 689


# print(range(n),"0~n-1연속된 정수를 뽑아주는 함수")
# print(range(start,end,step),"start~end, step간격으로 연속된 정수를 뽑아주는 함수")

# range(끝)
answer = 0
for i in range(n-2):
    # print("첫번째수",deck[i])
    # 첫번째수 다음번호부터 끝에서 1개전까지 반복하기
    # range(시작,끝,간격(선택))
    for j in range(i+1,n-1):
        # print("-두번째수",deck[j])
        # 두번째 수 다음부터 끝까지 반복해서 뽑기
        for k in range(j+1,n):
            # print("--세번째수",deck[k])
            # print(deck[i],deck[j],deck[k])
            add = deck[i]+deck[j]+deck[k]
            if add <= m and add > answer:
                answer = add
print(answer)                


# TODO: 


# <최댓값알고리즘>
# lst = [1,5,7,1,2,9]
# 최대값 = 내부값중에서 하나 혹은 0(자연수라는 가정하에)
# 다 꺼내서 비교해서
# 최대값보다 크면 최대값을 교체








