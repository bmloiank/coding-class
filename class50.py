# 선택 정렬(Selection Sort)
# : 앞에서부터 뒤쪽값중에서 최소값과 스왑swap하기
def selectionSort(ilst):
    for i in range(len(ilst)-1):
        #print("대상",ilst[i],'----------')
        # 나머지 리스트 중에서 가장 작은값
        # print(ilst[i+1:])
        sublist = ilst[i+1:]
        # 최솟값의 위치를 알고싶다.
        # 최소값알고리즘
        # 임시 최소값을 설정하고
        # 만약에 임시 최솟값과 비교해서 더 작은값으로 교체
        # minn = sublist[0]
        minj = 0
        for j in range(len(sublist)):
            if sublist[j] < sublist[minj]:
                minj = j
        minj += i+1
        # print(minj)
        # 교체알고리즘
        
        if ilst[i] > ilst[minj]:
            # 교체 
            tmp = ilst[minj]
            ilst[minj] = ilst[i]
            ilst[i] = tmp
            #print(ilst)
    return ilst            


        
#data
class sample:
    def __init__(self, name, collection_time, inspection_time):
        self.name = name
        # 채집시간
        self.collection_time = collection_time
        # 검사 시간
        self.inspection_time = inspection_time
    
    # __str__ 메서드 : 문자열로 출력했을때, 내용 보이도록 하기
    # 이름 : {name} 채집시간 {} 검사시간 {} 출력하기
    def __str__(self):
        return f'채집:{self.collection_time} / 검사:{self.inspection_time} / 이름:{self.name} '

def print_object(tosort):
    for i in range(len(tosort)):
        object = tosort[i]
        print(object)

import random
random.seed(66)
 
namelist = ['John.W','Judith.G','Brett.N.O','Tracy.H.N','Michael.B','Melissa.R','Andrea.F','Thomas.W.J','Veronica.C','Blake.W','Darren.V','Scott.C','Bill.R.C','Jeffrey.S','Dwayne.C','Bruce.F','Sara.P','Stromy.U.J','Lala.P.V','Maddox.B']
collection_time = [205503180530, 205503180613, 205503180733, 205503180814, 205503180945, 205503181242, 205503181256, 205503181581, 205503181600, 205503181621, 205503181641, 205503181747, 205503181728, 205503181729, 205503181823, 205503181902, 205503191125, 205503191325, 205503191400, 205503191505]
inspection_time = [205503200901, 205503201014, 205503200312, 205503200611, 205503200212, 205503200632, 205503200239, 205503200017, 205503200420, 205503200311, 205503200538, 205503200018, 205503200603, 205503200131, 205503200021, 205503200135, 205503200011,205503200511,205503200411,205503200451] 
random.shuffle(inspection_time)

tosort = []
for i in range(len(namelist)):
    tosort.append(sample(namelist[i], collection_time[i],inspection_time[i]))

print(tosort)



# 검사 데이터로만 삽입정렬을 정렬하기
# : 앞에서부터 뒤쪽값중에서 최소값과 스왑swap하기

def selectionSort2(tosort, count):
    cnt = 0

    for i in range(len(tosort)):
        print("--------------------------")
        object = tosort[i]
        print("비교위치",i,object.inspection_time)

        # # (2) i+1번째 끝까지에서 검사시간이 최소값인 객체를 찾아
        # 최솟값 인덱스 번호를 갖고있어햐한다.
        small_index = i
        # 중복된 정보를 막아야해서ㅠㅠ 쓰면 안된다.
        # small = tosort[i].inspection_time
        for j in range(i+1,len(tosort)):
            if tosort[j].inspection_time < tosort[small_index].inspection_time:
                small_index = j
        print("뒤쪽의 최소값",tosort[small_index].inspection_time)

        # (3) 교체 (스왑)
        # i번째: 최소값
        #       값
        # 다중 할당 = 동시 교체
        # 교체가 12번째일때
        tosort[i], tosort[small_index] = tosort[small_index], tosort[i]
        cnt = cnt + 1
        if cnt == 12:
            return (tosort[12])
    print_object(tosort)
    return tosort
print(selectionSort2(tosort, 12))
