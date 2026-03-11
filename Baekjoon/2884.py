'''
9. (3월26일 과제) 알람시계 https://www.acmicpc.net/problem/2884
'''
sanggeun = input().split(' ')
s_h = int(sanggeun[0])
s_m = int(sanggeun[1])
full_m = s_h*60 + s_m
changyeong = full_m - 45
c_h = changyeong//60
c_m = changyeong%60
if c_h < 0:
    c_h = 24 + c_h
print(c_h, c_m)







