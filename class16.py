'''
<데이터타입>
1. 숫자타입 Number 
2. 문자열타입
3. bool타입
4. 리스트 [요소,요소,요소]
5. 딕셔너리 {key:value, key:value}
6. 튜플 (요소,요소,요소)
- 리스트랑 거의 동일합니다. => 인덱스 => 인덱싱, 슬라이싱
- 데이터를 추가,수정,삭제 안된다.

7. 집합 set {요소,요소,요소}                => 고 1학년 2학기
: 서로 다른 데이터의 모음(중복되는것은 허용하지 않는다.)
- 순서가 없습니다.

'''

# A,A ,B ,C ,B ,D ,A 가 들어있는 G집합을 만들어보자
g = {'A', 'A', 'B', 'C', 'B', 'D', 'A'}
print(g)
# set([리스트]) : 리스트를 집합으로 만들어주기
# - 다소 헷갈릴수 있다. 그래서 데이터를 리스트로 만들고 집합으로 변환해서 사용합니다.
a=set(['A', 'A', 'B', 'C', 'B', 'D', 'A'])
print(a)

# 교집합, 합집합, 차집합 
print("----교집합, 합집합, 차집합 ---")
math_hate= [ 'A', 'B', 'C', 'D']
en_hate=[ 'A', 'C', 'D',"E","F"]

# 예제1) 교집합 &을 구해보시오. 
math_hate = set(math_hate)
en_hate = set(en_hate)
print(math_hate & en_hate)
print(math_hate.intersection(en_hate))


# 예제2) 합집합 |을 구해보시오. 
print(math_hate | en_hate)

# 예제3) 수학만 싫어하는 집합을 구해보시오. 
print(math_hate - en_hate)
print(en_hate.difference(math_hate))



print("mission 1-------------")
# a,b,c,d 각각의 명단을 찾아주세요.


# a기관과 b기관이 함계 작업한 프로젝트의 명단
a_b = ['oak', 'guitar', 'butter', 'clover', 'moon', 'notepad', 'bird', 'pineapple', 'grass','spider','ring', 'sun', 'bear','space']
# b기관과 d기관이 함계 작업한 프로젝트의 명단
b_d = ['clover', 'moon', 'notepad', 'bird', 'pineapple', 'grass','spider','boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee']
# c기관과 d기관이 함계 작업한 프로젝트의 명단
c_d = ['boat', 'piano', 'seed', 'tumblr', 'popcorn', 'eagle', 'tank', 'cactus', 'fever', 'orange', 'papercup', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee']
# fox : d참여한 프로젝트 
d = ['boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee']

a_b = set(a_b)
b_d = set(b_d)
c_d = set(c_d)
d = set(d)
c = c_d - d
b = b_d - d
a = a_b - b
print(a)
print(b)
print(c)
print(d)

print("mission 2=================")
# 부분집합 : 부분집합 찾기 집합이름1.issubset(집합이름2) : 집합1이 집합2에 부분집합이냐?
# => 집합1이 작은거 집합2 큰거

# unknown에 들어간 기관 3개르 찾기
unknown = ['oak', 'guitar', 'butter','boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee', 'ring', 'sun', 'bear','space','tumblr', 'popcorn', 'eagle', 'tank', 'cactus', 'fever', 'orange', 'papercup']
print(a.issubset(unknown))
print(b.issubset(unknown))
print(c.issubset(unknown))
print(d.issubset(unknown))


# 서로소 : 겹치는 교집합이 없는 집합
# 집합1.isdisjoint(집합2) : 서로소이면 Ture 아니면 false


# => a,b,c기관의 공통된 프로젝트를 찾아라
a_pj = {'Food Nutrition', 'Legal Services', 'pharmaceutics','Cement and steel', 'Agriculture industry', 'Mining','Artificial Intelligence', 'Psychology','Vocational Rehabilitation', 'Plant-Based food','Transport', 'Urbanisation', 'Postal and Delivery', 'Financial Services', 'Travel and Leisure'}
c_pj = {'Systems Engineering', 'Data Science', 'Drones and Robots','Information Technology', 'Neurocomputing', 'Aerospace', 'Cloud Systems', 'Materials','Artificial Intelligence', 'Food Nutrition', 'Digital Computing','Software Farm', 'Power Sectors', 'Networking', 'Database', 'Psychology'}
d_pj = {'Data Researching','Government Services', 'Artificial Intelligence','Telecommunication','Construction', 'Urbanisation', 'Legal Services','Physical Assets', 'Banks and Cashes', 'Labour and Capital','Education', 'Financials', 'Drones and Robots'}
ac = a_pj & c_pj
acd = ac & d_pj
print(acd)