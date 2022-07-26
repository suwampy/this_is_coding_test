def 두배열의원소교체():
    n,k = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    print(a)
    print(b)

    for i in range(k):
        # A의 원소가 B의 원소보다 작은 경우
        if a[i] < b[i]:
            # 두 원소를 교체
            a[i], b[i] = b[i], a[i]
        else: # A의 원소가 B의 원소보다 크거나 같을 떄, 반복문을 탈출
            break

    print(sum(a))



if __name__ == '__main__':
    두배열의원소교체()