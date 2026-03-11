import random
# (과제) - 함수로 만들기
# 로또 시스템: 1~45까지의 숫자중에서 6개를 자동으로 뽑기
# - 정답을 주기 [8, 23, 31, 35, 39, 40]
# - 내가 뽑은 숫자는 중복없이 6개가 되야한다.

#정답과 로또의 당첨이 3개면 "4등" 4개면 "3등" 5개면 "2등" 6개 "1등"

# 기능
# (1) 자동 로또 뽑기(숫자 6개)
# (2) 로또번호 결과 확인
# (3) 장수를 입력받으면 n장 로또를 여러장 생성한 다음에 => 로또 결과를 한번체 확인하기
# (4) 키보드로 6장번호 수동 뽑기
#  - 데이터를 잘못 넣으면 "로또뽑기에 실패햇습니다." 뜨기 
#  => 데이터가 잘못될 경우 생각하기, 입력도 어떤방식으로 할지 생각해보세요.

answer = [8, 23, 31, 35, 39, 40]

def lotto_auto():
    pick = []
    while len(pick) < 6:             # while 조건 : 조건이 만족하면 반복하다.
        num = random.randrange(1,46)
        if num not in pick:
            pick.append(num)
            # print(pick)
    pick.sort()                      # 리스트 정렬하기 => sorted(리스트) 리스.sort()
    return pick

# 터치금지-----------------

# rank() 로또 결과를 내보내는 함수
# - 입력 : 로또번호
def rank(p):
    total = 0
    for j in range(len(p)):
        if p[j] in answer:
            total = total + 1
        
    # print(p, total)
    if total == 3:
        return '4등'
    elif total == 4:
        return '3등'   
    elif total == 5:
        return '2등'
    elif total == 6:
        return '1등'
    else:
        return '다음기회에'



#-------- 건들지 마시오 ------------
# for i in range(100):
#     p = lotto_auto()
#     print(p, rank(p))   

cou = int(input())
# print(cou)
pick_total = []
for i in range(cou):
    pick_total.append(lotto_auto())
# print(pick_total)
for i in range(len(pick_total)):
    print(pick_total[i], rank(pick_total[i]))

