# 백준 https://www.acmicpc.net/problem/15649
'''

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열


출력)
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.

'''




'''
4 3
# => 1~4까지의 숫자중에서 2쌍의 순서쌍 모든 경우를 출력하시오.
1 2 3
  3 4
  4 5
2 1
  3
  4
3 1
  2
  4
'''
# num = []
# for i in range(n):
#     num.append(i+1)
# for  i in range(n):
#     for j in range(n):
#         if (i+1) != (j+1):
#             answer.append((i+1, j+1))
# print(answer)    


# dfs => stack, 재귀함수
# m사이즈의 순서쌍이 필요하다. 순서쌍을 찾기 찾기위해서 탐색
n,m = list(map(int, input().split()))
answer = []

# 5 4 3 2 1 
def bts():
    # m개의 순서쌍이 완성되면 출력하고 탈출
    if len(answer) == m:
        # "구분인자".join()
        print(' '.join(list(map(str, answer))))
        return
    
    # 1~n까지의 자연수부터
    for i in range(n):
        if (i+1) not in answer:
            answer.append(i+1)
            bts()
            # 뒤에서 하나 빼기
            answer.pop()
    # return

bts()