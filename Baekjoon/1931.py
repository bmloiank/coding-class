# 회의실 배정 https://www.acmicpc.net/problem/1931

# n개
# 각팀별소 회의 시작시간 - 끝시간
# 



# 
'''
11팀
1 4✅
3 5
0 6
5 7✅
3 8
5 9
6 10
8 11 ✅
8 12
2 13
12 14✅


    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
A   -------✅
B       -----
C   -----------
D           ------✅
E       -------------
F           -----------
G              ----------
H                  ---------✅
I                  -----------✅
J     -----------------------------
K                             -------✅

=> 1. 시작시간부터 빠른것부터 접근
=> 2. 회의시간이 짧은것
=> 3. 아 빨리끝나는게 좋다 ✅(채택)
# => 종료시점이 빠른것부터 보겠다
# => 종료시점이 빠른 순으로 정렬해서 해보자.

'''

n = int(input())
time = []
for i in range(n):
   time.append(list(map(int, input().split())))
# print(time)

# key=정렬기준 => [끝,시작] 이렇게 정렬기준으로 삼고 싶다!!
#[[시작,끝],[시작,끝],[시작,끝],[시작,끝]]
# apple abc abd

# def sort_key(x):
#    return (x[0],x[1])

# lambda x: return내용을 바로
time = sorted(time,key=lambda x: (x[1], x[0]))
'''
회의시간목록
0
[1, 4]
- 다음시작시간 4(이전끝시간)보다 커야된다. [5, 7]
- 다음시작시간 7(이전끝시간)보다 커야한다. [8, 11]

[[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

'''
# 마지막 회의타끄\
count = 0
end_time = 0
for i in range(n):
   start, end = time[i]
#    print(end_time)
   if end_time <= start:
      end_time = end
      count += 1
print(count)



# 전자레인지 https://www.acmicpc.net/problem/10162
# 구간 합 구하기4 https://www.acmicpc.net/problem/11659    