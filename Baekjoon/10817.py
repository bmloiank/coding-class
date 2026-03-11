# 21. (6/11 과제)세수 https://www.acmicpc.net/problem/10817

# input_str = input().split(' ')
# num = []
# for t in range(len(num)):
#     num.append(int(input_str[t]))
# deck = num[0]
# for i in range(len(num)):
#     if deck < num[i]:
#         deck = num[i]
# num2 = []
# for j in range(len(num)):
#     if deck != num[j]:
#         num2.append(num[j])
# deck2 = num2[0]
# for k in range(len(num2)):
#     if deck2 < num2[i]:
#         deck2 = num2[i]

input_str = input().split(' ')
num = []
for t in range(len(input_str)):
    a = int(input_str[t])
    num.append(a)
num = sorted(num)
print(num[1])

