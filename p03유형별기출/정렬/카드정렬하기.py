'''
정렬된 두 묶음의 숫자카드 A,B
두 묶음을 합쳐서 하나로 만드는 데에는 A=B번의 비교를 해야 함

e.g 10, 20, 40

(10+20) + (30+40) = 100
(10+40) + (50+20) = 120
(20+40) + (60+10) = 130


최소 몇 번의 비교가 필요?
'''

'''
항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장
매 상황에서 무조건 가장 작은 크기의 두 카드 묶음을 합치자
-> 우선순위 큐
- 원소를 넣었다 뺴는 것만으로 정렬된 결과를 얻을 수 있음
'''
import heapq

n = int(input())
heap = []

for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)