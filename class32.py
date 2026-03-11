 # 해쉬(Hash) <-> 딕셔너리(key-value)
# - 주어진 값(Key)을 value(해쉬값)로 매칭하는 과정(해싱)



'''
hashtable, bucket 데이터 생성부. 수정하지 않습니다.
'''
# 차고사이즈 500개
garage = 500

password = []
import random
random.seed(29)
for i in range(garage):
    password.append(random.randint(1111,9999))

'''
hashtable, bucket 데이터 생성부. 수정하지 않습니다.
'''


# 6657 => 차고157번 4418
# 4762 => 차고 262번 3757


# ==key(차량번호)=>  ------해쉬함수-----  ====해쉬값(차고번호)====>
#   0000~ 9999    |    충돌체크      |    500개 (충돌나는건 다음번호로 매핑시켜주기)
#                 | (차고에 매핑체크)  |
#                 |  (buckets)     |

# 차고 500개의 입출입 체크 리스트를 만들어보기
# => 맨처음에는 아무차량도 들어가지 않습니다. 0으로 500개 셋팅하기

bucket = [0] * 500
# print(bucket)

# collision
# 차고번호를 넣어주고, 1씩 늘려주면서 충돌을 안할때까지 반복하기
def crash(garnum):
    while bucket[garnum] != 0:
        garnum = garnum + 1
    return garnum

def hashfunc(carnum):
    garnum = carnum % 500
    # 만약에 내가 뽑은 차고번호에 실제로 차량이 없으면 들어가게하기
    if bucket[garnum] != 0:
        print("충돌!!!!!!!, 새로운 번호 찾음")
        garnum  = crash(garnum)

    bucket[garnum] = 1
    return garnum


    

car6657 = hashfunc(6657)
print(car6657,"pw",password[car6657])
car4762 = hashfunc(4762)
print(car4762,"pw",password[car4762])
car7657 = hashfunc(7657)
print(car7657)
car8657 = hashfunc(8657)
print(car8657)


# 1809 => 차고 번호 =>주차비밀번호
car1809 = hashfunc(1809)
print(car1809,'pw',password[car1809])