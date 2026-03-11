# https://www.acmicpc.net/problem/1157

word = input().upper()
# print(word)
alph = []
count = []
for i in range(len(word)):
    # print(word[i])
    if word[i] not in alph:
        alph.append(word[i])
for i in range(len(alph)):
    count.append(0)
# print(alph, count)
for i in range(len(word)):
    for j in range(len(alph)):
        if word[i] == alph[j]:
            count[j] = count[j] + 1
            # print(count)
count_sort = sorted(count)
big_num = count_sort[-1]
big = []
for i in range(len(alph)):
    if count[i] == big_num:
        big.append(i)
# print(len(big))
if len(big) == 1:
    print(alph[big[0]])
else:
    print('?')
