'''
💪 수업 준비사항 💻
1. 하우코딩 수업 NIS 로그인
＊ID: agent@nis.com
＊PW: python
2.  VSCode LiveShare 링크 준비
'''

# 이차원리스트 : 리스트안에 리스트가 있는 형태의 데이터

# 5) 
ex=[
    #열(=칸): len(행)
    ['a','b','c'], # 행(줄)
    ['d','e','f'],
    ['g','h','i']
]

# 5-1) 0행 리스트를 출력해주세요.
print(ex[0])
# 5-2) 'e'는 몇번째행 몇번째열일까요? 1행 1열
print(ex[1][1])
# 5-3) 0행 2열의 데이터를 출력해주세요.
print(ex[0][2])
# 5-4) 2행 1열의 데이터를 출력해주세요.
print(ex[2][1])

# 리스트 : 여러가지 데이터(7가지 데이터타입 전체)를 저장하는 데이터타입
# 리스트에 데이터를 추가, 맨 뒤에다가 추가
# 리스트.append(추가할 데이터)


# 5-5) ex 이차원리스트에 마직막에j,k,l이 들어가는 행을 추가해주세요.
ex.append(['j', 'k', 'l'])
print(ex)

print('mission 3 -------')
# 이차원리스트 dron_sensing 농도데이터가 62를 초과한 호수를 구하여라.


# 0b110000 뭔가요?

# 2진수(binary)인지 10진수
# 0b1010
# 16진수 : 숫자 16개 : 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f
# https://www.google.com/search?q=%EC%83%89%EC%83%81%EC%84%A0%ED%83%9D%EB%8F%84%EA%B5%AC&rlz=1C5CHFA_enKR1149KR1149&oq=%EC%83%89%EC%83%81%EC%84%A0%ED%83%9D%EB%8F%84%EA%B5%AC&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIJCAEQABgKGIAEMgYIAhAAGB4yCAgDEAAYBRgeMggIBBAAGAUYHjIICAUQABgFGB4yCggGEAAYBRgKGB4yCAgHEAAYBRgeMggICBAAGAUYHjIICAkQABgFGB7SAQg0NjA1ajBqN6gCCLACAfEFKVL9qm011cHxBSlS_aptNdXB&sourceid=chrome&ie=UTF-8


# 이차원리스트 
dron_sensing = [
    # [호수, 농도데이터1열]
    [5,0b110000],
    [9,0b011101],
    [10,0b100100],
    [11,0b111100],
    [12,0b111101],
    [14,0b10110],
    [15,0b100101],
    [16,0b110000],[17,0b110011],[18,0b100100],[19,0b111100],[23,0b111101],[30,0b111101],[33,0b111111]]  
for i in range(len(dron_sensing)):
    # int(2진수) : 10진수 정수타입으로 변경
    print(dron_sensing[i][1])
    # 출력된 값이 62보다 초과하다면 호수를 출력해주세요.
    if int(dron_sensing[i][1]) > 62:
        print('wjdekq', dron_sensing[i][0])


# 조건문
# <조건문>
# 비교 : == != > < > <
# 논리 : 조건 and 조건, 조건 or 조건, not 조건
# 포함연산자 : 찾는데이터 in 리스트 => 포함되어 있다 True / 안포함 => False
#           찾는데이터 not in 리스트 => 안포함되어 있다 True / 포함 => False


# 3월 
# 월 10~11시 수 9:30~10:30  