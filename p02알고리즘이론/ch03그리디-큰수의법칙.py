def 큰수의법칙_단순하게푸는답안():
    # 92p
    # 입력값 중에서 가장 큰 수와 두번째로 큰 수만 저장하면된다.....!!!이개념이가장중ㅇ요한듯
    # N, M, K를 공백으로 구분하여 입력받기
    # N : 배열의 크기
    # M : 더하는 횟수
    # K : 연속으로 더할 수 있는 횟수
    n, m, k = map(int, input().split())

    # N개의 수를 공백으로 구분하여 입력받기
    data = list(map(int, input().split()))

    data.sort() # 입력받은 수 정렬하기
    first = data[n-1] # 가장 큰 수
    second = data[n-2] # 두 번째로 큰 수

    result = 0

    while True:
        for i in range(k): # 가장 큰 수를 k번 더하기
            if m == 0: # m이 0이라면 반복문 탈출
                break
            result += first
            m -= 1 #더할 때마다 1씩 빼기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += second # 두 번째로 큰 수를 한 번 더하기
        m -= 1 # 더할 때마다 1씩 빼기

    print(result)

def 큰수의법칙_효율적인답안():
    # N, M, K를 공백으로 구분하여 입력받기
    n, m, k = map(int, input().split())
    # N개의 수를 공백으로 구분하여 입력받기
    data = list(map(int, input().split()))

    data.sort() # 입력받은 수 정렬
    first = data[n-1] # 가장 큰 수
    second = data[n-2] # 두 번째로 큰 수

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(m/(k+1)) * k
    count += m%(k+1)

    result = 0
    result += (count) * first # 가장 큰 수 더하기
    result += (m-count) * second # 두 번째로 큰 수 더하기
    print(result)


def 연습해보자():
    # n : 배열의 크기 (별로 상관 없음)
    # m : 더하는 횟수
    # k : 연속으로 더할 수 있는 횟수
    n,m,k = map(int, input().split())
    data = list(map(int,input().split()))

    data.sort()
    first = data[n-1]
    second = data[n-2]
    # n=5 m=8 k=3
    # 6,6,6,5,6,6,6,5
    # first*x + second*(m-x)
    # x를 구하자 x = 6...
    count = int(m/(k+1))*k

    # n=5 m=7 k=2
    # 6,6,5,6,6,5
    # 이 경우에는 m/(k+1)이 딱 떨어지지않음...ㅜ
    count += m%(k+1)

    result = 0
    result += (count) * first
    result += (m-count) * second

    print(result)

if __name__ == '__main__':
    큰수의법칙_효율적인답안()