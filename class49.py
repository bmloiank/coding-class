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


        

num_list = [4,5,2,1,3]
# num_list = ['a','c','f','z','b']
# num_list = ['가','그','기','고','거']
# num_list = ['11','22','133','213','444']

print(selectionSort(num_list))

'''
버블 정렬 (Bubble Sort)
- 서로 옆에 있는것 끼리 비교합니다.
- 작은값이 앞으로 오도록 자리 변경 => 큰게 맨 뒤로 먼저 결정

'''
def bubbleSort(ilst):
    for j in range(len(ilst)-1):
        for i in range(len(ilst)-j-1):
            if ilst[i] > ilst[i+1]:
                # tmp = ilst[i]
                # ilst[i] = ilst[i+1]
                # ilst[i+1] = tmp

                # 간단한 교체
                # 변수1,변수2 = [데이터여러개]
                # 변수1, 변수2 = 오른쪽데이터의 갯수와 맞춰서 매핑
                # 
                # a1, a2 = b1, b2
                ilst[i], ilst[i+1] = ilst[i+1],ilst[i]
            
        # 정렬 대상
        #print(ilst[-(j+1)])
    return ilst

num_list = [4,5,2,1,3]
print(bubbleSort(num_list))

a1, a2 = [1,2]
print(a1,a2)

print()
'''
삽입정렬(insertionSort)
# 1번째부터 ~끝까지 탐색을 진행하면서
# 자신의 앞에서 나보다 크고 나보다 작은 사이 인덱스 값을 찾기
# (1) 교체할 데이터를 변수에 따로 빼놓기
'''
def insertionSort(ilst):
    # for i in range(len(ilst)-1) # 0~
    for i in range(1,len(ilst)):
        #print(ilst[i], ilst,"-----")
        curr = ilst[i]
        index = i
        # index가 하나씩 앞으로 가면서 나보다 큰지를 비교하기
        # index가 0보다 작을때까지 반복하기 => 0보다 크면 반복하기
        while index > 0:
            # 전값이 기준값보다 작으면 브레이크
            if ilst[index-1] < curr:
                break
            # 작면 앞에 있던 숫자가 뒤로 밀리기
            ilst[index] = ilst[index-1]
            #print(ilst)
            # [2 4 5 *1* 3] index = 3 curr=1
            # [2 4 5 5 3]  index=2
            # [2 4 4 5 3]
            # [2 2 4 5 3]
            # [1 2 4 5 3]

            index = index - 1
        # 마지막에 결정된 위치(index)에 curr값ㅇ르 넣어줍니다.
        ilst[index] = curr
    return ilst


num_list = [4,2,5,1,3]
print(insertionSort(num_list))






'''
시간복잡도 : 알고리즘이 주어졌을때 해결하기 위해서 소요되는 시간 수식화
- 비용 Cost 항상 적을 수록 좋다.

프로그래밍에서는 => 최악의 시나리오 고려하는게 아주 중요하다.
(1) 최악의 경우     => 빅 오O 표시법
(2) 최선의 경우 (x) => 빅 오메가 Ω
(3) 평균의 경우 (x) => 빅 세타 


# 앞에 계수는 아무상관없음
<빠름>
O(1) : 입력값과 상관없이 항상 실행시간이 같은것

O(log n) : 고2               => 정렬, 최적화
O(n) : n개 -> n초
------------------

O(n log n^n) : 고2           => 정렬, 최적화

------------------
O(n^2): 1개 -> 초 2개 -> 4초 3-> 9초

------------------
<비추천 시간>
O(2^n): 재귀함수 => 중복 계산
O(n!) : 탐색 모든 경우의 수를 다 찾는 형태



<느림>
(https://velog.velcdn.com/images/ka0ka0ka/post/d3b258bf-f873-4f14-98f4-94073210ce9c/image.png)



'''

# O(1) : 상수시간
a =10
a=[1,2,3,4,5]
print(a[1])


# O(n) : 기본 반복문
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)):
    print(a[i])


# O(n^2) : 2중 for문
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[j])


 
# O(n!) : 탐색 모든 경우의 수를 다 찾는 형태
#








