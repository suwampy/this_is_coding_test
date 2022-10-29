#c개의 공유기를 n개의 집에 적당히 설치해서 가장ㅇ 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
n, c = map(int, input())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

# [1,2,4,8,9]
start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while start<=end:
    mid = (start+end) // 2
    value = array[0]
    count = 1

    for i in range(1, n):
        if array[i] > mid + value:
            value = array[i]
            count += 1

    if count >= c:
        start = mid+1
        result = mid
    else:
        end = mid - 1