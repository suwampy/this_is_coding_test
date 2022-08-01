# 우선순위 큐를 이용해서 풀자^_^
# 적게 걸리는음식부터 확인!! -> 모든 음식을 시간을 기준으로 정렬한 뒤, 시간이 적게 걸리는 음식부터 제거해나가기

import heapq
food_times = [3,1,2] # 각 음식을 모두 먹는 데 필요한 시간이 담겨 있는 배열
k = 5 # 방송이 중단된 시간

result = 0

# 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
if sum(food_times) <= k:
    result = -1

# 시간이 작은 음식분터 빼야하므로 우선순위 큐를 이용
q = []
for i in range(len(food_times)):
    # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
    heapq.heappush(q, (food_times[i], i+1))
'''
(1,2)
(2,3)
(3,1)
'''
sum_value = 0 # 먹기 위해 사용한 시간
previous = 0 # 직전에 다 먹은 음식 시간
length = len(food_times) # 남은 음식의 개수

# sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k(방송이 중단된 시간) 비교
while sum_value + ((q[0][0] - previous) * length) <= k:
    now = heapq.heappop(q)[0] # 시간이 적게 걸리는 음식부터 한개씩 빼기
    sum_value += (now-previous) * length
    length -= 1 # 다 먹은 음식 제외
    previous = now # 이전 음식 시간 재설정

# 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
result = sorted(q, key =lambda x: x[1]) # 음식의 번호 기준으로 정렬
result[(k -sum_value) % length][1]
