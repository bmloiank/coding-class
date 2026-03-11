# 재귀함수 **

def a(num):
    print("재귀",num)
    #  num <10보다 작으면 종료
    if num <= 0:
        print("ㅎㅎ")
        return 'ㅎㅎ'
    return a(num-1)


print("-----")
print("결과:", a(10))
# 5
#     4
#         3
#             2
#                 1
#                     return 0 => ㅎㅎ










