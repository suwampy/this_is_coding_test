def 시각():
    h = int(input())
    # 완전 탐색 알고리즘
    # 확인(탐색) 해야 할 전체 데이터의 개수가 100만개 이하일 때 완탐 사용하면 적절
    count = 0
    for i in range(h+1): # 시간
        for j in range(60): # 분
            for k in range(60): #초
                # 매 시각 안에 3이 포함되어 있다면 카운트 증가
                if '3' in str(i) +str(j) +str(k) :
                    count += 1


if __name__ == '__main__':
    시각()