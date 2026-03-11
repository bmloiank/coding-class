# 논리연산과 쿼리 https://www.acmicpc.net/problem/33757
n, q = list(map(int,input().split(' ')))
form = list(input())
print(form)
k = list(map(int,input().split(' ')))
# print(n, q, form, k)
answer = []
def f(form):
    for i in range(len(form)):
        deck = form
        if deck[i] == '&':
            if deck[i-1] == '1' and deck[i+1] == '1':
                deck[i+1] = '1'
                print(deck[i-1], '&', deck[i+1])
            else:
                deck[i+1] = '0'
                print(deck[i-1], '&', deck[i+1])
        elif deck[i] == '|':
            if deck[i-1] == '1' or deck[i+1] == '1':
                deck[i+1] = '1'
                print(deck[i-1], '|', deck[i+1])
            else:
                deck[i+1] = '0'
                print(deck[i-1], '|', deck[i+1])
    print('------', deck[-1])
    return deck[-1]

for i in range(q):
    if form[2*k[i]-2] == '0':
        answer.append(f(form))
        form[2*k[i]-2] = '1'
    elif form[2*k[i]-2] == '1':
        answer.append(f(form))
        form[2*k[i]-2] = '0'
print(answer)


