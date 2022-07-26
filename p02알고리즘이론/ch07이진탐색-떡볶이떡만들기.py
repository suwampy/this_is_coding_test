if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    start = 0
    end = max(array)

    result = 0
    while(start<=end):
        total = 0
        mid=(start+end)//2
        for x in array:
            # 잘랐을때의 떡의 양 계산
            if x >mid:
                total += x -mid
        #떡의 양ㅇ이 부족한 경우 더 맣ㄴ이 자르기
        if total<m:
            end = mid -1
        else:
            result = mid
            start = mid +1

    print(result)

def 떡():
    n,m=list(map(int, input().split(' ')))
    array = list(map(int, input().split()))

    # 이진 탐색을 위한 시작점과 끝점 설정
    start = 0
    end = max(array)

    #이진탐색 수행
    result = 0
    while(start <= end):
        total = 0
        mid=(start+end)//2

        for x in array:
            # 잘랐을 때의 떡의 양 계산
            if x>mid:
                total += x-mid
        # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        if total < m:
            end = mid -1
        # 떡의 양이 충분한 경우 덜자르기 (오른쪽부분 탐색)
        else:
            result = mid
            start = mid +1

