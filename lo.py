# (4) 키보드로 6장번호 수동 뽑기
#  - 데이터를 잘못 넣으면 "로또뽑기에 실패햇습니다." 뜨기 
#  => 데이터가 잘못될 경우 생각하기, 입력도 어떤방식으로 할지 생각해보세요.

# (5) 반자동뽑기
# - 엔터만 칠경우, => 자동으로 6개 뽑기
# - 1~5개 사이로 입력할 경우 => 모자란 갯수만큼 숫자 뽑기
# [1,2,3] +3개를 자동으로 뽑기
# - 6개를 다 입력할 경우 => 수동뽑기



# https://meet.google.com/wqu-ofee-sva

answer = [8, 23, 31, 35, 39, 40]

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



def lotto_manual():
    pick_manual = []
    while len(pick_manual) < 6:           # while 조건 : 조건이 만족하면 반복하다.
        pick = int(input())
        if pick > 45 or pick < 1:
            print("로또뽑기에 실패했습니다.")
        elif pick not in pick_manual:
            pick_manual.append(pick)
    pick_manual.sort()                      # 리스트 정렬하기 => sorted(리스트) 리스.sort()
    return pick_manual

p = lotto_manual()
print(p, rank(p))
