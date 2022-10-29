'''
고정점 = 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
a = {-15, -4, 2, 8, 13}
a[2] = 2
고정점 : 2
'''
from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, input().split()))

result = -1
for i in range(n):
    idx = bisect_left(arr, arr[i])
    if idx == arr[i]:
        result = arr[i]

print(result)

# 이진 탐색 재귀로 구현
def binary_search(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작ㅇ느 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, mid+1, end)

n = int(input())
array = list(map(int, input().split()))

# 이진 탐색 수행
index = binary_search(array, 0, n-1)