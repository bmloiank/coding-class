'''
💪 수업 준비사항 💻
1. 하우코딩 수업 NIS 로그인
＊ID: agent@nis.com
＊PW: python
2.  VSCode LiveShare 링크 준비
'''


'''
<데이터타입>
1. 숫자타입 Number
2. 문자열타입 String "", ''
- 순서(=인덱스) => 인덱싱, 슬라이싱
3. bool타입 True(참)/False(거짓)
4. 리스트타입 List [요소,요소,요소]
- 순서(=인덱스) => 인덱싱, 슬라이싱
- 추가 .append(),수정 '=',삭제.pop()


<제어문>
1. 반복문(for문)

(1) 횟수반복
for i in range(횟수):
    #반복할 코드
    # 중요한거!) 반복문안에는 반복변수만이 바뀐다.



2. 조건문(if~elif~else)
(1) 조건문 형태
if 조건 :
    (들여쓰기) 조건이 만족할때 할 코드
elif 두번째 조건 :
    (들여쓰기) 위 조건이 만족하지 않고, 해당 조건이 만족할때 할 코드
else:
    모든 조건이 만족하지 않는다면 할 코드
    
(2) 조건 표현식
- 비교연사자 : == !=(다르다) > < >= <=
- 논리연산자 : A조건 and B조건(동시에, 그리고, ,) 
            A조건 or B조건 (또는, 둘중헤 하나, or)
            not A조건 (A조건이 아니다., 반대) 

'''


print('mission 1 ==========')
#문제) 기밀자료실이 있는 층을 모두 구하여라 ("secret")

# 시청의 각 층별로 용도가 적힌 리스트
purpose_list = ['general', 'office', 'office', 'general', 'office', 'general', 'office', 'office', 'office', 'secret', 'conference', 'conference', 'office', 'general', 'office', 'general', 'secret', 'office', 'general', 'secret', 'general', 'office', 'office', 'general', 'office', 'conference', 'office', 'office', 'office', 'conference', 'conference', 'conference', 'office', 'general', 'secret', 'general', 'office', 'secret', 'general', 'office']
#        층수   : 1층       , 2층     ,  3층    , 4층 
#        인덱스  :  0 

# 정답을 리스트로 만들어줄거예요.
a = []

# 리스트를 전체를 뽑는 방법  => 반복문 for문을 사용해서
for i in range(len(purpose_list)):
    # 만약에 출력한 값이 "secret"이라면~~
    if purpose_list[i] == 'secret':
        # 변수이름[인덱스] : []안에 있는게 인덱스
        print(i+1)
        # 정답을 정답리스트 a 추가해주기 리스트변수.appned(추가할 데이터)
        a.append(i+1)

print(a)

print('mission 2 ==========')
# 센서가 고장난 층을 모두 구하시오.'error'
b = []
sensor_list = ['error', 'error', '054057', '054324', '054326', '054327', 'error', 'error', '054345', '054352', '054353', '054359', '054404', '054406', '054411', '054412', '054413', '054414', 'error', 'error', '054415', '054416', 'error', 'error', 'error', 'error', '054421', '054422', 'error', 'error', '054425', '054426', '054427', '054428' , '054429', '054430', '054431', '054432', '054433', '054434']
for i in range(len(sensor_list)):
    if sensor_list[i] == 'error' :
        print(i+1)
        b.append(i+1)
print(b)

print('mission 3 ==========')
# 기밀자료실이면서 센서가 동시에 고장난 층을 구하여라

# 시청 용도랑 센서
purpose_list = ['general', 'office', 'office', 'general', 'office', 'general', 'office', 'office', 'office', 'secret', 'conference', 'conference', 'office', 'general', 'office', 'general', 'secret', 'office', 'general', 'secret', 'general', 'office', 'office', 'general', 'office', 'conference', 'office', 'office', 'office', 'conference', 'conference', 'conference', 'office', 'general', 'secret', 'general', 'office', 'secret', 'general', 'office']
sensor_list = ['error', 'error', '054057', '054324', '054326', '054327', 'error', 'error', '054345', '054352', '054353', '054359', '054404', '054406', '054411', '054412', '054413', '054414', 'error', 'error', '054415', '054416', 'error', 'error', 'error', 'error', '054421', '054422', 'error', 'error', '054425', '054426', '054427', '054428' , '054429', '054430', '054431', '054432', '054433', '054434']

for i in range(len(purpose_list)):
    # 모든층에 대한 용도값과 센서값을 출력해보기
    # print(purpose_list[i] , sensor_list[i])
    # 용도는 = 'secret", 센서 ="error" 동시에 and 
    if purpose_list[i] == 'secret' and sensor_list[i] == 'error':
        print(i+1)


# range(10) : 0~9까지의 연속된 숫자나오게하는 함수
for i in range(10):
    print(i) # 반복변수를 인덱스에 활용하면 리스트의 모든값을 뽑아볼수있다.
    print(1)
    print("a")
