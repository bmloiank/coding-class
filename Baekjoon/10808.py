# 13. (과제) 알파벳의 갯수 https://www.acmicpc.net/problem/10808

s = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = []
s = list(s)
for j in range(len(alpha)):
    answer.append(0)
    for i in range(len(s)):
        # answer.append(0)
        if s[i] == alpha[j]:
            answer[j] += 1
        # elif  alpha[i] not in s:
        #     answer[i] = 0
for k in range(len(answer)):
    answer[k] = str(answer[k])
print(' '.join(answer))













