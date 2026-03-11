# 우선순위 큐
# heap => 이진트리 구조로 바꿔주는 것

# heapq 모듈 : 우선순위큐 + heap
import heapq


# (1) q를 저장할 리스트 하나 생성하기
queue = []

# (2) 삽입
# heapq.heappush(리스트,"추가할데이터")
# 3,2,7,9,14,11,5 삽입하기
heapq.heappush(queue, 3)
heapq.heappush(queue, 2)
heapq.heappush(queue, 7)
heapq.heappush(queue, 9)
heapq.heappush(queue, 14)
heapq.heappush(queue, 11)
heapq.heappush(queue, 5)
print(queue)

# (3) 삭제 : 우선순위가 높은 (숫자가 작은 값)부터 나오게됩니다.
# heapq.heappop(리스트)
for i in range(len(queue)):
    print(heapq.heappop(queue))

# (4) 큰수부터 뽑기
# 숫자가 클수록 작아지는 개념 => 음수

heapq.heappush(queue, -3)
heapq.heappush(queue, -2)
heapq.heappush(queue, -7)
heapq.heappush(queue, -9)
heapq.heappush(queue, -14)
heapq.heappush(queue, -11)
heapq.heappush(queue, -5)
print(queue)


for i in range(len(queue)):
    print(heapq.heappop(queue)*-1)




