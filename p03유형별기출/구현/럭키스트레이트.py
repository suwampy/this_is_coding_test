n = input() #점수

'''
럭키 스트레이트 = 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과
오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미

123456
1+2+3 = 4+5+6 
'''

left = 0
for i in range(len(n)//2):
    left += int(n[i])

right = 0
for i in range(len(n)//2 , len(n)):
    right += int(n[i])


if left == right:
    print("LUCKY")
else:
    print("READY")
