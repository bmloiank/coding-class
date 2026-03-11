'''
더하기 사이클 https://www.acmicpc.net/problem/1110

0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

'''


n = int(input())
start = n
answer = 0      # 사이클 수

while True:
    if n != start or answer == 0:
        # print(n)
        n = n%10*10 + (n//10 + n%10)%10
        answer += 1
    else:
        break
print(answer)



# now = 0
# n_list = list(map(int, list(n)))
# print(n_list)
# if int(n) < 10:
#     n_list = [0, int(n)]
# print(n_list)
# answer = 0
# while now != int(start):
#     add = n_list[0]+n_list[1]
#     new_n = n_list[1]*10 + add
#     n = str(new_n)
#     now = new_n
#     answer += 1
#     print(n,add,new_n,answer)


# n = int(input())
# if int(n) < 10:
#     n1, n2 = 0, int(n) 
# else:
#     n1, n2 = map(int, list(n))
# print(n1, n2)

# 처음값을 갖고 있어야해
# 재귀함수 an+1 = 전을 어떻게 했을때, 다음게 나오는가?
# def add(n, first,):
#     # 종료
#     # n, first가 같으면


#     print(n)
#     if n < 10:
#         n1, n2 = 0, n
#     else:
#         n1, n2 = map(int, list(str(n)))

#     return add(n2*10 + (n1+n2)%10, first)
# print(add(n, n))