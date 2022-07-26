def 숫자카드게임_min함수를_이용하는_답안_예시():
    n,m = map(int, input().split())
    result = 0
    #한 줄씩 입력받아 확인
    for i in range(n):
        data = list(map(int,input().split()))
        #현재 줄에서 가장 작은 수 찾기
        min_value = min(data)
        # 가장 작은 수 들 중에서 가장 큰 수 찾기
        result = max(result, min_value)
    print(result)

def 이중반복문구조를이용하는답안예시():
    n,m = map(int, input().split())
    result = 0

    for i in range(n):
        data = list(map(int, input().split()))
        #현재 줄에서 가장ㅈ작은수찾기
        min_value=10001
        for a in data:
            min_value = min(min_value, a)
        #가장 작은 수 들 중에서 가장 큰 수 찾기
        result = max(result, min_value)

    print(result)

if __name__ == '__main__':
    숫자카드게임_min함수를_이용하는_답안_예시()