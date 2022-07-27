n, m = map(int, input().split()) # n 볼링공의 개수, m 공의 최대 무게 e.g 5,3
data = list(map(int, input().split())) # k 볼링공의 무게 e.g [1,3,2,3,2]

#공의 최대 무게 = 10
#1부터 10까지 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    #각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
'''
e.g
array[1] = 1
array[2] = 2
array[3] = 2
'''


result = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1) :
    n-= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)