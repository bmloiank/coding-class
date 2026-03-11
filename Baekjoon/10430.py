'''
나머지 https://www.acmicpc.net/problem/10430

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

첫째 줄에 (A+B)%C, 
둘째 줄에 ((A%C) + (B%C))%C, 
셋째 줄에 (A×B)%C, 
넷째 줄에 ((A%C) × (B%C))%C를 출력한다.


입력)
첫째 줄에 A, B, C가 순서대로 주어진다.
'''
# 입력받기 input()
in_data = input()
in_data = in_data.split(' ')
# print(in_data)
a = int(in_data[0])
b = int(in_data[1])
c = int(in_data[2])
# print(type(a))
print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)



