# - DNA비밀번호 https://www.acmicpc.net/problem/12891

'''

18 8
GATAGAGATATACCGATA
2 0 1 1



'''
import sys
input = sys.stdin.readline

s, p = list(map(int, input().strip().split()))
dna_str = list((input().strip().lower()))
a, c, g, t = list(map(int, input().strip().split()))
dna_lst = {'a':0, 'c':0, 'g':0, 't':0}

for i in range(p):
    dna_lst[dna_str[i]] += 1

start = 0
count = 0

for end in range(p,s):
    if dna_lst['a'] >= a and dna_lst['c'] >= c and dna_lst['g'] >= g and dna_lst['t'] >= t:
        count += 1

    dna_lst[dna_str[start]] -= 1
    dna_lst[dna_str[end]] += 1
    start += 1

if dna_lst['a'] >= a and dna_lst['c'] >= c and dna_lst['g'] >= g and dna_lst['t'] >= t:
    count += 1
print(count)


print("========================")
from collections import deque
import sys
input = sys.stdin.readline

s, p = list(map(int, input().strip().split()))
dna_str = list((input().strip().lower()))
a, c, g, t = list(map(int, input().strip().split()))
dna_lst = {'a':0, 'c':0, 'g':0, 't':0}


w = deque()
count = 0
for i in range(s):
    if len(w) >= p:
        if dna_lst['a'] >= a and dna_lst['c'] >= c and dna_lst['g'] >= g and dna_lst['t'] >= t:
            count += 1
        out = w.popleft()
        dna_lst[out] -= 1
    w.append(dna_str[i])
    dna_lst[dna_str[i]] += 1
    # print(w)
    # print(dna_lst)
   
        # print("카운트",count)

if dna_lst['a'] >= a and dna_lst['c'] >= c and dna_lst['g'] >= g and dna_lst['t'] >= t:
    count += 1
print(count)