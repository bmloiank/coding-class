# 20. (6/11 과제)최댓값 https://www.acmicpc.net/problem/2562

deck = []
deck_int = []
for i in range(9):
    deck.append(input())
for k in range(9):
    deck_int.append(int(deck[k]))
    # print(deck_int)
max_num = sorted(deck_int)[-1]
for j in range(9):
    if deck_int[j] == max_num:
        num = j+1
print(max_num)
print(num)

