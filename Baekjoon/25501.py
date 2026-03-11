# 재귀의귀재 https://www.acmicpc.net/problem/25501
# (슈퍼주니어-로꾸꺼) 수박이박수 이효이

def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))

t = int(input())

for i in range(t):
    s = input()
    print(isPalindrome(s))










