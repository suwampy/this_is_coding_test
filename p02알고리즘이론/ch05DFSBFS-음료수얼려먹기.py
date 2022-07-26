def 음료수얼려먹기():
    # N, M을 공백으로 구분하여 입력받기
    global n, m
    n, m = map(int, input().split())

    # 2차원 리스트의 맵 정보 입력받기
    global graph
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    # 모든 노드에 대하여 음료수 채우기
    result = 0
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS 수행
            if dfs(i,j) == True:
                result +=1

# DFS로 특정한 노드를 방문한 뒤에 연결된 모드 노드들도 방문
'''
def dfs(v):
    v를 이미 방문한 곳으로 처리한다 
    for 각각의 v에 연결된 모든 정점 i에 대해서:
        if i에 방문하지 않았다면:
            dfs(i)

def dfs(v,visited=[]):
    visited.append(v)
    for i in graph[v]:
        if not i in visited:
            visited = dfs(i,visited)
    return visited # [1,2,5,6,7,3,4]
'''
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or \
            y <= -1 or y >=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x -1 ,y) #상
        dfs(x + 1, y)  # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True
    return False
if __name__ == '__main__':
    음료수얼려먹기()