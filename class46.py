# 2025 제5회 청소년 IT경시대회
# https://kitpa.org/contest/5

def f(a, b):
    if a == b:
        print(a)
        return
    c = a + (b - a) // 4
    print(a,b,c,"----")
    f(a, c)
    f(c+1, b)
f(0, 9)



# 주차요금 정산기 https://www.acmicpc.net/problem/33753
# 격자막기 https://www.acmicpc.net/problem/33754
# 논리연산과 쿼리 https://www.acmicpc.net/problem/33757


# math 수학
# datetime 시간날짜
# collections 컨테이너 데이터들을 관리하는 모듈
# os 파일을 복사한다던지, 파일을 생성하거나 디렉토리 관리한다던지 os관련된 모듈
# sys 모듈 파이썬 시스템(인터프리터)이 동작하느데 제어하는 모듈 입력, 출력

# pickle 모듈을 이용하면 원하는 데이터를 자료형의 변경없이 파일로 저장하여 그대로 로드






# s = -20
# s += 1
# s %= 5 
# print(s)

# # 나머지 양수여야한다.
# -19 % 5 = 4 +1 




ans = ""
# "False" != False
if "False":
    ans += "1"
    print("있다")
if []:
    ans += "2"
    print("있다")
if -10:
    ans += "3"
    print("있다")

print(0b1101101)
print(9<<3)


a, b, c = [], [], [] 
d = 0
for i in range(3):
    a.append(i+2)
    b.append(i*4)
    c.append(i*i)
for i in range(3):
    for j in range(3):
        for k in range(3):
            d += a[i] + b[j] * c[k]
            print(b[j]*c[k])
print(d)


print(len('savefromtheavalanche'))



# s, t = input().split()
# r = len(s)
# p = len(t)
# i = 0
# while i <= len(s)-p:
#     j, u = 0, 0
#     if s[i] == t[j]:
#         for j in range(1, p):             
#             if s[i+j] != t[j]:                
#                 u = 1
#                 i += 1
#                 break
#         if not u:
#             i += p
#             r -= p - 1
#     else:
#         i += 1
# print(r)

# savefromtheavalanche av
class Point:
    def __init__(self, x, y):         
        self.x = x
        self.y = y


n = int(input())
s = 0
p = [(0, 0)]
for i in range(n):
    a, b = tuple(map(int, input().split()))
    p.append((a, b)) 
p.append((0, 0))
p.sort(key = lambda a: (a[0], a[1]))
print(p)


