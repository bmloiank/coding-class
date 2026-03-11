'''
5. 딕셔너리 dictionary {}
- key-value 쌍으로 이루어진 데이터타입
  => key- (리스트) 인덱스와 같은 역할, 찾는얘    / value - 나오는 값
- 순서(=인덱스) 없습니다. => 인덱싱, 슬라이싱 X
- 값을 뽑기
 (1) 변수이름['key'] :없으면 Error (항목이 반드시 있고, 일정할때)
 (2) .get('key') : 없으면 None (어떨땐 있고, 어떨땐 없을수 잇는)

- 딕셔너리.keys() : 키값만 리스트로 원할때 
- 딕셔너리.values() : value값만 리스트로원할때
- 딕셔너리.items() : key-value하나의 쌍으로 리스트로 원할때 => 딕셔너리의 반복

- 딕셔너리 저장(추가,수정),삭제 가능
(1) 딕셔너리['key'] = value
(2) # .pop() : 맨뒤의 값 제거
# .pop(인덱스) : 해당 인덱스 제거
# .pop('key') : 해당 Key제거

'''

'''
5. 딕셔너리 dictionary {}
- key-value 쌍으로 이루어진 데이터타입
  => key- (리스트) 인덱스와 같은 역할, 찾는얘    / value - 나오는 값
- 순서(=인덱스) 없습니다. => 인덱싱, 슬라이싱 X
- 값을 뽑기
 (1) 변수이름['key'] :없으면 Error (항목이 반드시 있고, 일정할때)
 (2) .get('key') : 없으면 None (어떨땐 있고, 어떨땐 없을수 잇는)

- 딕셔너리.keys() : 키값만 리스트로 원할때 
- 딕셔너리.values() : value값만 리스트로원할때
- 딕셔너리.items() : key-value하나의 쌍으로 리스트로 원할때 => 딕셔너리의 반복


6. 튜플 Tuple ()

'''


f = {'apple':'사과', 'banana':'바나나', 'cherry':'체리'}
print(f.keys())
# 결과 : dict_keys(['apple', 'banana', 'cherry'])
print(f.values())
# 결과 : dict_values(['사과', '바나나', '체리'])
print(f.items())
# 결과 : dict_items([('apple', '사과'), ('banana', '바나나'), ('cherry', '체리')])


print("mission 1 ------------")
# <변수>용도_데이터타입
# num_list
# text_list
# class_num
############
# ip 중복되지않는 데이터를 원합니다.
ip_list = []
reduced_log = [{'time': '1014', 'ip': '89.149.233.0', 'type': 'trade', 'item': 'wiz asset', 'price': 40000, 'res_code': 504}, {'time': '1508', 'ip': '89.149.233.20', 'type': 'trade', 'item': 'wiz asset', 'price': 45000, 'id': 'haha160'}, {'time': '1500', 'ip': '89.149.233.30', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'son1257'}, {'time': '1048', 'ip': '89.149.233.3', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'wyre97'}, {'time': '1353', 'ip': '89.149.233.48', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'lala20'},{'time': '1510', 'ip': '89.149.233.30', 'type': 'trade', 'item': 'wiz asset', 'price': 6000, 'id': 'son1257'}, {'time': '1248', 'ip': '89.149.233.3', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'wyre97'}, {'time': '1553', 'ip': '89.149.233.48', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'lala20'}]
for i in range(len(reduced_log)):
    #print(reduced_log[i])
    rd = reduced_log[i]
    # rd : 딕셔너리
    print(rd.get('ip'))
    if rd.get('ip') not in ip_list:
        ip_list.append(rd.get('ip'))
print(ip_list)



print("mission 2 ------------")
# 가짜ip랑 진짜ip key-value형태로 묶여있는 데이터

fpn_db = {'41.222.235.255':'41.93.255.255','154.65.127.255':'102.36.183.255','196.13.123.255':'196.13.175.255','102.38.191.255':'102.69.223.255','102.131.16.255':'102.69.247.255','102.223.173.255':'43.251.120.0','43.246.152.0':'43.247.104.0','27.117.192.0':'46.235.128.0','185.104.203.255':'185.110.39.255','93.114.189.255':'92.114.55.255','89.43.173.255':'89.42.175.255','89.37.59.255':'85.204.192.255','212.77.31.255':'178.170.211.255','204.231.240.255':'37.203.199.255','109.234.103.255':'212.120.159.255','217.173.223.255':'185.217.20.0','185.176.128.0':'91.214.173.0','89.149.233.36':'218.155.162.150','89.149.233.0':'119.235.64.0','218.150.009.000':'218.150.980.709','45.221.240':'106.246.246.138','160.119.108':'164.160.255.255','45.222.191.255':'45.221.24.255','41.66.255.255':'196.43.242.255','196.43.225.255':'196.43.207.255','196.43.194.255':'196.201.2.255','41.189.191.255':'41.191.247.255','169.239.251.255':'192.251.202.255','193.108.23.255':'193.108.28.255','196.40.159.255':'196.201.5.255'}

# ip_list에서 fpn_db안에 있는 ip가 가짜 입니다.
# fpn_db의 key뽑아서 요ㅔ ip_list있느냐? 

# fpn_db모든 key,value값을 출력해보기
# 보통은 .items() 사용해서 반복돌리기
# for  k,v   in 딕셔너리.items():

original_ip = ''
for key, value in fpn_db.items():
    # print(key,'/',value)
    #해당 key가 ip_list있으면 가짜일때, 진짜 ip value를 출력해주기
    if key in ip_list:
        # 89.149.233.0 / 119.235.64.0
        print(value)
        original_ip = value


print("mission 3 ------------")
# original_ip에 저장되어있다.
# 
# 119.235.64.0
# 3.3.3.1
# (국가).(구체적위치)

ip_map_country = {'121':'Guam','45':'Brazil','197':'Namibia','14':'Japan','185':'Spain','78':'France','103':'Singapol','119':'Netherlands','89':'Fiji island','91':'Bulgaria','14':'china','5':'Poland','45':'Philippines','77':'Finland','85':'Serbia','160':'Morocco','88':'Lithuania','46':'Armenia','199':'Switzerland','170':'Argentina','115':'Mongolia','23':'United States','200':'Mexico','5':'Russia','80':'Germany','109':'Island','196':'Cuba','41':'Kenya','185':'Czechoslovakia','14':'Australia','80':'Algeria','43':'Vietnam','103':'Laos'}
ip_map_address = {'121':'western donnie AVE-17','45':'Maureen plaza -70','197':'National Science Building-16','14':'East Lansing MI-4','185':'Memphis street-197','78':'Lauren Street_50','103':'Louis Mo-19','89':'William Street-5','235':'Upper Alma Road-9','91':'Parla AVE-80','14':'New sum Street-193','5':'Years building-8','45':'Phlia AVE-55','77':'Fin Street-90','85':'Serbia building-6','160':'Eckman horse Street-10','88':'Lith building-1002','46':'Ralph AVE-22','199':'Suite Street 179','170':'Argen AVE-66','115':'Mon von AVE-80','23':'United Sorborn building-78','200':'Ashford APT-27','5':'Cond Garden hills-8','80':'Luke Plaza-25','109':'Parlia Apt-103','196':'Cubanian Street-5','41':'Calle Amapolas Apt-105','185':'Czech AVE-72','14':'Del Mar Apt-26','80':'East Algeria Street-2','43':'Upper Julian AVE-26','103':'Maximilian Apt-8'}
o = original_ip.split('.')
print(o)
c = o[0]
a = o[1]

co = ip_map_country.get(c)
print(co)
ad = ip_map_address.get(a)
print(ad)





f = {'apple':'사과', 'banana':'바나나', 'cherry':'체리'}
# 추가 : strawberry = 딸기
f['strawberry'] = '딸기'
print(f)

# 수정 : 'apple' : '빨간사과'로 수정하기
f['apple'] = '빨간사과'

print(f)

# 삭제 : banana를 삭제해주세요.
# .pop() : 맨뒤의 값 제거
# .pop(인덱스) : 해당 인덱스 제거
# .pop('key') : 해당 Key제거
f.pop('banana')
print(f)

f.pop("apple")
f["Apple"]="사과"
