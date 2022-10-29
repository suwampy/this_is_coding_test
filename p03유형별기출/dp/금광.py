# m번에 걸쳐서 매번 오른쪽 위, 오 른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 함

# 2차원 테이블을 이용한 다이나미 프로그래밍으로 해결
# 1. 왼쪽 위에서 오는 경우
# 2. 왼족 아래에서 오는 경우
# 3. 왼쪽에서 오는 경우

# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

#테스트 케이스 입력
for tc in range(int(input())):
    # 금광 정보 입력 4 * 3
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    # 왼쪽 열만 그대로 값을 남겨두면 됨
    for i in range(n):
        dp.append(array[index:index +m])
        index += m
    '''
    array = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]
    dp = [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]
    '''

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

result = 0
for i in range(n):
    result = max(result, dp[i][m-1])

print(result)