# 18. 과제 안 내신 분..? https://www.acmicpc.net/problem/5597

submit = []
# 입력을 받기
for i in range(28):
    submit.append(input())

submit = sorted(map(int, submit))

# 학생번호가 1~30번까지
# print(submit)
answer = []
a = 1
# 제출한 학생을 모두 뽑는 형태 list(range(시작,끝))
# 다르다 1:1 비교
# 포함되어잇찌 않느냐? 1:다수
    
# alhpa = list("abcdefghjkliahkdlfjlq;")
student = list(range(1,31))
for j in range(len(student)):
    # 한명씩 뽑기
    # 이 번호가 제출한 명단에 없는가? 없으면 answer에 추가하면 된다.
    if student[j] not in submit:
        answer.append(student[j])
    
    # if submit[j] != j+a:
    #     answer.append(j+a)
    #     a += 1
    
answer = sorted(answer)

for k in range(len(answer)):
    print(answer[k])

