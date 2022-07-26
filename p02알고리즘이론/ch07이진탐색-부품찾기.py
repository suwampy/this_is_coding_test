def 부품찾기():
    n = int(input())
    list = list(map(int,input().split()))
    list.sort()

    m = int(input())
    check = list(map(int,input().split()))

    for i in check:
        result = search(list, i, 0, n-1)
        if result !=None:
            print('yes', end ='')
        else:
            print('no', end=' ')


def search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return None


if __name__ == '__main__':
    부품찾기()