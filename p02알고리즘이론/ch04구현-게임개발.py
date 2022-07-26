def 게임개발():
    # N, M을 공백으로 구분하여 입력받기
    # 맵의 세로크기 N, 가로 크기 M
    n, m = map(int, input().split())

    # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
    '''
    eg . n=4, m=4
    d = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    '''
    d = [[0] * m for _ in range(n)]

    # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
    # 방향 direciton = 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽
    x, y, direction = map(int, input().split())
    d[x][y] = 1 # 현재 좌표 방문 처리

    # 전체 맵 정보를 입력받기
    # 육지인지 바다인지에 대한 정보
    # N개의 줄에 맵의 상태가 북쪽에서 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어짐. 맵의 외곽은 항상 바다
    # 0: 육지, 1: 바다
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))

    # 북, 동, 남, 서 방향 정의
    # (-1,0) (0,1) (1,0) (0,-1)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        # 왼쪽으로 회전
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 회전한 이후에 정면으로 가보지 않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count +=1
            turn_time = 0
            continue
        # 회전한 이후 정면으로 가보지 않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1

        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 갈 수 있다면 이동하기
            if array[nx][ny] == 0:
                x = nx
                y = ny
            # 뒤가 바다로 막혀있는 경우
            else:
                break
            turn_time = 0
    # 정답 출력
    print(count)
'''
현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정함
'''
# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

if __name__ == '__main__':
    게임개발()