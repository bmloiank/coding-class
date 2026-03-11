# 2025 제5회 청소년 IT경시대회
# https://kitpa.org/contest/5

#data 
genetic_string = 'ATGTAATGGTTGCAGTCAATTGATGTCGTGCTCGAGCTGCAGCTAGCGATCGAGGCTTCCAGCGTAGCGTAGCGCGGTACGTCA'

# ATGTA
#  TGTAA
#   GTAAT
#    TAATG
#     AATG
# 모든 5글자를 잘라보기
def pal(case):
    # 여기안에다가
    # print(case)
    answer = True
    for j in range(len(case)//2):
        if case[j] != case[len(case)-j-1]:
            answer = False
    return answer

for i in range(len(genetic_string)-4):
    text = genetic_string[i:i+5]
    if pal(text):
        print(text)




# https://ichi.pro/ko/python-keollegsyeon-modyul-250859860348947