print("missin 2 ===========")
# 다음에 사용될 ATM 기기를 구해보기

account_details =[
    {'date':'0201','type':'withdraw','account':'211-854-6681','amount':132500,'memo':'-..', 'atmSection':'PA1101'},
{'date':'0205','type':'withdraw','account':'121-554-1820','amount':106000,'memo':'--', 'atmSection':'FG1001'},
{'date':'0205','type':'withdraw','account':'211-157-3580','amount':130000,'memo':'---', 'atmSection':'HT1010'},
{'date':'0207','type':'deposit','account':'202-3207-8819','amount':50000, 'memo':'Jovia'},
{'date':'0201','type':'pay','account':'554-6280-7772','amount':100000,'memo':'Emily'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':123000,'memo':'-.', 'atmSection':'PA1101'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':167000,'memo':'.-', 'atmSection':'FG1001'},
{'date':'0204','type':'deposit','account':'260-415-2919','amount':16000,'memo':'John'},
{'date':'0204','type':'withdraw','account':'211-854-6720','amount':180000,'memo':'..-.', 'atmSection':'HT1010'},
{'date':'0201','type':'withdraw','account':'115-854-1280','amount':230000,'memo':'..', 'atmSection':'PA1101'},
{'date':'0202','type':'withdraw','account':'131-555-6000','amount':251000,'memo':'-.', 'atmSection':'FG1001'},
{'date':'0203','type':'deposit','account':'243-31-5325','amount':15000,'memo':'Nugu'},
{'date':'0204','type':'deposit','account':'463-433-0205','amount':7050,'memo':'Samuel'},
{'date':'0201','type':'withdraw','account':'221-554-6880','amount':300000,'memo':'-..', 'atmSection':'HT1010'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':113700,'memo':'--', 'atmSection':'PA1101'},
{'date':'0204','type':'deposit','account':'206-415-2919','amount':16000,'memo':'Harry'},
{'date':'0201','type':'withdraw','account':'628-7490-5471','amount':213700,'memo':'---', 'atmSection':'FG1001'},
{'date':'0201','type':'withdraw','account':'128-2196-5471','amount':113700,'memo':'-.', 'atmSection':'HT1010'},
{'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-', 'atmSection':'PA1101'},
{'date':'0204','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..-.', 'atmSection':'FG1001'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..', 'atmSection':'HT1010'},
{'date':'0202','type':'withdraw','account':'131-554-6000','amount':221000,'memo':'-.', 'atmSection':'PA1101'},
{'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},
{'date':'0204','type':'deposit','account':'2463-433-0205','amount':7050,'memo':'Samuel'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':300000,'memo':'-..', 'atmSection':'FG1001'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':313700,'memo':'--', 'atmSection':'HT1010'},
{'date':'0204','type':'deposit','account':'2060-415-2919','amount':16000,'memo':'Ann'},
{'date':'0204','type':'withdraw','account':'111-554-6880','amount':320000,'memo':'---', 'atmSection':'PA1101'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':24000,'memo':'Betty'},
{'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Norman'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':371200,'memo':'-.', 'atmSection':'FG1001'},
{'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-', 'atmSection':'HT1010'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Betty'},
{'date':'0202','type':'withdraw','account':'131-554-6000','amount':1000,'memo':'DrFisher'},
{'date':'0204','type':'withdraw','account':'2463-433-0205','amount':7050,'memo':'Samuel'},
{'date':'0204','type':'withdraw','account':'111-554-6880','amount':530000,'memo':'..-.', 'atmSection':'PA1101'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':130000,'memo':'..', 'atmSection':'FG1001'},
{'date':'0202','type':'withdraw','account':'131-554-6000','amount':109400,'memo':'-.', 'atmSection':'HT1010'}]

# account_details 변수에서 atm기기가 있을때만 출력하기

for i in range(len(account_details)):
    ad = account_details[i]
    if ad.get('atmSection') != None:
        print(ad.get('atmSection'))
    


# 720p : 세로 픽세이 720개 구성하기
# 1040p : 세로 픽셀 1040개


# 몽타주
criminal = [
[200,233,187,215,78,41,32,240,188,94],
[107,9,215,4,215,72,211,72,0,73],
[86,94,6,211,41,107,102,6,11,82],
[94,6,94,86,41,72,107,2,72,103],
[32,215,5,187,187,2,9,86,211,211],
[84,52,7,222,4,86,13,216,10,35],
[0,215,215,121,5,215,86,4,15,42],
[210,83,103,23,215,2,22,103,145,75],
[81,60,28,5,210,145,72,145,200,46],
[66,20,1,99,7,145,48,103,229,83],
]

suspect1 = [
[32,15,225,17,187,12,9,86,90,20],
[200,233,87,215,78,41,32,20,1,5],
[10,6,14,8,111,723,109,12,72,103],
[12,25,115,217,107,72,66,86,4,198],
[107,9,215,4,215,72,211,72,0,75],
[107,9,215,4,215,72,211,72,0,75],
[0,90,215,121,5,130,86,4,130,42],
[147,248,90,24,86,130,98,55,12,2],
[81,60,28,25,210,145,72,145,130,46],
[66,20,1,99,7,145,48,103,229,52],
]

suspect2 = [
[8,250,45,144,25,240,153,112,114,150],
[218,185,178,176,250,110,70,51,151,99],
[107,9,215,4,215,72,211,72,0,73],
[162,66,78,241,201,110,70,51,151,10],
[196,88,221,36,234,34,73,113,210,167],
[102,102,243,160,241,147,218,158,20,1],
[147,248,90,24,86,130,98,55,12,2],
[200,233,187,215,78,41,32,240,180,94],
[81,60,28,5,210,145,72,145,200,46],
[32,215,5,187,187,772,9,86,211,11],
]

suspect3 = [
[200,233,87,215,78,41,32,240,180,94],
[166,220,1,99,7,145,8,13,29,80],
[32,15,225,17,187,12,9,86,90,20],
[10,6,14,8,111,723,109,12,72,103],
[107,9,215,4,215,72,211,72,0,75],
[84,52,7,222,4,86,13,216,10,35],
[147,248,90,24,86,130,98,55,12,2],
[200,233,187,215,78,41,132,20,40,94],
[81,60,28,25,210,145,72,145,200,46],
[12,25,115,217,107,72,66,86,4,198],
]

suspect4 = [
[200,233,187,215,78,41,32,240,188,94],
[107,9,215,4,215,72,211,72,0,73],
[86,94,6,211,41,107,102,6,11,82],
[94,6,94,86,41,72,107,2,72,103],
[32,215,5,187,187,72,9,86,211,211],
[84,52,7,222,4,86,13,216,10,35],
[0,215,215,121,5,215,86,4,15,42],
[210,83,103,23,215,2,22,103,145,75],
[81,60,28,5,210,145,72,145,200,46],
[66,20,1,99,7,145,48,103,229,83],
]

suspect5 = [
[34,35,242,202,149,214,221,3,90,20],
[200,233,87,215,78,41,32,20,1,5],
[10,6,14,8,111,723,109,12,72,69],
[12,25,115,217,137,72,66,198,4,12],
[107,9,215,4,215,72,198,94,0,47],
[107,9,215,204,232,72,93,72,0,75],
[3,90,215,121,5,130,86,4,130,42],
[147,248,90,24,86,130,98,55,12,2],
[81,60,28,25,210,145,72,145,202,6],
[147,248,17,47,62,65,8,55,12,52],
]

# 몽타주랑 용의자 얼굴을 비교해서 점수로 만드는 함수를 만들기
# - 입력 : 몽타주, 용의자 
# - 결과 : 점수(숫자)
print("mission 3 ---------")

# 함수: 독립된 공간
def compare(cri, sus):
    # 같은 위치 : 행과 열이 같아야 같은 위치
    # 같은 위치의 값이 서로 같으면 1점 추가 해서 계산하기
    
    #print(cri, sus)
    point = 0
    # for i in range(10):
    for i in range(len(cri)):
        cri_row = cri[i]
        sus_row = sus[i]
        for j in range(len(cri_row)):
            cri_col = cri_row[j]
            sus_col = sus_row[j]
            if cri_col == sus_col:
                # point = point + 1
                point += 1
                # (+= : 더해서저장하기) (-= : 빼서 저장하기) (*=: 곱해서 저장하기)
                # (/= : 나눠서저장하기) (%= : 나머지구해서 저장하기) 
            
            # 열 c

    return point

print(compare(criminal, suspect1))
print(compare(criminal, suspect2))
print(compare(criminal, suspect3))
print(compare(criminal, suspect4))
print(compare(criminal, suspect5))