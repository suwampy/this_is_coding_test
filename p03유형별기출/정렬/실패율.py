# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
# 전체 스테이지의 개수 N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번확 담긴 배열 stages가 매개변수로 주어질 때,
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열ㅇ르 return
'''
stages에는 1 이상 n+1 이하의 자연수가 담겨있음
- 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타냄
- 단, N+1 은 마지막 스테이지까지 클리어한 사용자를 나타냄
만약 실패율이 같은 스테이지가 있따면 작은 번호의 스테이지가 먼저 오도록 하면 됨
스테이지에 도달한 유저가 없는 경우 해달 스테이지의 실패율은 0으로 정의
'''

N = 5
stages = [2,1,2,6,2,4,3,3]

answer = []
length = len(stages)

for i in range(1, N+1):
    #현재 스테이지에 남아있는 수
    count = stages.count(i)

    # 실패율 계산
    if length == 0:
        fail = 0
    else:
        fail = count / length

    answer.append((i, fail))
    length -= count

# 실패율을 기준으로 각 스테이지를 내림차순 정렬
answer = sorted(answer, key=lambda t: t[1], reverse=True)

answer = [i[0] for i in answer]