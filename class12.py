#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")


# 2진수-> 문자열  => bin()
# =>int(2진수문자열,2) : 2진수를 10진수로 변환
# 0b1101010101010
q = 0b1001111001
q = bin(q)
q = int(q,2)
print(q)


print("mission 2=====")
# 여기서 무언가를 찾아야내합니다.
# 1이라는⬜  0띄어쓰기

num_list = [0b1011110000001111, 
            0b1010010000001001, 
            0b1010010111101001, 
            0b1011110100101001, 
            0b1010010111101001, 
            0b1010010100001001, 
            0b1011110111101111]
for i in range(len(num_list)):
    # 2진수를 문자열로 바꾸는 함수 bin()
    # print(num_list[i])
    o = bin(num_list[i]) #문자열
    # 문자열도 인덱스가 있기때문에 리스트처럼 반복돌려서 각각의 문자를 뽑아볼수가 있습니다.
    
    # print(o)
    for j in range(len(o)):
        # 1이라는⬜  0띄어쓰기
        #print(o[j])
        # print("",end="!") #:한줄씩 출력하는 함수 끝나면 줄바꿈이됩니다.
        # - end옵션: 출력이 끝나고 맨 뒤에 어떤것을 추가할것인가 결정
        #           기본 \n 줄바꿈 => 기본말고 변경이 가능해요.
        if o[j] == '1':
            print('⬜',end='')
        elif o[j] == '0':
            print('  ',end='')
    #한줄 입력이 완료되면 줄바꿈
    print('\n',end='')

# 리스트
# .split("구분인자"):  "문자열" => 리스트
# "구분인자".join(리스트) : 리스트 요소 사이에 구분인자를 넣어서 문자열이된다.

alpha = ["a","b",'c','d','e']
# 구분인자 /를 넣어서 문자열로 만들고싶어요.
print('/'.join(alpha))
# 문자열로 이어서 만들고싶어요.
print(''.join(alpha))


print("mission 3=====")
# - 대쉬가 수상하다!
# m의 -가 있는 위치 p의 글자들으 모아보고싶다.

p = 'We are a form of warfare. We aim to achieve maximum consequential impact for where   asymmetric happens. We attack where finite input allocation of resources   exists. objectives should be clearly defined and work norms and means adopted by the organization are acceptable to the individual and groups. Each Person   is responsible for completing   the work. Organisation will appoint the job should be done. should be set up in such a way that every individual should be assigned a duty according to his skill and qualification. The person should   continue the same work so that he specialises in his work. This helps in increasing production in the concern. The scope of authority and responsibility   should be clearly defined.   Every person should know his work with definiteness. If the duties are not clearly assigned.  then it will not be possible to fix responsibility also. Everybody’s responsibility will become nobody’s responsibility. The principle states that top management should interfere only when something goes wrong.   If the things are done as per plans then there is no need for the interference of top management.   The management should leave routine things to be supervised by lower cadres.   It is only in exceptional situations when attention of   top easy management is drawn.  The principle   relieves top management of many botherations and routine things. Principle of exception allows top   management to concentrate on planning game and policy formulation.   Important time of management is not   wasted on avoidable supervision. The responsibility of the superior does not decrease once he has delegated authority. A person   can delegate authority and not responsibility. We will remain for the work even if it is de legated to the subordinate accountable work. So the responsibility of superior and subordinate remains absolute.'
m = 'We are a form of warfare. We aim to achieve maximum consequential impact for where   as-mmetric happens. We attack where finite input all-cation of reso-rces - exists. objectives s-ould be cle-rly defined and work norms and means adopted by the organization are acceptable to the indi-idual and groups. Each P-rson - is responsi-l- for compl-ti-g - the work. Organisation will appoint the job shoul- be d-ne. should be set up in such a way that every individual should be assigned a duty accord--- to his skill and qualification. The person should - continue the same -ork so that h- specialises in his work. This he-ps in increasing production in the concern. The scope of authority and responsibi-ity - -h-uld be clearly defined. - Every person should know his work with de-initeness. If the duties --e not clearly assigned-- then it will not -e possible to fix responsibility also. Everybody’s responsibility will become nobody’s responsibility. The principle states that top management sho-ld in-erfere only when something goes wrong. - If the things are done as per plans then there -s no need for -he interference of top management. - The management should leave routine things to be supervised by lo-er c-dre-. - It is only in excep-i-nal situations when attenti-n of - top ---- management is drawn- ---- principle - --lieves top man-gement of many botherations and routine things. Princip-e of exception allows top - management to concentrate on planning ---- and policy formulation. - Important time of management -- not - --sted on avo-dable supervision. The responsibility of -he super-or does -ot decrease once he has dele-ated authority- A person - can dele-ate authority and n-t resp-nsibility. We will remain for the work even if it is -e--egated to the s-bordinate a-countable wor-. So the responsibility of superior and subordinate remains absolute-'
# 정답리스트
w = []
for i in range(len(m)):
    # print(m[i])
    if m[i] == '-':
        # print(i)
        print(p[i])
        w.append(p[i])
        #정답 리스트 모아준다음에 문자열로 바꿔보기
print(w)
print(''.join(w))


