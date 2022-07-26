def 내가푼거():
    n,k = map(int, input().split())
    count = 0
    while n!=1:
        if n%k ==0:
            n=n/k
        else:
            n-1
        count=count+1
    print(count)

def 단순하게푸는예시():
    # n = 주어진 수
    # k = 나누는수
    n, k = map(int, input().split())
    result = 0

    # N이 K 이상이라면 K로 계속 나누기
    while n >= k:
        # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
        while n % k !=0:
            n -= 1
            result += 1
        # k로 나누기
        n //= k
        result +=1

def 답안예시():
    n, k = map(int, input().split())
    result = 0

    while True:
        # N==K로 나누어 떨어지는 수가 될때까지(N이 K의 배수가 될 때까지) 1씩 빼기
        # N=25, K=3
        target = (n//k)*k
        result += (n-target)
        n=target

        # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        if n<k:
            break

        # N을 K로 나누기
        result +=1
        n //= k

if __name__ == '__main__':
    내가푼거()