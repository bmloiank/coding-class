# 17. 열개씩 끊어서 출력하기 https://www.acmicpc.net/problem/11721

inp = input()
n = len(inp)
# n 길이를 10나눈거 +1 만큼 출력되야한다.
#0번째반복 0~9
#1번째반복 10~19
#2번째반복 20~29
#3번째반복 30-39
for i in range(n//10):
    print(inp[i*10:(i+1)*10])
if n%10!=0:
    print(inp[(n//10)*10 :])






#### <주하 답변> ####
# inp = list(inp)
# # print(inp)
# t1 = []
# t2 = []
# t3 = []
# t4 = []
# t5 = []
# t6 = []
# t7 = []
# t8 = []
# t9 = []
# t10 = []
# for i in range(len(inp)):
#     if i < 10:
#         t1.append(inp[i])
#     elif i < 20:
#         t2.append(inp[i])
#     elif i < 30:
#         t3.append(inp[i])
#     elif i < 40:
#         t4.append(inp[i])
#     elif i < 50:
#         t5.append(inp[i])
#     elif i < 60:
#         t6.append(inp[i])
#     elif i < 70:
#         t7.append(inp[i])
#     elif i < 80:
#         t8.append(inp[i])
#     elif i < 90:
#         t9.append(inp[i])
#     elif i < 100:
#         t10.append(inp[i])
# # print(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10)

# t1 = ''.join(t1)
# t2 = ''.join(t2)
# t3 = ''.join(t3)
# t4 = ''.join(t4)
# t5 = ''.join(t5)
# t6 = ''.join(t6)
# t7 = ''.join(t7)
# t8 = ''.join(t8)
# t9 = ''.join(t9)
# t10 = ''.join(t10)

# aa = []
# aa.append(t1)
# aa.append(t2)
# aa.append(t3)
# aa.append(t4)
# aa.append(t5)
# aa.append(t6)
# aa.append(t7)
# aa.append(t8)
# aa.append(t9)
# aa.append(t10)
# # print(aa)

# for j in range(len(aa)):
#     if aa[j] != '':
#         print(aa[j])