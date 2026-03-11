print("mission 1 ==========")
# 2칸 오른쪽으로 밀어서 나온 단어 word
# 원래 암호는 뭐가 되었을까?
word1 = ['o','q','q','p','r','a']
#       [m o o n p y]




# 함수로 만들기
# 기능 : 암호화된 단어를 트랜스포지션암호화를 복호화 해주기
# 입력 : 암호,몇칸 밀었는지 
# 결과 : 복호화된 암호(문자열)

def trans(w, step):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # c(2번째) -(복호화)> a(0번째)
    # (1) 암호화된 단어의 각 알파벳을 출력하고
    # (2) 각 알파벳의 인덱스를 확인해보기
    # (3) (2)인덱스에서 2칸을 왼쪽으로 밀기
    # (4) (3)인덱스의 알파벳을 가져와야한다.

    decode_w = ''
    for i in range(len(w)):
        # print(w[i],"문자-------")
        for j in range(len(alphabet)):
            #print(alphabet[인덱스])
            if w[i] == alphabet[j]:
                #print(alphabet[j - step]) 
                # decode_w = decode_w + alphabet[j - step]
                decode_w += alphabet[j - step]
    return decode_w
    
print(trans(word1, 2)) 
print("mission 2 ==========")
# 문제 2) 8칸 밀기

word2 = ['q','u','q','b','i','b','q','w','v']
print(trans(word2, 8))

print("mission 3 ==========")
# 리스트를 정렬 
# 리스트.sort()    : 원본이 바뀌는 정렬
# sorted(리스트)   : 정렬해서 새로운 리스트가 결과로 나오는 것
slides = {7:'catch criminals,',1:'Dear',14:'is best',3:'I made',4:'project MONA',6:'our country,',8:'and find the',10:'other countries',11:'— so please',13:'Think about what',15:'for this country.',18:'Idle.',16:'Sincerely,',17:'Dr.',2:'President:',9:'spies from',12:'let me continue.',5:'to protect'}
# 딕셔너리에서 리스트처럼 쓰게되면 기본적으로 key값만 사용이됩니다.
# 딕셔너리를 리스트로 만드는 방법
# - .keys()
# - .values()
# - .items()
# 순서대로 문장을 만들어라!!!
# 변수명 : 기능_분류_타입
santance = ''
slides_list = sorted(slides.items())
for i in range(len(slides_list)):
    print(slides_list[i][1])
    # if i !=0:
    santance = santance + ' ' + slides_list[i][1]
    # else:
    #     santance += slides_list[i][1]
    
print(santance.strip(' '))
# 앞뒤에 특정 문자를 지울수가 있습니다. 문자열변수.strip(지울문자)
#@@@@@hi@@@python@@@@@@
# hi@@@python


# 예고1) 이차원리스트의 탐색
