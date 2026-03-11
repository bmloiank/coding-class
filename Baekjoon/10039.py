# 12. (과제) 평균 https://www.acmicpc.net/problem/10039 (함수로 풀기)



def average():
    score_list = []
    for i in range(5):
        score = int(input())
        if score >= 40:
            score_list.append(score)
        elif score < 40:
            score_list.append(40)
        total = 0
        for j in range(len(score_list)):
            total += score_list[j]
        answer = total / 5
    return int(answer)
print(average())
















